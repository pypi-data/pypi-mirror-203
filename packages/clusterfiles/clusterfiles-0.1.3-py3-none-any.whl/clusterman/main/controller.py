import datetime
import json
import zirconium as zr
from autoinject import injector
import logging
import clusterman.main.orm as orm
from threading import RLock
import pathlib
import flask
import queue
"""
file path {local_storage_root}{/target_path/one/two/}{file_name.ext}
"""

DEFAULT_RECRAWL_INTERVAL = 3600

class DequeueException(Exception):
    pass


class EmptyQueue(DequeueException):
    pass


class LockedQueue(DequeueException):
    pass


@injector.injectable_global
class SyncController:

    config: zr.ApplicationConfig = None

    @injector.construct
    def __init__(self):
        self.local_storage_root = self._normalize_path(self.config.as_str(("clusterman", "storage_dir")))
        self._download_on_creation = self.config.as_bool(("clusterman", "download_on_create"), default=True)
        self._cluster_name = self.config.as_str(("clusterman", "cluster_name"), default="_default")
        self._lock_time = self.config.as_int(("clusterman", "file_copy_max_lock_time"), default=3600)
        self._keep_successes = self.config.as_int(("clusterman", "success_retention_time"), default=172800)
        self._keep_errors = self.config.as_int(("clusterman", "failure_retention_time"), default=1814400)
        self.log = logging.getLogger("clusterman.syncdb")
        self._security_check_root(self.local_storage_root)
        self._queue_lock = RLock()
        self._sync_map_lock = RLock()
        self._refresh_lock = RLock()
        self._auto_refresh = {
            "download_mappings": [self.config.as_int(("clusterman", "refresh_times", "mappings"), default=3600), None, "download_mappings"],
            "check_sync": [self.config.as_int(("clusterman", "refresh_times", "sync_check"), default=15), None, "check_sync_maps"],
            "vacuum": [self.config.as_int(("clusterman", "refresh_times", "vacuum"), default=86400), None, "vacuum_local"]
        }
        self._result_queues = []

    def add_result_queue(self, q):
        self._result_queues.append(q)

    def _security_check_root(self, root):
        root_str = str(root)
        if root_str == "/":
            raise ValueError("LSR cannot be unix root")
        if root_str == "C:/" or root_str == "C:\\":
            raise ValueError("LSR cannot be C:/")

    def check_path(self, path):
        path = str(self._normalize_path(str(pathlib.Path(path).resolve()), False, False))
        lsr = str(self.local_storage_root)
        return path.startswith(lsr) or (path == lsr[:-1])

    def _copy_to_local(self, sm: orm.SharedMap):
        with self._sync_map_lock:
            existing = orm.LocalMap.query.filter_by(shared_map_id=sm.id).first()
            if existing:
                cleanup = sm.deprecated and not existing.deprecated
                redownload = existing.deprecated and not sm.deprecated
                existing.copy_shared(sm)
                orm.db.session.commit()
                if cleanup:
                    self.enqueue_from_map(existing, "cleanup")
                elif redownload:
                    self.enqueue_from_map(existing, "sync")
            else:
                existing = orm.LocalMap(
                    shared_map_id=sm.id,
                    last_checked=None,
                )
                existing.copy_shared(sm)
                orm.db.session.add(existing)
                orm.db.session.commit()
                if self._download_on_creation and not existing.deprecated:
                    self.enqueue_from_map(existing, "sync")

    def define_sync_mapping(self, source_root, target_root, metadata: dict, recrawl_interval=None):
        if recrawl_interval is None:
            recrawl_interval = DEFAULT_RECRAWL_INTERVAL
        source_root = self._normalize_path(source_root)
        target_root = self._normalize_path(target_root)
        with self._sync_map_lock:
            existing = orm.LocalMap.query.filter_by(
                source_root=source_root
            ).first()
            do_sync = False
            if existing:
                do_sync = existing.deprecated
                existing.target_root = target_root
                existing.recrawl_interval = recrawl_interval
                existing.map_metadata = json.dumps(metadata)
                existing.deprecated = False
            else:
                do_sync = True
                existing = orm.LocalMap(
                    source_root=source_root,
                    target_root=target_root,
                    metadata=json.dumps(metadata),
                    recrawl_interval=recrawl_interval,
                    source_root_length=len(source_root),
                    deprecated=False
                )
                orm.db.session.add(existing)
            orm.db.session.commit()
            if do_sync:
                self.enqueue_from_map(existing, "sync")

    def remove_sync_mapping(self, source_root):
        source_root = self._normalize_path(source_root)
        with self._sync_map_lock:
            existing = orm.LocalMap.query.filter_by(
                source_root=source_root
            ).first()
            if existing:
                existing.deprecated = True
                orm.db.session.commit()
                return True
            return False

    def _normalize_path(self, path, suf_slash = True, pre_slash = False):
        path = str(path).replace("\\", "/")
        if suf_slash and not path.endswith("/"):
            path += "/"
        if pre_slash and not path.startswith("/"):
            path = "/" + path
        return path

    def define_shared_sync_mapping(self, source_root, target_root, metadata: dict, recrawl_interval=None, cluster_name="_default"):
        source_root = self._normalize_path(source_root)
        target_root = self._normalize_path(target_root)
        if recrawl_interval is None:
            recrawl_interval = DEFAULT_RECRAWL_INTERVAL
        existing = orm.SharedMap.query.filter_by(
            source_root=source_root,
            cluster_name=cluster_name,
        ).first()
        if existing:
            existing.target_root = target_root
            existing.recrawl_interval = recrawl_interval
            existing.map_metadata = json.dumps(metadata)
        else:
            existing = orm.SharedMap(
                source_root=source_root,
                target_root=target_root,
                metadata=json.dumps(metadata),
                recrawl_interval=recrawl_interval,
                cluster_name=cluster_name,
                deprecated=False
            )
            orm.db.session.add(existing)
        orm.db.session.commit()

    def remove_shared_sync_mapping(self, source_root, cluster_name):
        source_root = self._normalize_path(source_root)
        existing = orm.SharedMap.query.filter_by(
            source_root=source_root,
            cluster_name=cluster_name
        ).first()
        if existing:
            existing.deprecated = True
            orm.db.session.commit()
            return True
        return False

    def refresh(self):
        with self._refresh_lock:
            ct = datetime.datetime.now()
            for key in self._auto_refresh:
                refresh_time, last_time, cb = self._auto_refresh[key]
                if (not refresh_time) or refresh_time <= 0:
                    continue
                if last_time is None or (last_time + datetime.timedelta(seconds=refresh_time)) <= ct:
                    getattr(self, cb)()
                    self._auto_refresh[key][1] = ct

    def download_mappings(self):
        if self._cluster_name != "":
            for sm in orm.SharedMap.query.filter_by(cluster_name=self._cluster_name):
                self._copy_to_local(sm)

    def check_sync_maps(self, force_all: bool = False):
        with self._sync_map_lock:
            dt = datetime.datetime.utcnow()
            for lm in orm.LocalMap.query.all():
                if (not force_all) and lm.recrawl_interval is None:
                    continue
                if (not force_all) and lm.last_checked is not None and (dt - lm.last_checked).total_seconds() < lm.recrawl_interval:
                    continue
                self.enqueue_from_map(lm, 'sync')
                lm.last_crawled = dt
                orm.db.session.commit()

    def cleanup_from_source(self, source_file):
        source_file = self._normalize_path(source_file, False)
        return self.enqueue_from_file(source_file, "cleanup")

    def sync_from_source(self, source_file, force: bool = False):
        source_file = self._normalize_path(source_file, False)
        return self.enqueue_from_file(source_file, "force_sync" if force else "sync")

    def enqueue_from_file(self, source_file, op):
        for lm in orm.LocalMap.query.order_by(orm.LocalMap.source_root_length.desc()):
            if source_file.startswith(lm.source_root):
                self.enqueue_from_map(lm, op, source_file[len(lm.source_root):])
                return True
        return False

    def enqueue_from_map(self, lm: orm.LocalMap, op, basename=""):
        path = pathlib.Path(f"{self.local_storage_root}{lm.target_root}{basename}").resolve()
        self.enqueue(
            lm.source_root + basename,
            str(path),
            lm.map_metadata,
            op,
            lm.priority_boost or 0
        )

    def enqueue_as_child(self, source_path, target_path, item, op=None):
        self.enqueue(
            str(source_path),
            str(target_path),
            item["metadata"],
            op or item["operation"],
            item["priority"]
        )

    def enqueue(self, source_path, target_path, metadata, operation, priority=0):
        with self._queue_lock:
            existing = orm.QueueItem.query.filter_by(
                target_file=target_path,
                operation=operation,
                state=orm.STATE_READY
            ).first()
            if not existing:
                existing = orm.QueueItem(
                    source_file=source_path,
                    target_file=target_path,
                    item_metadata=metadata,
                    operation=operation,
                    priority=priority or 0,
                    state=orm.STATE_READY,
                    locked_by=None,
                    locked_since=None,
                    queued_time=datetime.datetime.utcnow()
                )
                orm.db.session.add(existing)
                orm.db.session.commit()
            elif existing.priority < priority:
                existing.priority = priority
                orm.db.session.commit()

    def dequeue(self):
        with self._queue_lock:
            found = orm.QueueItem.query.filter_by(state=orm.STATE_READY).order_by(orm.QueueItem.priority.desc()).first()
            if not found:
                raise EmptyQueue()
            if not found.obtain_lock():
                # Locked by someone else, skip it (let the dequeuer grab the next row if they want)
                raise LockedQueue()
            lo = orm.LocalObject.query.filter_by(local_path=found.target_file).first()
            if not lo:
                lo = orm.LocalObject(
                    local_path=found.target_file
                )
                orm.db.session.add(lo)
                orm.db.session.commit()
            if not lo.obtain_lock():
                # Delay releasing the original item to prevent it from being reprocessed immediately
                found.release_at(lo.locked_since + datetime.timedelta(self._lock_time))
                orm.db.session.commit()
                raise LockedQueue()
            # Now we should have an exclusive lock on the local file and the queue item
            return {
                "id": found.id,
                "file_id": lo.id,
                "file_print": lo.fingerprint,
                "source_file": found.source_file,
                "target_file": pathlib.Path(found.target_file),
                "metadata": found.item_metadata,
                "operation": found.operation,
                "priority": found.priority
            }

    def release(self, item, success, changed=False):
        with self._queue_lock:
            qitem = orm.QueueItem.query.filter_by(id=item['id']).first()
            if qitem:
                if success is None:
                    qitem.release()
                else:
                    qitem.ack(bool(success))
            else:
                self.log.warning(f"Attempted to update state on non-existing queue item {item['id']}")
            lo = orm.LocalObject.query.filter_by(id=item['file_id']).first()
            if lo:
                lo.release()
            else:
                self.log.warning(f"Attempted to update state on non-existing local item {item['file_id']}")
            orm.db.session.commit()
            if success is True and changed is True:
                for q in self._result_queues:
                    try:
                        q.put_nowait(item)
                    except queue.Full:
                        pass

    def vacuum_local(self):
        with self._queue_lock:
            orm.QueueItem.clean_acks(self._keep_successes, False)
            orm.QueueItem.clean_acks(self._keep_errors, True)
            orm.QueueItem.ready_timeouts(self._lock_time)
            orm.LocalObject.clear_timeouts(self._lock_time)
            orm.db.session.commit()
            #orm.db.session.execute(orm.db.sql("VACUUM"))

    def get_fingerprint(self, local_path):
        lo = orm.LocalObject.query.filter_by(local_path=str(local_path)).first()
        if lo:
            return lo.fingerprint
        return None

    def set_fingerprint(self, local_path, remote_print):
        with self._queue_lock:
            lo = orm.LocalObject.query.filter_by(local_path=str(local_path)).first()
            if lo:
                lo.remote_fingerprint = remote_print
            else:
                lo = orm.LocalObject(
                    local_path=str(local_path),
                    fingerprint=remote_print
                )
                orm.db.session.add(lo)
            orm.db.session.commit()

    def create_databases(self):
        orm.db.create_all()
        with self._sync_map_lock:
            orm.db.create_all('local_map_db')
        with self._queue_lock:
            orm.db.create_all('local_lock_db')


@injector.injectable_global
class MessageHandler:

    controller: SyncController = None

    @injector.construct
    def __init__(self):
        pass

    def handle_message(self, content):
        with flask.current_app.app_context():
            correl_id = content['message_id'] if 'message_id' in content else None
            if not correl_id:
                self.log.warning(f"Message missing message_id property")
            if "op" in content:

                if content["op"] == "create_db":
                    self.controller.create_databases()
                elif content["op"] == "add_local_map":
                    if "source_root" not in content:
                        raise ValueError("Missing source_root")
                    if "target_root" not in content:
                        raise ValueError("Missing target root")
                    if "metadata" not in content:
                        content["metadata"] = {}
                    if "recrawl_interval" not in content:
                        content["recrawl_interval"] = None
                    self.controller.define_sync_mapping(
                        content["source_root"],
                        content["target_root"],
                        content["metadata"],
                        content["recrawl_interval"]
                    )
                elif content["op"] == "vacuum":
                    self.controller.vacuum_local()
                elif content["op"] == "reload":
                    self.controller.download_mappings()
                elif content["op"] == "check_sync":
                    self.controller.check_sync_maps(False)
                elif content["op"] == "sync_all":
                    self.controller.check_sync_maps(True)
                elif content["op"] == "sync":
                    if 'source' not in content:
                        raise ValueError(f"Missing source on sync message {correl_id}")
                    elif not self.controller.sync_from_source(content['source'], 'force' in content and content['force']):
                        raise ValueError(f"No source mapping found for {content['source']} while synchronizing it")
                elif content["op"] == "remove":
                    if 'source' not in content:
                        raise ValueError(f"Missing source on remove message {correl_id}")
                    elif not self.controller.cleanup_from_source(content['source']):
                        raise ValueError(f"No source mapping found for {content['source']} while removing it")
                else:
                    raise ValueError(f"Unrecognized operation in {correl_id}: {content['op']}")
            else:
                raise ValueError(f"Missing op in message {correl_id}")

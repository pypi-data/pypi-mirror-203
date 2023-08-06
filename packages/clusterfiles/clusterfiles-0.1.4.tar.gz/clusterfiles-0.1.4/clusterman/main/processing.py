import threading
import zirconium as zr
from .controller import SyncController, DequeueException
from autoinject import injector
import logging
import universalio as uio
import os
import pathlib
import time
import datetime


class RefreshController(threading.Thread):

    controller: SyncController = None

    @injector.construct
    def __init__(self, app):
        super().__init__()
        self.app = app
        self._halt = threading.Event()
        self.daemon = True

    def halt(self):
        self._halt.set()

    @injector.as_thread_run
    def run(self):
        with self.app.app_context():
            while not self._halt.is_set():
                self.controller.refresh()
                self._halt.wait(5)


class FileSyncController(threading.Thread):

    controller: SyncController = None
    config: zr.ApplicationConfig = None

    @injector.construct
    def __init__(self, app):
        super().__init__()
        self.app = app
        self.log = logging.getLogger("clusterman.syncengine")
        self._partial_file_retention = self.config.as_int(("clusterman", "partial_file_retention_time"), default=86400)
        self._success_callbacks = []
        self._halt = threading.Event()
        self.daemon = True

    def halt(self):
        self._halt.set()

    @injector.as_thread_run
    def run(self):
        with self.app.app_context():
            while not self._halt.is_set():
                item = None
                success = None
                changed = False
                try:
                    item = self.controller.dequeue()
                    success, changed = self.handle_item(item)
                except DequeueException as ex:
                    self._halt.wait(5)
                    continue
                except (SystemExit, KeyboardInterrupt) as ex:
                    success = None
                    raise ex
                except Exception as ex:
                    self.log.exception(str(ex))
                    success = False
                finally:
                    if item:
                        self.controller.release(item, success, changed)

    def handle_item(self, item) -> (bool, bool):
        if item['operation'] in ('sync', 'force_sync'):
            return self.download_file(item, item['operation'] == 'force_sync')
        elif item['operation'] == 'cleanup':
            return self.cleanup_file(item)
        else:
            raise ValueError(f"Unrecognized operation: {item['operation']}")

    def secure_make_dir(self, path):
        if not self.controller.check_path(path):
            raise ValueError(f"Invalid path, not under controller directory: {path}")
        if not path.parent.exists():
            self.secure_make_dir(path.parent)
        if not path.exists():
            path.mkdir()

    def download_file(self, item, force) -> (bool, bool):
        full_path = item['target_file'].resolve()
        self.secure_make_dir(full_path.parent)
        if not self.controller.check_path(full_path):
            raise ValueError(f"Invalid path, not under controller directory: {full_path}")
        src = uio.FileWrapper(item['source_file'])
        dest = uio.FileWrapper(full_path)
        # If it is a directory, process it recursively
        if src.is_dir():
            found = []
            for path, mirror in src.crawl(
                mirror_resource=dest,
                recursive=True
            ):
                self.controller.enqueue_as_child(
                    str(path),
                    str(mirror),
                    item
                )
                found.append(pathlib.Path(str(mirror)).resolve())
            gate_time = None
            if self._partial_file_retention > 0:
                gate_time = datetime.datetime.now() + datetime.timedelta(seconds=self._partial_file_retention)
            for file in os.scandir(str(dest)):
                ext = file.name[file.name.rfind("."):] if "." in file.name else ""
                # Partial files should be omitted
                if ext.startswith(".partial") and ext[8:].isdigit():
                    if gate_time is None:
                        # Keep forever
                        continue
                    mtime = datetime.datetime.fromtimestamp(file.stat().st_mtime)
                    if mtime >= gate_time:
                        # Keep for now
                        continue
                path = pathlib.Path(file.path).resolve()
                if path not in found:
                    self.controller.enqueue_as_child(
                        "",
                        path,
                        item,
                        "cleanup"
                    )
            return True, False
        # Otherwise, we will check the fingerprint and continue
        else:
            current_print = src.fingerprint()
            last_print = self.controller.get_fingerprint(item['target_file']) if item['operation'] == 'sync' else None
            if current_print is None or last_print is None or last_print != current_print:
                src.copy(dest,
                         require_not_exists=False,
                         allow_overwrite=True,
                         recursive=True,
                         use_partial_file=True)
                self.controller.set_fingerprint(item['target_file'], current_print)
                return True, True
            return True, False

    def cleanup_file(self, item) -> (bool, bool):
        dest = item['target_file'].resolve()
        if not self.controller.check_path(dest):
            raise ValueError(f"Invalid path, not under controller directory: {dest}")
        if not dest.is_symlink():
            # Does not exist
            if not dest.exists():
                return True, False
            # Is a directory
            elif dest.is_dir():
                for file in os.scandir(dest):
                    if not file.is_symlink():
                        self.controller.enqueue_as_child(
                            "",
                            file.path,
                            item
                        )
                return True, False
            # Is a file
            elif dest.is_file():
                dest.unlink(True)
                return True, True
        else:
            self.log.warning(f"Attempt to remove symlink {dest}, skipping")
        return False, False

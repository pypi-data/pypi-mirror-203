import flask_sqlalchemy
import datetime
import uuid

db = flask_sqlalchemy.SQLAlchemy()

STATE_READY = 1
STATE_UNACK = 2
STATE_PENDING_RELEASE = 3
STATE_ACK = 10
STATE_ACK_FAILED = 11


class _MappingMixin:
    id = db.Column(db.Integer, primary_key=True, nullable=False)
    source_root = db.Column(db.String(4196), nullable=False)
    target_root = db.Column(db.String(4196), nullable=False)
    recrawl_interval = db.Column(db.Integer)
    map_metadata = db.Column(db.Text)
    deprecated = db.Column(db.Boolean)
    priority_boost = db.Column(db.Integer)


class SharedMap(_MappingMixin, db.Model):

    __table_name__ = "shared_map"
    __table_args__ = (
        db.UniqueConstraint('source_root', name='ux_local_map_source_root'),
    )

    cluster_name = db.Column(db.String(1024), nullable=False)

    def __init__(self, **kwargs):
        super().__init__(**kwargs)


class LocalMap(_MappingMixin, db.Model):

    __table_name__ = "local_map"
    __bind_key__ = 'local_map_db'

    __table_args__ = (
        db.UniqueConstraint('source_root', name='ux_local_map_source_root'),
    )

    shared_map_id = db.Column(db.Integer, nullable=True)
    last_checked = db.Column(db.DateTime(timezone=True), nullable=True)
    source_root_length = db.Column(db.Integer)

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def copy_shared(self, sm: SharedMap):
        self.source_root = sm.source_root
        self.target_root = sm.target_root
        self.recrawl_interval = sm.recrawl_interval
        self.map_metadata = sm.map_metadata
        self.deprecated = sm.deprecated
        self.priority_boost = sm.priority_boost
        self.source_root_length = len(sm.source_root)


class QueueItem(db.Model):

    __table_name__ = "queue"
    __bind_key__ = 'local_lock_db'

    id = db.Column(db.Integer, primary_key=True, nullable=False)
    source_file = db.Column(db.String(4196), nullable=True)
    target_file = db.Column(db.String(4196), nullable=False)
    item_metadata = db.Column(db.Text)
    operation = db.Column(db.String(1024), nullable=False)
    priority = db.Column(db.Integer)
    state = db.Column(db.Integer)
    locked_by = db.Column(db.String(1024), nullable=True)
    locked_since = db.Column(db.DateTime(timezone=True), nullable=True)
    restarts = db.Column(db.Integer, default=0)
    queued_time = db.Column(db.DateTime(timezone=True), nullable=True)
    ack_time = db.Column(db.DateTime(timezone=True), nullable=True)
    release_time = db.Column(db.DateTime(timezone=True), nullable=True)

    def obtain_lock(self):
        global db
        lock_time = datetime.datetime.utcnow()
        lock_id = str(uuid.uuid4())
        st = (
            db.update(QueueItem).values({
                "locked_by": lock_id,
                "locked_since": lock_time,
                "state": STATE_UNACK
            })
            .where(QueueItem.id == int(self.id))
            .where(QueueItem.locked_by == None)
        )
        db.session.execute(st)
        db.session.commit()
        db.session.refresh(self)
        return self.locked_by == lock_id

    def release_at(self, dt):
        self.state = STATE_PENDING_RELEASE
        self.release_time = dt

    def ack(self, failed: bool):
        self.state = STATE_ACK if not failed else STATE_ACK_FAILED
        self.ack_time = datetime.datetime.utcnow()

    def release(self):
        self.state = STATE_READY

    @staticmethod
    def ready_timeouts(lock_time):
        gate = datetime.datetime.utcnow() + datetime.timedelta(seconds=lock_time)
        st = (
            db.update(QueueItem)
            .values({
                "locked_by": None,
                "locked_since": None,
                "restarts": QueueItem.restarts + 1,
                "state": STATE_READY
            })
            .where(QueueItem.state == STATE_UNACK)
            .where(QueueItem.locked_since < gate)
        )
        db.session.execute(st)
        st = (
            db.update(QueueItem)
            .values({
                "locked_by": None,
                "locked_since": None,
                "restarts": QueueItem.restarts + 1,
                "state": STATE_READY
            })
            .where(QueueItem.state == STATE_PENDING_RELEASE)
            .where(QueueItem.release_time <= datetime.datetime.utcnow())
        )
        db.session.execute(st)

    @staticmethod
    def clean_acks(retention_time: int, for_ack_failed: bool = False):
        gate = datetime.datetime.utcnow() + datetime.timedelta(seconds=retention_time)
        st = (
            db.delete(QueueItem)
                .where(QueueItem.state == (STATE_ACK if not for_ack_failed else STATE_ACK_FAILED))
                .where(QueueItem.ack_time < gate)
        )
        db.session.execute(st)


class LocalObject(db.Model):

    __table_name__ = "local_object"

    __bind_key__ = 'local_lock_db'

    id = db.Column(db.Integer, primary_key=True, nullable=False)
    local_path = db.Column(db.String(4196), nullable=False, unique=True)
    locked_by = db.Column(db.String(1024), nullable=True)
    locked_since = db.Column(db.DateTime(timezone=True), nullable=True)
    fingerprint = db.Column(db.String(1024), nullable=True)

    def obtain_lock(self):
        global db
        lock_time = datetime.datetime.utcnow()
        lock_id = str(uuid.uuid4())
        st = (
            db.update(LocalObject).values({
                "locked_by": lock_id,
                "locked_since": lock_time
            })
            .where(LocalObject.id == self.id)
            .where(LocalObject.locked_by == None)
        )
        db.session.execute(st)
        db.session.commit()
        db.session.refresh(self)
        return self.locked_by == lock_id

    def release(self):
        self.locked_by = None
        self.locked_since = None

    @staticmethod
    def clear_timeouts(lock_time):
        gate = datetime.datetime.utcnow() + datetime.timedelta(seconds=lock_time)
        st = (
            db.update(LocalObject)
            .values({
                "locked_by": None,
                "locked_since": None
            })
            .where(QueueItem.locked_since < gate)
        )
        db.session.execute(st)

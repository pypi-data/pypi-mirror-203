import pika
import zirconium as zr
from autoinject import injector
import json
import logging
import threading
import itsdangerous
from .controller import MessageHandler


"""
instructions.cluster.CLUSTER_NAME.reload
instructions.cluster.CLUSTER_NAME.sync_all
instructions.cluster.CLUSTER_NAME.sync_file

instructions.global.none.sync_file
"""


@injector.injectable_global
class MessageCreator:

    config: zr.ApplicationConfig = None

    @injector.construct
    def __init__(self):
        self._secret_keys = self.config.as_str(("clusterman", "ampq", "secret_keys"))
        self._signer = itsdangerous.Serializer(self._secret_keys)

    def pack_message(self, cluster_name, op, data: dict = None):
        package = {
            "op": op,
            "cluster": cluster_name,
        }
        if data:
            package.update(data)
        return self._signer.dumps(data)

    def build_message(self, message):
        return self._signer.loads(message)


@injector.injectable_global
class MessageQueueSender:

    config: zr.ApplicationConfig = None
    builder: MessageCreator = None

    @injector.construct
    def __init__(self):
        super().__init__()
        self.daemon = True
        self.log = logging.getLogger("clusterman.mqsend")
        uri = self.config.as_str(("clusterman", "ampq", "broker_uri"))
        self.exchange_name = self.config.as_str(("clusterman", "ampq", "exchange_name"))
        self._secret_keys = self.config.as_str(("clusterman", "secret_keys"))
        self.conn = pika.BlockingConnection(pika.URLParameters(uri))
        self.channel = self.conn.channel()
        self.channel.exchange_declare(self.exchange_name, 'topic', durable=True)

    def reload(self, cluster_name=None):
        self.channel.basic_publish(
            exchange=self.exchange_name,
            routing_key=self._routing_key(cluster_name, 'reload'),
            body=self.builder.pack_message(cluster_name, "reload")
        )

    def check_sync(self, cluster_name=None):
        self.channel.basic_publish(
            exchange=self.exchange_name,
            routing_key=self._routing_key(cluster_name, 'check_sync'),
            body=self.builder.pack_message(cluster_name, "check_sync")
        )

    def sync_all(self, cluster_name=None):
        self.channel.basic_publish(
            exchange=self.exchange_name,
            routing_key=self._routing_key(cluster_name, 'sync_all'),
            body=self.builder.pack_message(cluster_name, "sync_all")
        )

    def sync_file(self, source_file, cluster_name=None):
        self.channel.basic_publish(
            exchange=self.exchange_name,
            routing_key=self._routing_key(cluster_name, 'sync'),
            body=self.builder.pack_message(cluster_name, "sync", {
                "source": str(source_file)
            })
        )

    def remove_file(self, source_file, cluster_name=None):
        self.channel.basic_publish(
            exchange=self.exchange_name,
            routing_key=self._routing_key(cluster_name, 'remove'),
            body=self.builder.pack_message(cluster_name, "remove", {
                "source": str(source_file)
            })
        )

    def _routing_key(self, cluster_name, op):
        if cluster_name:
            return f"instructions.cluster.{cluster_name}.{op}"
        else:
            return f"instructions.global.none.{op}"


class MessageQueueListener(threading.Thread):

    config: zr.ApplicationConfig = None
    handler: MessageHandler = None
    builder: MessageCreator = None

    @injector.construct
    def __init__(self, app):
        super().__init__()
        self.app = app
        self.daemon = True
        self._channel = None
        self._halt = threading.Event()
        self.log = logging.getLogger("clusterman.mqlisten")
        self._check_for_halts = self.config.as_int(("clusterman", "ampq", "receive_timeout"), default=1)
        self.uri = self.config.as_str(("clusterman", "ampq", "broker_uri"))
        self.exchange_name = self.config.as_str(("clusterman", "ampq", "exchange_name"))
        self.cluster_name = self.config.as_str(("clusterman", "ampq", "cluster_name"), default="_default")

    def config_valid(self):
        return self.uri and self.exchange_name

    def halt(self):
        self._halt.set()

    @injector.as_thread_run
    def run(self):
        with self.app.app_context():
            conn = pika.BlockingConnection(pika.URLParameters(self.uri))
            self._channel = conn.channel()
            self._channel.exchange_declare(self.exchange_name, 'topic', durable=True)
            result = self._channel.queue_declare(queue='', exclusive=True)
            self._channel.queue_bind(exchange=self.exchange_name, queue=result.method.queue,
                               routing_key=f'instructions.cluster.{self.cluster_name}.*')
            self._channel.queue_bind(exchange=self.exchange_name, queue=result.method.queue,
                               routing_key=f'instructions.global.*.*')
            self._channel.basic_qos(prefetch_count=2)
            self._channel.basic_consume(
                queue=result.method.queue,
                on_message_callback=self.handle_message,
                auto_ack=False
            )
            while not self._halt.is_set():
                m, p, b = self._channel.consume(queue=result.method.queue, auto_ack=False, inactivity_timeout=self._check_for_halts)
                if m is None:
                    self._halt.wait(0.1)
                else:
                    self.handle_message(self._channel, m, p, b)

    def handle_message(self, ch, method, properties, body):
        try:
            content = self.builder.build_message(body)
            self.handler.handle_message(content)
        except ValueError as ex:
            self.log.exception(ex)
        finally:
            ch.basic_ack(delivery_tag=method.delivery_tag)

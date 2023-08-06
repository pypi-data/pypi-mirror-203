import socket
import threading
import logging
from autoinject import injector
from .controller import MessageHandler
import zirconium as zr
import json
from select import select
import time

SEPARATOR = chr(31)


class MainListener(threading.Thread):

    config: zr.ApplicationConfig = None
    handler: MessageHandler = None

    @injector.construct
    def __init__(self, app):
        super().__init__()
        self.app = app
        self._host = self.config.as_str(("clusterman", "commands", "host"), default="localhost")
        self._port = self.config.as_int(("clusterman", "commands", "port"), default=7012)
        self.log = logging.getLogger("clusterman.main")
        self._halt = threading.Event()
        self._server = None
        self.daemon = True

    def halt(self):
        self._halt.set()

    @injector.as_thread_run
    def run(self):
        with self.app.app_context():
            self._server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            self._server.bind((self._host, self._port))
            while not self._halt.is_set():
                self._server.listen(5)
                ready, _, _ = select([self._server], [], [], 0.5)
                if ready:
                    clientsocket, address = self._server.accept()
                    data = clientsocket.recv(6000).decode("utf-8").split(SEPARATOR)
                    response = self.handle(data)
                    clientsocket.sendall(response.encode("utf-8"))
                    clientsocket.close()
                    self._halt.wait(0.01)

    def handle(self, raw_data: list) -> str:
        if len(raw_data) < 3:
            return "invalid structure"
        message_id, op, data = raw_data
        try:
            m = {
                "message_id": message_id,
                "op": op
            }
            if data:
                m.update(json.loads(data))
            self.handler.handle_message(m)
            return "good"
        except Exception as ex:
            self.log.error(ex)
            self.log.exception(ex)
            return f"{type(ex)}: {str(ex)}"


@injector.inject
def send_message(message_id: str, op: str, content: dict = None, config: zr.ApplicationConfig = None):
    enc_content = "{}"
    if content is not None:
        enc_content = json.dumps(content)
    parts = [
        message_id,
        op,
        enc_content
    ]
    message = SEPARATOR.join(s.replace(SEPARATOR, "?").replace("\n", " ") for s in parts)
    host = config.as_str(("clusterman", "commands", "host"), default="localhost")
    port = config.as_int(("clusterman", "commands", "port"), default=7012)
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
        sock.connect((host, port))
        sock.sendall(bytes(message + "\n", "utf-8"))
        received = str(sock.recv(1024), "utf-8").strip("\r\n\t ")
        if received == "good":
            return True
        raise ValueError(received)

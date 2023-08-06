
import zirconium as zr
from .mainline import MainListener
import signal
from autoinject import injector
from .processing import FileSyncController, RefreshController
import time
from .ampq import MessageQueueListener


class MainRunner:

    def __init__(self, app):
        self.app = app
        self.processors = []
        self.ref = None
        self._halting = False
        self._invalid_ampq_config = False
        self._processing_threads = 1
        self.listener = None
        self.ampq = None

    def shutdown(self, signum, frame):
        self._halting = True
        if self.listener:
            self.listener.halt()
        for x in self.processors:
            x.halt()
        if self.ampq:
            self.ampq.halt()
        if self.ref:
            self.ref.halt()

    @injector.inject
    def run_forever(self, config: zr.ApplicationConfig = None):
        self._processing_threads = config.as_int(("clusterman", "processing_threads"), default=1)
        if self._processing_threads < 1:
            self._processing_threads = 1
        signal.signal(signal.SIGINT, self.shutdown)
        signal.signal(signal.SIGBREAK, self.shutdown)
        while not self._halting:
            self._boot_all()
            time.sleep(1)
        if self.listener:
            self.listener.join()
        for x in self.processors:
            x.join()
        if self.ampq:
            self.ampq.join()
        if self.ref:
            self.ref.join()

    def _boot_all(self):
        if self._halting:
            return
        if self.ref is None or not self.ref.is_alive():
            self.ref = RefreshController(self.app)
            self.ref.start()
        if self.listener is None or not self.listener.is_alive():
            self.listener = MainListener(self.app)
            self.listener.start()
        if (not self._invalid_ampq_config) and (self.ampq is None or not self.ampq.is_alive()):
            self.ampq = MessageQueueListener(self.app)
            if self.ampq.config_valid():
                self.ampq.start()
            else:
                self.ampq = None
                self._invalid_ampq_config = True
        active_processors = []
        for p in self.processors:
            if p.is_alive():
                active_processors.append(p)
        self.processors = active_processors
        for i in range(len(self.processors), self._processing_threads):
            p = FileSyncController(self.app)
            p.start()
            self.processors.append(p)

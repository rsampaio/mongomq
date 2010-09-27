from base import Monque
import threading
from multiprocessing import Process

class MonqueWorker(Monque):
    def __init__(self, queue):
        self.queue = queue
        Monque.__init__(self)

    def work(self):
        job = self.dequeue(self.queue)
        self._work_on_thread(job['func'], *job['args'], **job['kwargs'])

    def _work_on_thread(self, func, *args, **kwargs):
        thread = threading.Thread(target=func, args=args, kwargs=kwargs)
        thread.start()

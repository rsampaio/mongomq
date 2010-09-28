from base import Monque
import threading
try:
    from multiprocessing import Process
except Exception, e:
    print "Multiprocessing module is required to use a 'fork' scheduler"

_available_scheduler = ('thread', 'fork')

class MonqueWorker(Monque):
    def __init__(self, queue, sched_type='thread'):
        self.queue = queue
        if sched_type in _available_scheduler:
            self.scheduler = sched_type
            Monque.__init__(self)
        else:
            e = Exception("Scheduler is not supported: %s" % sched_type)
            raise e

    def work(self, limit=1):
        while True:
            job = self.dequeue(self.queue, limit=limit)
            if not job:
                break
            if self.scheduler == 'thread':
                self._work_on_thread(job['func'], *job['args'], **job['kwargs'])
            elif self.scheduler == 'fork':
                self._work_on_process(job['func'], *job['args'], **job['kwargs'])

    def _work_on_thread(self, func, *args, **kwargs):
        thread = threading.Thread(target=func, args=args, kwargs=kwargs)
        thread.start()

    def _work_on_process(self, func, *args, **kwargs):
        proc = Process(target=func, args=args, kwargs=kwargs)
        proc.start()

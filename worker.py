from base import Monque

class MonqueWorker(Monque):
    def __init__(self):
        Monque.__init__(self)

    def work(self):
        pass

    def _work_on_thread(self, func, *args, **kwargs):
        pass

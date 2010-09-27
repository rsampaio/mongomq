import pymongo
import time
import os

class Monque(object):

    def __init__(self, server="localhost", port=27017):
        self._connect(server, port)

    def _connect(self, server, port):
        self.mongo = pymongo.Connection(server, port)
        self.db = self.mongo.monque
    
    def enqueue(self, queue, job, *args, **kwargs):
        _queue = self.db[queue]
        _queue.insert(self._encode(job, *args, **kwargs))

    def dequeue(self, queue):
        job = self.db[queue].find_one()
        if not job:
            time.sleep(1)
        self.db[queue].remove({'_id': job['_id']})
        return self._decode(job)

    def _encode(self, job, *args, **kwargs):
        if not isinstance(job, basestring):
            job_name = job.__name__
            job_module = job.__module__
        return {
            'func': job_name, 
            'module': job_module, 
            'args': args, 
            'kwargs': kwargs
        }

    def _decode(self, job):
        mod = __import__(job['module'], {}, {}, str(job['func']))
        func = getattr(mod, str(job['func']))
        job.update({'func': func})
        return job
        

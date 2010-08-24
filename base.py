import pymongo

class MongoMQ(object):

    def __init__(self):
        self.mongo = pymongo.Connection()
        self.db = self.mongo.mongomq

    def enqueue(self, queue, job, *args, **kwargs):
        _queue = self.db[queue]
        _queue.insert(self._encode(job, *args, **kwargs))
    
    def dequeue(self, queue):
        job = self.db[queue].find(
                limit=1, 
                sort=[('_id', pymongo.DESCENDING)]
            ).next()
        return self._decode(job)

    def _encode(self, job, *args, **kwargs):
        if not isinstance(job, basestring):
            job_name = job.__name__
            job_module = job.__module__
        return {
            'job': job_name, 
            'module': job_module, 
            'args': args, 
            'kwargs': kwargs
        }

    def _decode(self, job):
        mod = __import__(job['module'], {}, {}, str(job['job']))
        func = getattr(mod, str(job['job']))
        return func
        

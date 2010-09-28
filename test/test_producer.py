from monque import Monque
import time

def prod_test(*args):
    print args, time.time()

def produce():
    m = Monque()
    for arg in ('a', 'b', 'c', 'd'):
        m.enqueue('test', prod_test, arg)

if __name__ == "__main__":
    produce()

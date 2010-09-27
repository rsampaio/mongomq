from monque import MonqueWorker
import test_producer

def work():
    w = MonqueWorker('test')
    w.work()

if __name__ == "__main__":
    work()

from monque import Monque

def prod_test(*args):
    print args

def produce():
    m = Monque()
    #while True:
    m.enqueue('test', prod_test, 'aaa')


if __name__ == "__main__":
    produce()

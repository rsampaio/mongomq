import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
from test_producer import *
from test_consumer import *

def test():
    produce()
    work()

if __name__ == "__main__":
    test()


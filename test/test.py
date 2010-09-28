import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
import test_producer
import test_consumer

def test():
    test_producer.produce()
    test_consumer.work()

if __name__ == "__main__":
    test()


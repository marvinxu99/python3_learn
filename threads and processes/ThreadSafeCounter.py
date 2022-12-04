# https://superfastpython.com/thread-safe-counter-in-python/

# example of a thread-safe counter
from threading import Thread
from threading import Lock
 
# thread safe counter class
class ThreadSafeCounter():
    # constructor
    def __init__(self):
        # initialize counter
        self._counter = 0
        # initialize lock
        self._lock = Lock()
 
    # increment the counter
    def increment(self):
        with self._lock:
            self._counter += 1
 
    # get the counter value
    def value(self):
        with self._lock:
            return self._counter
 
# task executed by threads
def task(counter):
    # increment the counter
    for _ in range(100000):
        counter.increment()
 
# create the counter
counter = ThreadSafeCounter()
# create 10 threads to increment the counter
threads = [Thread(target=task, args=(counter,)) for _ in range(10)]

# start all threads
for thread in threads:
    thread.start()

# wait for all threads to finish
for thread in threads:
    thread.join()

# report the value of the counter
print(counter.value())

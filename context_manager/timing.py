# timing.py

from time import perf_counter

class Timer:
    def __enter__(self):
        self.start = perf_counter()
        self.end = 0.0
        return lambda: self.end - self.start

    def __exit__(self, *args):
        self.end = perf_counter()

'''
When you use Timer in a with statement, .__enter__() gets called. This method 
uses time.perf_counter() to get the time at the beginning of the with code block 
and stores it in .start. It also initializes .end and returns a lambda function 
that computes a time delta. In this case, .start holds the initial state or time measurement.
'''

if __name__ == "__main__":
    from time import sleep
    
    with Timer() as timer:
        # Time-consuming code goes here...
        sleep(0.5)
    
    print(f"time: { timer() }")
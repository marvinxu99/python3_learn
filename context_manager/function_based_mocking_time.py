# https://realpython.com/python-with-statement/

'''
Mocking the Time

As a final example of how to create custom context managers with @contextmanager, 
say you’re testing a piece of code that works with time measurements. The code 
uses time.time() to get the current time measurement and do some further computations. 
Since time measurements vary, you decide to mock time.time() so you can test your code.

Here’s a function-based context manager that can help you do that:

>>> from contextlib import contextmanager
>>> from time import time

>>> @contextmanager
... def mock_time():
...     global time
...     saved_time = time
...     time = lambda: 42
...     yield
...     time = saved_time
...

>>> with mock_time():
...     print(f"Mocked time: {time()}")
...
Mocked time: 42

>>> # Back to normal time
>>> time()
1616075222.4410584

Inside mock_time(), you use a global statement to signal that you’re going to modify 
the global name time. Then you save the original time() function object in saved_time so you can safely restore it later. The next step is to monkey patch time() using a lambda function that always returns the same value, 42.

The bare yield statement specifies that this context manager doesn’t have a useful object to send back to the with target variable for later use. After yield, you reset the global time to its original content.

When the execution enters the with block, any calls to time() return 42. Once you leave the with code block, calls to time() return the expected current time. That’s it! Now you can test your time-related code.

'''

from contextlib import contextmanager
from time import time

@contextmanager
def mock_time():
    global time
    saved_time = time
    time = lambda: 42
    yield
    time = saved_time

if __name__ == "__main__":
    with mock_time():
        print(f"Mocked time: {time()}")

    # time restored
    print(f'time restored: { time() }')
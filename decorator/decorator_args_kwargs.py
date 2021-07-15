# Decorator with *args and **kwargs

from functools import wraps
from time import perf_counter, sleep


def decorator(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        # do something before
        result = func(*args, **kwargs)
        # do something after
        return result
    return wrapper

@decorator
def func():
    pass

""" example"""
def timer(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        start = perf_counter()
        result = func(*args, **kwargs)
        end = perf_counter()
        duration = end - start
        arg = str(*args)
        print(f'{func.__name__}({arg}) = {result} -> {duration: .8f}s')
        return result
    return wrapper


@timer
def fib(n):
    """Return the nth value from the Fibonacci sequence"""
    if n < 2:
        return n
    else:
        return fib(n-1) + fib(n-2)

@timer
def lazy_func(n):
    sleep(n)

# print(fib(15))
print(lazy_func(2))
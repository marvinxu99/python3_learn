# Decorator Pattern
from time import time


def performance(fn):
    def wrapper(*args, **kwargs):
        t1 = time()
        result = fn(*args, **kwargs)
        t2 = time()
        print(f'it took {t2-t1} s')
        return result
    return wrapper


@performance
def long_time():
    print('1')
    for i in range(10000000):
        i*5


@performance
def long_time2():
    print('2')
    for i in list(range(10000000)):
        i*5


long_time()
long_time2()

#########################################
def generator(start,stop):
    while (start<=stop):
        yield start
        print(f'start={start}')
        start+=1
for counter in generator(3,4):
    print(f'counter={counter}')

'''
counter=3
start=3
counter=4
start=4
'''
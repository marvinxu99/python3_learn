import itertools as it


def evens():
    ''' Generate even integers, stating with 0. '''
    n = 0
    while True:
        yield n
        n += 2


evens = evens()
print(list(next(evens) for _ in range(5)))


def odds():
    ''' Generate odd integers, starting with 1.'''
    n = 1
    while True:
        yield n
        n += 2


odds = odds()
print(list(next(odds) for _ in range(5)))

'''
That is pretty straightforward, but with itertools you can do this much 
more compactly. The function you need is itertools.count(), which does 
exactly what it sounds like: it counts, starting by default 
with the number 0.
'''

evens = it.count(step=2)
print(list(next(evens) for _ in range(5)))

odds = it.count(start=1, step=2)
print(list(next(odds) for _ in range(5)))

count_with_floats = it.count(start=0.5, step=0.75)
print(list(next(count_with_floats) for _ in range(5)))

negative_count = it.count(start=-1, step=-0.5)
print(list(next(negative_count) for _ in range(5)))

'''
The example that made me realize the power of the infinite iterator was 
the following, which emulates the behavior of the built-in enumerate() function.

Below is a simple example, but think about it: you just enumerated a list 
without a for loop and without knowing the length of the list ahead of time.
'''
li = list(zip(it.count(), ['a', 'b', 'c', 'd']))
print(li)

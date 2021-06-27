'''
This module implements a number of iterator building blocks inspired by 
constructs from APL, Haskell, and SML. Each has been recast in a form 
suitable for Python.
https://docs.python.org/3.6/library/itertools.html#module-itertools
https://docs.python.org/3.6/library/itertools.html#itertools-recipes

'''

import itertools as it

def print_x(comment, list):
    print(comment, end=' ')
    print(list)


'''
Under the hood, the zip() function works, in essence, by calling iter() 
on each of its arguments, then advancing each iterator returned by 
iter() with next() and aggregating the results into tuples. 
The iterator returned by zip() iterates over these tuples.
'''
list1 = list(zip([1, 2, 3], ['a', 'b', 'c']))

print("1. zip example:", end=" ")
print(list1)

'''
The map() built-in function is another “iterator operator” that, in its 
simplest form, applies a single-parameter function to each element of 
an iterable one element at a time:

The map() function works by calling iter() on its second argument, advancing 
this iterator with next() until the iterator is exhausted, and applying the 
function passed to its first argument to the value returned by next() at each step.
'''
list2 = list(map(len, ['abc', 'de', 'fghi']))
print_x('2. map() example: ', list2)


def len_x(x):
    return f'length: {len(x)}'


list3 = list(map(len_x, ['abc', 'de', 'fghi']))
print('3. custom func: ', list3)

'''
lambda - An anonymous inline function consisting of a single expression 
which is evaluated when the function is called. The syntax to create a 
lambda function is lambda [parameters]: expression
'''
list4 = list(map(lambda x: f'length: {len(x)}', ['abc', 'de', 'fghi']))
print('4. lambda example:', list4)

'''
This is what is meant by the functions in itertools forming an “iterator 
algebra.” itertools is best viewed as a collection of building blocks that 
can be combined to form specialized “data pipelines” like the one in the 
example below.
'''
list5 = list(map(sum, zip([1, 2, 3], [4, 5, 6])))
print('5. "iterator algebra example": ', list5)

x = [1,2,3,4,5]
y = ['a','b','c']
print_x("6. Unequal lenght: ", list(zip(x,y)))
print_x("6. Unequal lenght: ", list(it.zip_longest(x,y, fillvalue=None)))

def grouper(inputs, n, fillvalue=None):
    iters = [iter(inputs)] * n
    print(*iters)
    print(*iters)
    return it.zip_longest(*iters, fillvalue=fillvalue)

print_x("7. Grouper: ", list(grouper(x,4,fillvalue=None)))

'''
You have three $20 dollar bills, five $10 dollar bills, two $5 dollar bills, 
and five $1 dollar bills. How many ways can you make change for a $100 dollar bill?
'''
bills = [20, 20, 20, 10, 10, 10, 10, 10, 5, 5, 1,1,1,1,1]
makes_100 = []
for n in range(1, len(bills)+1):
    for combination in it.combinations(bills, n):
        if sum(combination) == 100:
            makes_100.append(combination)

print(makes_100)
print("combinations for $100:", set(makes_100))


'''
How many ways are there to make change for a $100 bill 
using any number of $50, $20, $10, $5, and $1 dollar bills?
'''
# bills = [50, 20, 10, 5, 1]
bills = [50, 20, 10, 5]
makes_100 = []
for n in range(2, 21):
    for combination in it.combinations_with_replacement(bills, n):
        if sum(combination) == 100:
             makes_100.append(combination)
print(len(makes_100))
print(makes_100)
print(list(range(2,21)))


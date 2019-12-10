# map, filter, zip, and reduce
from functools import reduce

my_list1 = [1, 2, 3, 5, 6, 7, 8]
my_list2 = [10, 20, 30, 50, 60, 70, 80]

# map
def multiply_by2(item):
    return item * 2


print(list(map(multiply_by2, my_list1)))
print(my_list1)

# filter
def only_odd(item):
    return item % 2 != 0


print(list(filter(only_odd, my_list1)))
print(my_list1)

# zip - put two lists into a list of tuples
print(list(zip(my_list1, my_list2)))

my_list3 = [101, 201, 301, 501, 601, 701, 801]
print(list(zip(my_list1, my_list2, my_list3)))

# reduce
def accumulator(acc, item):
    return acc + item

print(reduce(accumulator, my_list1, ))

from functools import reduce

# Lamba expressions
# # they are used only once, and they are anonymous
# A lambda function can take any number of arguments, but can only have one expression.

my_list1 = [1, 2, 3, 5, 6, 7, 8]

# map


def multiply_by2(item):
    return item * 2


print(list(map(multiply_by2, my_list1)))

# using lambda
print("using lambda expression:")
print(list(map(lambda item: item * 2, my_list1)))

# reudce using lambda
print(reduce(lambda acc, item: acc + item, my_list1))

# using lambda expression to square my list
print(list(map(lambda item: item*item, my_list1)))

# sort as per the 2nd numner in tuples
a = [(0, 2), (4, 3), (9, 9), (10, -1)]

a.sort(key=lambda item: item[1])
print(a)

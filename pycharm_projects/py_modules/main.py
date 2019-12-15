# Python built-in modules
# https://docs.python.org/3/py-modindex.html

from utils import multiply, divide    # module
from shopping.shopping_cart import buy    # package
from Lib import keyword

import random

print(multiply(2, 3))
print(divide(2, 3))

print(buy('apple'))

if __name__ == '__main__':
    print("please run this")

# To determine if a string is a keyword.
print(keyword.iskeyword(print))

# print out all the key words
kwlist = keyword.kwlist
kwlist.sort(key=lambda x: x.lower())
print(kwlist)

print(f"random = {random.random()}")
print(f"random = {random.randint(1, 10)}")
print(f"random = {random.choice([1, 2, 3, 4, 5])}")

my_list = [1,2,3,4,5,6,7,8]
random.shuffle(my_list)
print(my_list)


# help(random)
# print(dir(random))
# The array type can hold homogeneous data types and operate
# on them more efficiently while using less memory

from array import array

# TODO: Create an array of integer numbers
arr1 = array('i', [2, 4, 6, 8, 10, 12, 14, 16, 18, 20])
print(arr1.typecode)
print("Array 1 item szie:", arr1.itemsize)

# TODO: Add additional items to the array
arr1.insert(0, 0)
arr1.append(22)
arr1.extend([24, 26, 28])
print(arr1)

# TODO: iterate over the array content like any other list
for i, elem in enumerate(arr1):
    arr1[i] = elem * 2
print(arr1)

# TODO: Try to add a non-integer number to the array
# arr1.insert(1, 'a')
# '''TypeError: an integer is required (got type str)'''

# TODO: Create an array to hold bytes instead of ints
arr2 = array('B', [18, 102, 182, 56, 89, 5, 254, 32, 64, 50])
print(arr2.typecode)
print(arr2.itemsize)
print(arr2)

# TODO: try to add an item that's out of range
# arr2.append(300)
# """OverflowError: unsigned byte integer is greater than maximum"""

# TODO: Convert an array to a list
list1 = arr2.tolist()
print(list1)
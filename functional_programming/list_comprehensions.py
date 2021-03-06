# list, dict, set comprehensions

my_list1 = [char for char in "hello"]

my_list2 = [num for num in range(0, 100)]

my_list3 = [num*2 for num in range(0, 100)]

my_list4 = [num**2 for num in range(0, 100) if num % 2 == 0]


my_list11 = list("hello")
my_list21 = list(range(0, 100))

# print(my_list1)
# print(my_list11)

# print(my_list2)
# print(my_list21)

print(my_list4)

# set comprehension
my_set1 = {char for char in "hello"}
my_set2 = {num**2 for num in range(0, 100) if num % 2 == 0}

print(my_set1)
print(my_set2)

# dictionary
simple_dict = {
    'a': 1,
    'b': 2
}

#my_dict = {key:value**2 for key, value in simple_dict.items()}
my_dict1 = {k:v**2 for k,v in simple_dict.items() if v%2==0}
print(my_dict1)

my_dict2 = {num:num*2 for num in [1,2,3]}
print(my_dict2)

# find the duplicates
some_list = ['a', 'b', 'c', 'b', 'd', 'm', 'n', 'n']

duplicates = list(set([char for char in some_list if some_list.count(char) > 1]))

print(duplicates)
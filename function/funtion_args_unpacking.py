# Why Python Is Great:
# Function argument unpacking

def myfunc(x, y, z):
    print(x, y, z)

tuple_vec = (1, 0, 1)
dict_vec = {'x': 1, 'y': 0, 'z': 1}

myfunc(*tuple_vec)

myfunc(*dict_vec)  # print out keys

myfunc(**dict_vec)  # print out values

# example.
def multi_add(*args):
    result = 0
    for x in args:
        result += x
    return result

multi_add(1, 2, 3)
'''
6
'''
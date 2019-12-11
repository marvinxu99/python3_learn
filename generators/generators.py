# generator
range(100)
list(range(100))

def make_list(num):
    result = []
    for i in range(num):
        result.append(i*2)
    return result


my_list = make_list(100)
print(my_list)

# generator
def generator_func(num):
    for i in range(num):
        yield i

for item in generator_func(100):
    print(item)

g = generator_func(100):
    next(g)

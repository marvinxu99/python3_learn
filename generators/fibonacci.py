def fib(num):
    if num == 0:
        return 0
    elif num == 1:
        return 1
    else:
        return fib(num-1) + fib(num)


print(fib(10))


# fib2 - not using memory
def fib2(n):
    a = 0
    b = 1
    for i in range(n):
        yield a
        temp = a
        a = b
        b = temp + b


for x in fib2(20):
    print(x)

for x in fib2(20):
    print(x)

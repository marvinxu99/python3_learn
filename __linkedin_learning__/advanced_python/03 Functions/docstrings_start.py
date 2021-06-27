# Demonstrate the use of function docstrings

l1 = [1, 2, 3, 4, 5]
l2 = [6, 7, 8, 9, 10]

print(list(map(lambda x,y: x+y, l1, l2)))

def myFunction(arg1, arg2=None):
    print(arg1, arg2)


def main():
    print(myFunction.__doc__)


if __name__ == "__main__":
    main()

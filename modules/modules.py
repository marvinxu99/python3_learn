import sys
import os
import random

def main():
    v = sys.version_info
    print(f'Python version is { v }')
    print("Python version {}.{}.{}".format(*v))

    s = os.name + ' ' + sys.platform
    print(f'OS is: {s}')
 
    s = os.getenv('PATH')
    print(s)

    s = os.getcwd()
    print(s)

    s = os.urandom(25).hex()
    print(s)

    s = random.randint(1, 1000)
    print(s)

    x = list(range(25))
    print(x)
    random.shuffle(x)
    print(x)


if __name__ == '__main__':
    main()
#!/usr/bin/env python3
# Copyright 2009-2017 BHG http://bw.org/

# String is immutable.
s1 = "hello world."
s2 = s1.upper()

print(id(s1), id(s2))

s3 = 'this string' " that string"
print(s3)


# Reverse string 
class ReverseString(str):
    def __str__(self) -> str:
        return self[::-1]

print(ReverseString("hello word."))

def main():
    print("Hellow, World.".upper())
    print("Hellow, World.".lower())
    print("hellow, world.".capitalize())
    print("Hellow, World.".title())
    print("Hellow, World.".swapcase())

    print('Hell, World. {}'.format(42 * 7))

    s = 'Hell, World. {}'
    print(s.format(42 * 7))

    # Using positional arguments
    s = 'Hell, World. {1} {0} {2}'
    print(s.format((42 * 7), 99, 'test'))

    s = 'Hell, World. {2} {1} {0} {2}'
    print(s.format((42 * 7), 99, 'test'))

    # you can name the variables.
    x = 42
    y = 73
    print('Hell, World. {xx} {yy} {xx}'.format(xx = x, yy = y))

    print('Hell, World. {xx:<5} {yy:5}'.format(xx = x, yy = y))
    print('Hell, World. {xx:<5} {yy:+05}'.format(xx = x, yy = y))

    x = 42 * 567 * 1000
    print('Hell, World. big number: {:,}'.format(x))
    print('Hell, World. big number: {:,}'.format(x).replace(',', '.'))

    x = 42
    print('Hell, World. big number: {:.3f}'.format(x))

    print('Hell, World. big number: {:x}'.format(x))
    print('Hell, World. big number: {:o}'.format(x))
    print('Hell, World. big number: {:b}'.format(x))

if __name__ == '__main__': main()

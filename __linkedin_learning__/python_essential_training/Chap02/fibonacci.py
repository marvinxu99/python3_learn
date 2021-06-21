#!/usr/bin/env python3
# Copyright 2009-2017 BHG http://bw.org/

# simple fibonacci series
# the sum of two elements defines the next set

#from time import sleep

a, b = 0, 1
while b < 1000:
    print(b, end = ' ', flush = True)
    a, b = b, a + b

print() # line ending

x = f'This is a test { a:>09}'
print(x)
print(f'This is a test {a:>09} {b:<9}')

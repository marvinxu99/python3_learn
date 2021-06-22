#!/usr/bin/env python3
# Copyright 2009-2017 BHG http://bw.org/

x = [1,2,3, "two"]
y = [1,2,3, "two"]
print('x is {}'.format(x))
print(type(x))
print(id(x[3]))
print(id(y[3]))

x = (1,2,3, "two")
y = (1,2,3, "two")

if isinstance(x, tuple):
    print('yes')
else:
    print('Nope')

x = 5 == 7

print(x)
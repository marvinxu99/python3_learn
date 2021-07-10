#!/usr/bin/env python3
# Copyright 2009-2017 BHG http://bw.org/


x = (1, 2, 3, 4, 5)
y = x
print(x)
print(y)

x = (1, 2, 3, 4, 5)
y = list(reversed(x))
#y = tuple(reversed(x))
print(x)
print(y)
'''
(1, 2, 3, 4, 5)
[5, 4, 3, 2, 1]
'''
 
print(sum(x))   # => 15
print(sum(x, 10))   # => 25
print(min(x))      
print(max(x))

# enumerate()
x = ('cat', 'dog', 'rabbit', 'velociraptor')
for i, v in enumerate(x):
    print(f'{i} - {v}')
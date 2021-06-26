#!/usr/bin/env python3
# Copyright 2009-2017 BHG http://bw.org/

class bunny:
    def __init__(self, n):
        self._n = n
    
    def __repr__(self) -> str:
        return f'repr: the number of bunnies is {self._n} 👍'

    def __str__(self) -> str:
        return f'str: the number of bunnies is {self._n}'

x = bunny(48)
print(x)          # str: the number of bunnies is 48
print(repr(x))    # repr: the number of bunnies is 48 👍
print(ascii(x))   # repr: the number of bunnies is 48

print(chr(128406))
print(ord('🖖'))   # ord() gives the unicode value
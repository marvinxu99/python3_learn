#!/usr/bin/env python3
# Copyright 2009-2017 BHG http://bw.org/
import math

def main():
    seq = range(11)
    seq2 = [x * 2 for x in seq]
    seq3 = list(range(11))
    seq4 = [x for x in seq if x %3 !=0]

    # Create a tuple
    seq5 = [(x, x**2) for x in seq]

    seq5 = [round(math.pi, i) for i in seq]

    # create a dictionary:
    seq6 = { x: x**2 for x in seq }

    # Create a set 
    seq7 = { x for x in "superduper" if x not in 'pd'}

    print_list(seq)
    print_list(seq2)

    print(seq)
    print(seq2)
    print(seq3)
    print(seq4)
    print(seq5)
    print(seq6)
    print(seq7)

def print_list(o):
    for x in o: print(x, end = ' ')
    print()

if __name__ == '__main__': main()

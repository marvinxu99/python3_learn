#!/usr/bin/env python3
# Copyright 2009-2017 BHG http://bw.org/

print('Hello, World.')


def generator(start,stop):
    while (start<=stop):
        yield start
        print(f'start={start}')
        start+=1
for counter in generator(3,4):
    print(f'counter={counter}')

def main():
    do()
def do():
    print('test')

main()

#!/usr/bin/env python3
# Copyright 2009-2017 BHG http://bw.org/

def main():
    animals = { 'kitten': 'meow', 'puppy': 'ruff!', 'lion': 'grrr',
        'giraffe': 'I am a giraffe!', 'dragon': 'rawr' }
    
    animals2 = dict(kitten = 'meow', puppy = 'ruff!', 
                lion = 'grrr', giraffe = 'I am a giraffe!', 
                dragon = 'rawr' )

    print_dict(animals)
    print("--------------")
    print_dict(animals2)

def print_dict(o):
    for x in o: print(f'{x}: {o[x]}')


if __name__ == '__main__': main()

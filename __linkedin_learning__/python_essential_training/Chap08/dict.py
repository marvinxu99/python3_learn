#!/usr/bin/env python3
# Copyright 2009-2017 BHG http://bw.org/

def main():
    animals = { 'kitten': 'meow', 'puppy': 'ruff!', 'lion': 'grrr',
        'giraffe': 'I am a giraffe!', 'dragon': 'rawr' }
    
    animals2 = dict(kitten = 'meow', puppy = 'ruff!', 
                lion = 'grrr', giraffe = 'I am a giraffe!', 
                dragon = 'rawr' )

    for k in animals.keys():
        print(k)

    for v in animals.values():
        print(v)

    print_dict(animals)
    print("--------------")
    print_dict(animals2)

def print_dict(o):
    # for x in o: print(f'{x}: {o[x]}')
    for k,v in o.items(): 
        print(f'{k}: {v}')


if __name__ == '__main__': main()

#!/usr/bin/env python3
# Copyright 2009-2017 BHG http://bw.org/

def main():
    # sounds = ("purr", "gurle", "moow")
    # kitten(*sounds)
    kitten("purr", "gurle", "moow")


def kitten(*args):
    if len(args):
        for arg in args:
            print(arg)
    else:
        print('Meow.')


if __name__ == '__main__': main()

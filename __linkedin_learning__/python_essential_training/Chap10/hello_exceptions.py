#!/usr/bin/env python3
# Copyright 2009-2017 BHG http://bw.org/

import sys

def main():
    try:
        #x = int("foo")
        x = 5/0
    except ValueError:
        print('I caught a value error.')
    except (TypeError, ZeroDivisionError) as err:
        print(f"Error caught: { err }")
    except:
        print(f'unkown error: { sys.exc_info()[0] }; { sys.exc_info()[1] }')
    else:  
        print('going well. No error caught.')
    finally:
        print("Python exception is cool.")

if __name__ == '__main__': main()

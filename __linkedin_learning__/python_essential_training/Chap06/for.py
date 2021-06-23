#!/usr/bin/env python3
# Copyright 2009-2017 BHG http://bw.org/

animals = ( 'bear', 'bunny', 'dog', 'cat', 'velociraptor' )

for pet in animals:
    print(pet)

for x in [1, 2, 3]:
    if x == 2: continue
    print(x)
else:
    print('this executes due to no break')
# An else statement after a loop will only execute if the loop exits normally.

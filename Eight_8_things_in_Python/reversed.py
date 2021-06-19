'''
reversed(sequence)

(1) An iterable is anythng that you can loop over using a for loop
(2) e.g., list, tuple, string, sets and dictionaries
(3) sequence is a subset of iterables that have:
- a length
- an index
- can be sliced
(4) examples of iterables that are not sequences are:
- dictionaries, sets, files, generators
'''

'''
three ways: 
reverse()  - can not use on immuntables, tuple, string
slicing    - create a copy
reversed() - return an iterator
'''


countries = ['Netherlands', 'Nigeria', 'Jordan', 'Nepal', 'Niger', 'Japan']

# reverse() will reverse a sequence in-place, meaning modifying the sequence itself.
# slicing creates a reversed copy of a sequence.

countries.reverse()
print(countries)

print(countries[::-1])

print(countries)
print(countries[4:2:-1])

reversed_countries = reversed(countries)
print(list(reversed_countries))



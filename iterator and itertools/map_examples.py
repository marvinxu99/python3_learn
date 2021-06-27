# If you want to convert each of the lists to a list of integers, you can do

from itertools import chain

a, b = ['1','2','3'], ['1','2']
c, d = map(lambda x: map(int,x), [a, b])
print(type(c), type(d))
print(list(c), list(d))
'''
<class 'map'> <class 'map'>
[1, 2, 3] [1, 2]
'''

print(list(map(int, chain(a,b))))
'''
[1, 2, 3, 1, 2]
'''

# examle of 3 iterables 
# if you want to pass more than iterable as arguments, 
# then the function also has to accept that many number of parameters
print("Examle of multiples iterables")
a, b, c = [1, 2, 3, 4, 5], [1, 2, 3], [1, 2, 3]
print(list(map(lambda x, y, z: x + y + z, a, b, c)))
'''
[3, 6, 9]
'''
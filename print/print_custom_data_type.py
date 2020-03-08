'''
Printing Custom Data Types

For simple objects without any logic, whose purpose is to carry data, youâ€™ll 
typically take advantage of namedtuple, which is available in the standard 
library. Named tuples have a neat textual representation out of the box:
'''

from collections import namedtuple

Person = namedtuple('Person', 'name age')

jdoe = Person('John Doe', 42)

print(jdoe)


'''
Python gives you a lot of freedom when it comes to defining your own 
data types if none of the built-in ones meet your needs. Some of them, such as 
named tuples and data classes, offer string representations that look good 
without requiring any work on your part. Still, for the most flexibility, 
you’ll have to define a class and override its magic methods described above.
'''

'''
Understanding Python Print
You know how to use print() quite well at this point, but knowing what it is 
will allow you to use it even more effectively and consciously.
'''
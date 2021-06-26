# int
x = '47'
y = int(x)
print(f'x is { type(x) }')
print(f'x is { x }')
print(f'y is { type(y) }')
print(f'y is { y }')
'''
x is <class 'str'>
x is 47
y is <class 'int'>
y is 47
'''

# float
x = '-47.3'
y = float(x)
print(f'x is { type(x) }')
print(f'x is { x }')
print(f'y is { type(y) }')
print(f'y is { y }')
'''
x is <class 'str'>
x is -47.3
y is <class 'float'>
y is -47.3
'''

x = 47
y = divmod(x, 3)      # return the tuple (x//y, x%y)
print(f'x is { type(x) }')
print(f'x is { x }')
print(f'y is { type(y) }')
print(f'y is { y }')
'''
x is <class 'int'>
x is 47
y is <class 'tuple'>
y is (15, 2)
'''

x = 47
y = complex(x, 73)
# y = x + 73j 
print(f'x is { type(x) }')
print(f'x is { x }')
print(f'y is { type(y) }')
print(f'y is { y }')
'''
x is <class 'int'>
x is 47
y is <class 'complex'>
y is (47+73j)
'''

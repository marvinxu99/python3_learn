import os
print(f'Hello, {os.getlogin()}! How are you?')

# 'sep' has to be either a string or None, but the latter has the same effect as 
# the default space
print('hello', 'world', sep=None)
print('hello', 'world', sep=' ')
print('hello', 'world', sep='\n')
print('home', 'user', 'documents', sep='/')

# let print() handle the unpacking
print(*['jdoe is', 42, 'years old'])

print('node', 'child', 'child', sep=' -> ')

print('line1\nline2\nline3')

# Checking file integrity...ok
print('Checking file integrity...', end='')
print('ok')

'''
Printing in a Nutshell
 * Calling Print
 * Separating Multiple Arguments
 * Preventing Line Breaks
'''
print('Printing in a Nutshell', end='\n * ')
print('Calling Print', end='\n * ')
print('Separating Multiple Arguments', end='\n * ')
print('Preventing Line Breaks')


with open('file.txt') as file_object:
	for line in file_object:
		print(line)

# The following effectively removes one \n if there are two. 
with open('file.txt') as file_object:
...     for line in file_object:
...         print(line, end='')


#
linex ="this is a new line \n\n"
print(linex)
print(linex.rstrip())
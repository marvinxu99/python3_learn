s = 'This is a long string with a bunch of words in it.'

# Split into a list
print(s.split())
print(type(s.split()))
'''
['This', 'is', 'a', 'long', 'string', 'with', 'a', 'bunch', 'of', 'words', 'in', 'it.']
<class 'list'>
'''

print(s.split('i'))
'''
['Th', 's ', 's a long str', 'ng w', 'th a bunch of words ', 'n ', 't.']
'''

l = s.split()
s2 = ' -- '.join(l)
print(s2)
'''
This -- is -- a -- long -- string -- with -- a -- 
bunch -- of -- words -- in -- it.
'''
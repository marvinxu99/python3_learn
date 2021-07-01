# Demonstrate the usage of Counter objects
'''
c = Counter(a=3, b=1)
d = Counter(a=1, b=2)
c + d                       # add two counters together:  c[x] + d[x]
Counter({'a': 4, 'b': 3})
c - d                       # subtract (keeping only positive counts)
Counter({'a': 2})
c & d                       # intersection:  min(c[x], d[x]) 
Counter({'a': 1, 'b': 1})
c | d                       # union:  max(c[x], d[x])
Counter({'a': 3, 'b': 2})
'''


from collections import Counter


def main():
    # list of students in class 1
    class1 = ["Bob", "Becky", "Chad", "Darcy", "Frank", "Hannah"
              "Kevin", "James", "James", "Melanie", "Penny", "Steve"]

    # list of students in class 2
    class2 = ["Bill", "Barry", "Cindy", "Debbie", "Frank",
              "Gabby", "Kelly", "James", "Joe", "Sam", "Tara", "Ziggy"]

    # TODO: Create a Counter for class1 and class2
    c1 = Counter(class1)
    c2 = Counter(class2)

    # TODO: How many students in class 1 named James?
    print(c1['James'])

    # TODO: How many students are in class 1?
    print(sum(c1.values()), 'students in class1')
    print(sum(c2.values()), 'students in class2')

    # TODO: Combine the two classes
    c1.update(class2)
    print(sum(c1.values()), 'student in class1 and class2')

    # TODO: What's the most common name in the two classes?
    s = max(c1, key=lambda x: c1[x]) 
    print(s, ":", c1[s])
    ''' James : 3 '''
    print(c1.most_common(3))
    '''
    [('James', 3), ('Frank', 2), ('Bob', 1)]
    '''
    print(c1.most_common())
    '''
    [('James', 3), ('Frank', 2), ('Bob', 1), ('Becky', 1), 
    ('Chad', 1), ('Darcy', 1), ('HannahKevin', 1), ('Melanie', 1), ('Penny', 1), ('Steve', 1), ('Bill', 1), ('Barry', 1), ('Cindy', 1), ('Debbie', 1), ('Gabby', 1), ('Kelly', 1), ('Joe', 1), ('Sam', 1), ('Tara', 1), ('Ziggy', 1)]
    '''

    # TODO: Separate the classes again
    c1.subtract(c2)
    print(c1.most_common(3))
    '''
    [('James', 2), ('Bob', 1), ('Becky', 1)]
    '''
    # TODO: What's common between the two classes?
    print(c1 & c2)
    '''
    Counter({'Frank': 1, 'James': 1})
    '''

if __name__ == "__main__":
    main()

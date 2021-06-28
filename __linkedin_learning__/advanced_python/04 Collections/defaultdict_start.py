# Demonstrate the usage of defaultdict objects

from collections import defaultdict

def main():
    # define a list of items that we want to count
    fruits = ['apple', 'pear', 'orange', 'banana',
              'apple', 'grape', 'banana', 'banana']

    # use a dictionary to count each element
    # Count the elements in the list
    fruitCounter = {}
    for fruit in fruits:
        if fruit in fruitCounter.keys():
            fruitCounter[fruit] += 1
        else:
            fruitCounter[fruit] = 1

    # use defaultdict
    fruitCounter2 = defaultdict(int)   # int is the factory
    for fruit in fruits:
        fruitCounter2[fruit] += 1

    # print the result
    for (k, v) in fruitCounter.items():
        print(k + ": " + str(v))
    print('----------')
    for (k, v) in fruitCounter2.items():
        print(k + ": " + str(v))

    # Use a lambda function for the factory
    fruitCounter3 = defaultdict(lambda: 100)   # starting from 100
    for fruit in fruits:
        fruitCounter3[fruit] += 1
    # print the result
    print('----------')
    for (k, v) in fruitCounter3.items():
        print(k + ": " + str(v))

    # Another example
    s = 'mississippi'
    d = defaultdict(int)
    for k in s:
        d[k] += 1
    print(sorted(d.items())
)

if __name__ == "__main__":
    main()

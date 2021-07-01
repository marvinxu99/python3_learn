# Demonstrate how to use list comprehensions


def main():
    # define two lists of numbers
    evens = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]
    odds = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]

    # TODO: Perform a mapping and filter function on a list
    evenSquared = list(map(lambda e: e**2, filter(lambda x: x>4 and x<16, evens)))
    print(evenSquared)

    # TODO: Derive a new list of numbers frm a given list
    # evenSquared2 = [e**2 for e in evens]
    evenSquared2 = [e**2 for e in evens if e > 4 and e < 16]
    print(evenSquared2)

    # TODO: Limit the items operated on with a predicate condition
    oddSquared = [o ** 2 for o in odds if o > 3 and o < 17]
    print(oddSquared)

if __name__ == "__main__":
    main()

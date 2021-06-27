# advanced iteration functions in the itertools package
import itertools

def testFunction(x):
    return x < 40


def main():
    # TODO: cycle iterator can be used to cycle over a collection
    seq1 = ["Joe", "John", "Mike"]
    cycle1 = itertools.cycle(seq1)
    print(next(cycle1))
    print(next(cycle1))
    print(next(cycle1))
    print(next(cycle1))

    # TODO: use count to create a simple counter
    count1 = itertools.count(100, 10)
    print(next(count1))
    print(next(count1))
    print(next(count1))
    print(next(count1))

    # TODO: accumulate creates an iterator that accumulates values
    vals = [10,20,30,40,50,40,30]
    acc = itertools.accumulate(vals)
    print(list(acc))
    acc2 = itertools.accumulate(vals, max)
    print(list(acc2))

    # TODO: use chain to connect sequences together
    x = itertools.chain('ABCD', '1234')
    print(list(x))

    # TODO: dropwhile and takewhile will return values until
    # a certain condition is met that stops them
    # 
    print("dropwhile() and takewhile()...")
    # itertools.dropwhile(predicate, iterable) - Make an iterator 
    # that drops elements from the iterable as long as the 
    # predicate is true; afterwards, returns every element
    print(list(itertools.dropwhile(testFunction, vals)))
    
    # takewhile(predicate, iterable)
    # returns elements from the iterable as long as the predicate is true
    print(list(itertools.takewhile(testFunction, vals)))

       
if __name__ == "__main__":
    main()
    
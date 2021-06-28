# customize string representations of objects
'''
object.__str()__
object.__repr()__
object.__format()__
object.__bytes()__
'''

class Person():
    def __init__(self):
        self.fname = "Joe"
        self.lname = "Marini"
        self.age = 25

    # TODO: use __repr__ to create a string useful for debugging
    def __repr__(self) -> str:
        pass

    # TODO: use str for a more human-readable string
    def __str__(self) -> str:
        pass


def main():
    # create a new Person object
    cls1 = Person()

    # use different Python functions to convert it to a string
    print(repr(cls1))
    print(str(cls1))
    print("Formatted: {0}".format(cls1))


if __name__ == "__main__":
    main()

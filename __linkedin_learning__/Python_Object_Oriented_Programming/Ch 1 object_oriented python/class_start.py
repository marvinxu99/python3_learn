# Python Object Oriented Programming by Joe Marini course example
# Using class-level and static methods


class Book:
    # TODO: Properties defined at the class level are shared by all instances and the class itself
    BOOK_TYPES = ("HARDCOVER", "PAPERBACK", "EBOOK")

    # TODO: double-underscore properties are hidden from other classes
    __booklist = None

    # TODO: create a class method
    # Class methods take a cls parameter that points to the class
    @classmethod
    def getbooktypes(cls):
        return cls.BOOK_TYPES

    # TODO: create a static method
    # Static method takes neither a self nor a cls parameter 
    # Therefore a static method can neither modify object state nor class 
    # state. Static methods are restricted in what data they can 
    # access - and they’re primarily a way to namespace your methods.
    # use case: 
    #   when you want to make a class callable and not have its state modified
    @staticmethod
    def getbooklist():
        if Book.__booklist == None:
            Book.__booklist = []
        return Book.__booklist

    # instance methods receive a specific object instance (self) as an argument
    # and operate on data specific to that object instance
    def setTitle(self, newtitle):
        self.title = newtitle

    def __init__(self, title, booktype):
        self.title = title
        if booktype not in self.BOOK_TYPES:
            raise ValueError(f"{booktype} is not a valid book type")
        else:
            self.booktype = booktype


# TODO: access the class attribute
print("Book types:", Book.getbooktypes())

# TODO: Create some book instances
b1 = Book("Brave New World", "HARDCOVER")
b2 = Book("War and Peace", "EBOOK")

print(b2.BOOK_TYPES)

# TODO: Use the static method to access a singleton object
thebooks = Book.getbooklist()
thebooks.append(b1)
thebooks.append(b2)
print(thebooks)

# Python Object Oriented Programming by Joe Marini course example
# Using instance methods and attributes


class Book:
    # the "init" function is called when the instance is
    # created and ready to be initialized
    def __init__(self, title, author, pages, price):
        self.title = title
        # TODO: add properties
        self.author = author
        self.pages = pages
        self.price = price
        self.__secret = "this is a secret attibute"

    # TODO: create instance methods
    def getprice(self):
        if hasattr(self, "_discount") and self._discount:
            return self.price * (1 - self._discount)
        else:
            return self.price

    def set_discount(self, amount):
        self._discount = amount


# TODO: create some book instances
b1 = Book("War and Peace", "Leo Tolstoy", 1225, 39.95)
b2 = Book("The Catcher in the Rye", "JD Salinger", 234, 29.95)

# TODO: print the price of book1
print(b1.getprice())


# TODO: try setting the discount
b2.set_discount(0.25)
print(b2.getprice())

# TODO: properties with double underscores are hidden by the interpreter
# It is often used to prevent subclass from overriding the attribute
# print(b2.__secret)
print(b2._Book__secret)  # this will still print

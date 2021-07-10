# Python Object Oriented Programming by Joe Marini course example
# Using the postinit function in data classes

from dataclasses import dataclass, field


@dataclass
class C:
    a: float
    b: float
    c: float = field(init=False)

    def __post_init__(self):
        self.c = self.a + self.b


@dataclass
class Book:
    title: str
    author: str
    pages: int
    price: float

    # TODO: the __post_init__ function lets us customize additional properties
    # after the object has been initialized via built-in __init__
    """
    The generated __init__() code will call a method named __post_init__(), 
    if __post_init__() is defined on the class. It will normally be called 
    as self.__post_init__(). However, if any InitVar fields are defined, they 
    will also be passed to __post_init__() in the order they were defined 
    in the class. If no __init__() method is generated, 
    then __post_init__() will not automatically be called.
    """
    def __post_init__(self):
        self.description = f"{self.title} by {self.author}, {self.pages} pages "


if __name__ == "__main__":
    # create some instances
    b1 = Book("War and Peace", "Leo Tolstoy", 1225, 39.95)
    b2 = Book("The Catcher in the Rye", "JD Salinger", 234, 29.95)
    b3 = Book("War and Peace", "Leo Tolstoy", 1225, 39.95)

    print(b3.description)
    print(dir(b3))
    print(b3)

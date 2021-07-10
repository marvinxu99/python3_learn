# Python Object Oriented Programming by Joe Marini course example
# Using composition to build complex objects


class Book:
    def __init__(self, title, price, author):
        self.title = title
        self.price = price

        self.author = author

        self.chapters = []

    def addchapter(self, chapter):
        self.chapters.append((chapter))

    def getbookpagecount(self):
        # result = 0
        # for ch in self.chapters:
        #     result += ch.pagecount
        # return result
        return sum([ch.pagecount for ch in self.chapters])

class Author:
    def __init__(self, fname, lname) -> None:
        self.fname = fname
        self.lname = lname

    def __str__(self):
        return f"{self.fname} {self.lname}"

class Chapter:
    def __init__(self, name, pagecount) -> None:
        self.name = name
        self.pagecount = pagecount

    def __str__(self):
        return f"{self.name} {self.pagecount}"


b1 = Book("War and Peace", 39.0, Author("Leo", "Tolstoy"))

b1.addchapter(Chapter("Chapter 1", 125))
b1.addchapter(Chapter("Chapter 2", 97))
b1.addchapter(Chapter("Chapter 3", 143))

print(b1.title)
print(b1.getbookpagecount())
print(b1.author)

b2 = Book("Midnight Rose", 25.0, Author("Wesley", "Winter"))
print(b2.getbookpagecount())

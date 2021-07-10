# Python Object Oriented Programming by Joe Marini course example
# Understanding multiple inheritance

"""
MRO - Method Resolution Order
MRO is a concept used in inheritance. It is the order in which a method 
is searched for in a classes hierarchy and is especially useful in Python
 because Python supports multiple inheritance. In Python, the MRO is 
 from bottom to top and left to right.
"""

class A:
    def __init__(self):
        super().__init__()
        self.foo = "foo"
        self.name = "Class A"


class B:
    def __init__(self):
        super().__init__()
        self.bar = "bar"
        self.name = "Class B"


class C(A, B):
    def __init__(self):
        super().__init__()

    def showprops(self):
        print(self.foo)
        print(self.bar)
        print(self.name)

c = C()
c.showprops()
print(C.__mro__)
print(C.mro())
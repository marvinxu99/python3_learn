# the key parameter can be used to sort complex objects
from operator import attrgetter, methodcaller, itemgetter


class Product():
    def __init__(self, name, price, weight, discount):
        self.name = name
        self.price = price
        self.weight = weight
        self.discount = discount

    def __repr__(self):
        return repr((self.name, self.price, self.weight))

    def discountPrice(self):
        return self.price - (self.price * self.discount)


prodList = [
    Product("Widget A", 50, 10, 0.05),
    Product("Widget B", 40, 8, 0.15),
    Product("Widget C", 35, 12, 0.0),
    Product("Widget D", 65, 7, 0.20),
    Product("Widget E", 70, 7, 0.12)
]


# TODO: the operator module functions provide easy ways to select fields
# attrgetter() retrieves a given attribute or property from an object
# itemgetter() retrieves an item at a given index in a collection
# methodcaller() calls the given method on the object
print("Using the attrgetter method:")

# print("Using methodcaller to invoke a method:")

# TODO: Use itemgetter to retrieve an index
inventory = [("Widget A", 5), ("Widget B", 2), ("Widget C", 4),
             ("Widget D", 7), ("Widget E", 4)]

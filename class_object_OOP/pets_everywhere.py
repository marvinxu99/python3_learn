class Pets():
    animals = []

    def __init__(self, animals):
        self.animals = animals

    def walk(self):
        for animal in self.animals:
            print(animal.walk())


class Cat():
    is_lazy = True
    breed = 'unknown'

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def walk(self):
        return f'{self.name} is a {self.breed} cat and is just walking around'


class PersianCat(Cat):
    breed = "Persian"

    def sing(self, sounds):
        return f'{sounds}'


class MaineCoonCat(Cat):
    breed = "MaineCoon"

    def sing(self, sounds):
        return f'{sounds}'

# 1 Add another Cat


class SiameseCat(Cat):
    breed = "Siamese"

    def sing(self, sounds):
        return f'{sounds}'


# 2 Create a list of all of the pets (create 3 cat instances from the above)
my_cats = [PersianCat('Simon', 4), MaineCoonCat(
    'Sally', 10), SiameseCat('Teddy', 3)]

# 3 Instantiate the Pet class with all your cats use variable my_pets
my_pets = Pets(my_cats)

# 4 Output all of the cats walking using the my_pets instance
my_pets.walk()

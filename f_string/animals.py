class Animal:
    def __init__(self, name, species, sound):
        self.name = name
        self.species = species
        self.sound = sound

    def __str__(self):
        return f"<{self.species}: {self.name}>"

    def __format__(self, formatting=None):
        if formatting == "sound":
            return f"I, {self.name}, say: {self.sound}"
        return self.__str__()


if __name__ == "__main__":
    animals = [
        Animal("Doggo", "Dog", "Woof"),
        Animal("Catto", "Cat", "Meow"),
        Animal("Teddy", "Bear", "Roar"),
    ]

    print("Printed using: print(animal)")
    for animal in animals:
        print(animal)
    print()

    print('Printed using: print(f"{animal}")')
    for animal in animals:
        print(f"{animal}")
    print()

    print('Printed using: print(f"{animal:sound}")')
    for animal in animals:
        print(f"{animal:sound}")
    print()
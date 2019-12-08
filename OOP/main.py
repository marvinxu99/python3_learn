# OOP
# There are three types of methods in Python:
#   instance methods, static methods, and class methods.


class PlayerCharacter:

    # Class Attribute
    # it is not dynamic, do not change across instances
    membership = True

    def __init__(self, name, age=21):
        self.name = name  # attributes
        self.age = age

    def run(self):
        print(f'{self.name}({self.age}) is running')

    @classmethod
    def adding_things(cls, num1, num2):
        return num1 + num2

    @classmethod
    def adding_things2(cls, num1, num2):
        return cls("Teddy", num1 + num2)

    @staticmethod
    def adding_things3(num1, num2):
        return num1 + num2


player1 = PlayerCharacter("marvin", 49)
player2 = PlayerCharacter("Eric", 19)
player3 = PlayerCharacter.adding_things2(2, 3)
player2.attack = 90
player1.name = 'marvin xxx'

player1.run()
player2.run()

print(player1.membership)
print(player2.attack)
print(f"player3 age: {player3.age}")
print(f'static method: {PlayerCharacter.adding_things3(2, 3)}')

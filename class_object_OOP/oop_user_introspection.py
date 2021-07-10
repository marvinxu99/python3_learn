class User:
    def __init__(self, email):
        self.email = email

    def sign_in(self):
        print("logged in")


class Wizard(User):
    def __init__(self, name, power, email=""):
        super().__init__(email)
        self.name = name
        self.power = power

    def attack(self):
        self.power -= 5
        print(f"attacking with power of {self.power}")


class Archer(User):
    def __init__(self, name, num_arrows, email=""):
        super().__init__(email)
        self.name = name
        self.num_arrows = num_arrows

    def attack(self):
        self.num_arrows -= 1
        print(f'attacking with arrows: arrrows left - {self.num_arrows}')


wizard1 = Wizard("Mann", 95, "mann@gmail.com")
archer1 = Archer("Pointy", 35)

# Object introspection
print(dir(wizard1))

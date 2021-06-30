class User:
    def __init__(self, email):
        self.email = email

    def sign_in(self):
        print("logged in")


class Wizard(User):
    def __init__(self, name, power=60, email=""):
        super().__init__(email)
        self.name = name
        self.power = power

    def attack(self):
        self.power -= 5
        print(f"attacking with power of {self.power}")


class Archer(User):
    def __init__(self, name, num_arrows=50, email=""):
        super().__init__(email)
        self.name = name
        self.num_arrows = num_arrows

    def attack(self):
        self.num_arrows -= 1
        print(f'attacking with arrows: arrrows left - {self.num_arrows}')

    def run(self):
        print('run really fast')

class HybridBorg(Wizard, Archer):
    def __init__(self, name, power, arrows):
        Wizard.__init__(self, name, power)
        Archer.__init__(self, name, arrows)


wizard1 = Wizard("Mann", 95, "mann@gmail.com")
archer1 = Archer("Pointy", 35)

hb1 = HybridBorg("Hybrid1", 89, 35)
print(hb1.run())

#MRO - Method Resolution Order
print(HybridBorg.mro())
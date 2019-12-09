class Toy():
    def __init__(self, color, age):
        self.color = color
        self.age = age
        self.my_dict = {
            "name": "Yoyo",
            "has_pets": False
        }

    # def __getattribute__(self):
    #     return()

    def __str__(self):
        return self.color

    def __len(self):
        return 1000


action_figure = Toy('red', 0)
print(action_figure.__getattribute__("my_dict"))
print(action_figure)   # __str__()

# Python Object Oriented Programming by Joe Marini course example
# Creating immutable data classes

from dataclasses import dataclass


# @dataclass()  # TODO: "The "frozen" parameter makes the class immutable
@dataclass(frozen=True)  # TODO: "The "frozen" parameter makes the class immutable
class ImmutableClass:
    value1: str = "Value 1"
    value2: int = 0

    def some_func(self, newvalue):
        self.value1 = newvalue


obj = ImmutableClass()
print(obj.value1)

# TODO: attempting to change the value of an immutable class throws an exception
# obj.value1 = "ANother value"

# TODO: even functions within the class can't change anything
obj.some_func("another value")
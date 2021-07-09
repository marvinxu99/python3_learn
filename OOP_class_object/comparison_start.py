# Use special methods to compare objects to each other
"""
object.__gt__(self, other)     # self > other
object.__gE__(self, other)     # self >= other
object.__lt__(self, other)     # self < other
object.__le__(self, other)     # self <= other
object.__eq__(self, other)     # self == other
object.__ne__(self, other)     # self != other

"""

class Employee():
    def __init__(self, fname, lname, level, yrsService):
        self.fname = fname
        self.lname = lname
        self.level = level
        self.seniority = yrsService

    # TODO: implement comparison functions by emp level
    def __ge__(self, other):
        if self.level == other.level:
            return self.seniority >= other.seniority
        else:
            return self.level >= other.level

    def __gt__(self, other):
        if self.level == other.level:
            return self.seniority > other.seniority
        else:
            return self.level > other.level

    def __lt__(self, other):
        if self.level == other.level:
            return self.seniority < other.seniority
        else:
            return self.level < other.level

    def __le__(self, other):
        if self.level == other.level:
            return self.seniority <= other.seniority
        else:
            return self.level <= other.level

    def __eq__(self, other):
        if self.level == other.level:
            return self.seniority == other.seniority
        else:
            return self.level == other.level

    def __str__(self) -> str:
        return F'{self.fname}:{self.lname}:{self.level}:{self.seniority}'



def main():
    # define some employees
    dept = []
    dept.append(Employee("Tim", "Sims", 5, 9))
    dept.append(Employee("John", "Doe", 4, 12))
    dept.append(Employee("Jane", "Smith", 6, 6))
    dept.append(Employee("Rebecca", "Robinson", 5, 13))
    dept.append(Employee("Tyler", "Durden", 5, 12))

    # TODO: Who's more senior?
    print(dept[0] > dept[2])
    print(dept[4] < dept[3])

    # TODO: sort the items
    dept_sorted = sorted(dept)
    for emp in dept_sorted:
        print(emp)


if __name__ == "__main__":
    main()

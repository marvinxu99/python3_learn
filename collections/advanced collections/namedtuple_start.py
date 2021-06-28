# Demonstrate the usage of namdtuple objects

import collections


def main():
    # TODO: create a Point namedtuple
    Point = collections.namedtuple('Point', 'x y')
    print(type(Point))
    p1 = Point(10, 20)
    p2 = Point(30, 40)
    print(p1, p2)
    print(p1.x, p1.y)

    # TODO: use _replace to create a new instance
    print(id(p1))
    p1 = p1._replace(x=100)
    print(id(p1))
    print(p1)


if __name__ == "__main__":
    main()

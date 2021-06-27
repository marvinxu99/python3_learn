# use transform functions like sorted, filter, map


def filterFunc(x: int):
    '''
    return True if it is an even number
    '''
    return False if x % 2 == 0 else True


def filterFunc2(x: str):
    return False if x.isupper() else True


def squareFunc(x):
    return x*x


def toGrade(x):
    if x >= 90:
        return 'A'
    elif x >= 80:
        return 'B'
    elif x >= 70:
        return 'C'
    elif x >= 60:
        return 'D'
    else:
        return 'F'


def main():
    # define some sample sequences to operate on
    nums = (1, 8, 4, 5, 13, 26, 381, 410, 58, 47)
    chars = "abcDeFGHiJklmnoP"
    grades = (81, 89, 94, 78, 61, 66, 99, 74)

    # TODO: use filter to remove items from a list
    odds = list(filter(filterFunc, nums))
    print(odds)

    # TODO: use filter on non-numeric sequence
    lowers = list(filter(filterFunc2, chars))
    print(lowers)

    # TODO: use map to create a new sequence of values
    squares = list(map(squareFunc, nums))
    print(squares)

    # TODO: use sorted and map to change numbers to grades
    grades_sorted = sorted(grades, reverse=True)
    letters = list(map(toGrade, grades_sorted))
    print(letters)


if __name__ == "__main__":
    main()

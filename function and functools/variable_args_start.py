# Demonstrate the use of variable argument lists


# TODO: define a function that takes variable arguments
def addition(*args):
    return sum(args)
    # result = 0
    # for arg in args:
    #     result += arg
    # return result


def main():
    # TODO: pass different arguments
    print(addition(1,2,3, 0xb))

    # TODO: pass an existing list
    myNums = [1,2,3,4,5]
    print(addition(*myNums))



if __name__ == "__main__":
    main()

# Demonstrate the use of keyword-only arguments


# use keyword-only arguments to help ensure code clarity
def myFunction(arg1, arg2, *, supressException=False):
    pass


def main():

    # try to call the function without the keyword
    # myFunction(1, 2, True)
    '''
    TypeError: myFunction() takes 2 positional arguments but 3 were given
    '''
    # Must specify the value for the argument
    myFunction(1, 2, supressException=True)


if __name__ == "__main__":
    main()

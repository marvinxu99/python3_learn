# Demonstrate the use of function docstrings


def myFunction(arg1, arg2=None):
    """
    myFunction(arg1, arg2=None) -> not really doing anything, just prints.
    
    Parameters:
    - arg1 - whatevet you are passing
    - arg2 - default is None
    """
    print(arg1, arg2)


def main():
    print(myFunction.__doc__)


if __name__ == "__main__":
    main()

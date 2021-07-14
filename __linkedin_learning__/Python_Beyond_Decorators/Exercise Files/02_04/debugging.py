def make_posh(func):
    '''This is the function decorator'''
    def wrapper():
        '''This is the wrapper function'''
        print("+---------+")
        print("|         |")
        result = func()
        print(result)
        print("|         |")
        print("+=========+")
        return result
    return wrapper

def printfib():
    '''Print out Fibonacci'''
    return ' Fibonacci '


printfib()
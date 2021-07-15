from functools import wraps

def make_posh(func):
    '''This is the function decorator'''
    @wraps(func)
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

@make_posh
def printfib():
    '''Print out Fibonacci'''
    return ' Fibonacci '


printfib()
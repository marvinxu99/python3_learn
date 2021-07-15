from functools import wraps

def bold(func):
    """Add <b>text</b>"""
    @wraps(func)
    def wrapper():
        """return html bold tag"""
        result = "<b>" + func() + "</b>"
        return result
    return wrapper

def italics(func):
    """Add <i>text</i>"""
    @wraps(func)
    def wrapper():
        result = "<i>" + func() + "</i>"
        return result
    return wrapper

@bold
@italics
def printfib():
    '''return Fibonacci'''
    return 'Fibonacci'


if __name__ == "__main__":
    print(printfib())
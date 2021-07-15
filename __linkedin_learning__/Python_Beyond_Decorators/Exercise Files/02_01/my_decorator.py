def my_decorator(func):
    """Decorator function"""
    def wrapper():
        """Retunr string F-I-B-O-N-A-C-C-I"""
        return "F-I-B-O-N-A-C-C-I"
    return wrapper

@my_decorator
def pfib():
    '''Print out Fibonacci'''
    return 'Fibonacci'

print(pfib())
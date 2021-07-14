def make_posh(func):
    def wrapper():
        pass
 
@make_posh
def pfib():
    '''Print out Fibonacci'''
    return ' Fibonacci '

pfib()
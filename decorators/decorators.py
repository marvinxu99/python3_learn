# Decorator Pattern
def my_decorator(func):
    def wrap_func(*args, **kwargs):
        print('********************')
        func(*args, **kwargs)
        print('********************')

    return wrap_func


@my_decorator
def speak(words):
    print(words)


@my_decorator
def bye():
    print('bye bye, so long.')


speak("nice to meeting you")
bye()


####################################
def hello():
    print('helloooooo')


greet = hello
del hello
greet()

# function is first class citizen in the Python world


def execute_func(func):
    func()


def some_func():
    print('still here!')


execute_func(some_func)


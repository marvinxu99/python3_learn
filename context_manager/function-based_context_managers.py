# https://realpython.com/python-with-statement/

'''
Python’s generator functions and the contextlib.contextmanager decorator provide
an alternative and convenient way to implement the context management protocol. 
If you decorate an appropriately coded generator function with @contextmanager, 
then you get a function-based context manager that automatically provides both 
required methods, .__enter__() and .__exit__(). This can make your life more 
pleasant by saving you some boilerplate code.

The general pattern to create a context manager using @contextmanager along with a 
generator function goes like this:

>>> from contextlib import contextmanager

>>> @contextmanager
... def hello_context_manager():
...     print("Entering the context...")
...     yield "Hello, World!"
...     print("Leaving the context...")
...

>>> with hello_context_manager() as hello:
...     print(hello)
...
Entering the context...
Hello, World!
Leaving the context...

In this example, you can identify two visible sections in hello_context_manager(). 
Before the yield statement, you have the setup section. There, you can place the 
code that acquires the managed resources. Everything before the yield runs when 
the flow of execution enters the context.

After the yield statement, you have the teardown section, in which you can release 
the resources and do the cleanup. The code after yield runs at the end of the 
with block. The yield statement itself provides the object that will be assigned to 
the with target variable.

This implementation and the one that uses the context management protocol are 
practically equivalent. Depending on which one you find more readable, you might 
prefer one over the other. A downside of the function-based implementation is 
that it requires an understanding of advanced Python topics, such as decorators and generators.

The @contextmanager decorator reduces the boilerplate required to create a context manager. 
Instead of writing a whole class with .__enter__() and .__exit__() methods, 
you just need to implement a generator function with a single yield that produces 
whatever you want .__enter__() to return.
'''

# Opening Files for Writing: Second Version
from contextlib import contextmanager

@contextmanager
def writable_file(file_path):
    file = open(file_path, mode="w")
    try:
        yield file
    finally:
        file.close()

'''
In this case, writable_file() is a generator function that opens file for writing. 
Then it temporarily suspends its own execution and yields the resource so with 
can bind it to its target variable. When the flow of execution leaves the with 
code block, the function continues to execute and closes file correctly.
'''

if __name__ == "__main__":
    with writable_file("hello.txt") as file:
        file.write("Hello, World!!!")
    
    print("done")
    

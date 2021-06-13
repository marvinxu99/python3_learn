'''
Redirecting the Standard Output
A subtle detail to consider when you’re writing your own context managers is that 
sometimes you don’t have a useful object to return from .__enter__() and therefore 
to assign to the with target variable. In those cases, you can return None explicitly 
or you can just rely on Python’s implicit return value, which is None as well.

For example, say you need to temporarily redirect the standard output, sys.stdout, 
to a given file on your disk. To do this, you can create a context manager like this:

'''

# redirect.py

import sys

class RedirectedStdout:
    def __init__(self, new_output):
        self.new_output = new_output

    def __enter__(self):
        self.saved_output = sys.stdout
        sys.stdout = self.new_output

    def __exit__(self, exc_type, exc_val, exc_tb):
        sys.stdout = self.saved_output

'''
This context manager takes a file object through its constructor. In .__enter__(), 
you reassign the standard output, sys.stdout, to an instance attribute to avoid losing 
the reference to it. Then you reassign the standard output to point to the file on 
your disk. In .__exit__(), you just restore the standard output to its original value.

To use RedirectedStdout, you can do something like this:

>>> from redirectedstdout import RedirectedStdout
>>> with open("hello.txt", "w") as file:
...     with RedirectedStdout(file):
...         print("Hello, World!")
...     print("Back to the standard output...")
...
Back to the standard output...

The outer with statement in this example provides the file object that 
you’re going to use as your new output, hello.txt. The inner with temporarily 
redirects the standard output to hello.txt, so the first call to print() writes 
directly to that file instead of printing "Hello, World!" on your screen. 
Note that when you leave the inner with code block, the standard output 
goes back to its original value.

RedirectedStdout is a quick example of a context manager that doesn’t have a 
useful value to return from .__enter__(). However, if you’re only redirecting the 
print() output, you can get the same functionality without the need for coding a 
context manager. You just need to provide a file argument to print() like this:

>>> with open("hello.txt", "w") as file:
...     print("Hello, World!", file=file)
...

In this examples, print() takes your hello.txt file as an argument. This causes print() 
to write directly into the physical file on your disk instead of printing "Hello, World!" to your screen.

'''

class Indenter:
    def __init__(self):
        self.level = -1

    def __enter__(self):
        self.level += 1
        return self

    def __exit__(self, exc_type, exc_value, exc_tb):
        self.level -= 1

    def print(self, text):
        print("    " * self.level + text)

'''
Here, .__enter__() increments .level by 1 every time the flow of execution enters the context. 
The method also returns the current instance, self. In .__exit__(), you decrease .level so the 
printed text steps back one indentation level every time you exit the context.

The key point in this example is that returning self from .__enter__() allows you to reuse the 
same context manager across several nested with statements. This changes the text indentation 
level every time you enter and leave a given context.
'''

if __name__ == "__main__":
    with Indenter() as indent:
        indent.print("hi!")
        with indent:
            indent.print("hello")
            with indent:
                indent.print("bonjour")
        indent.print("hey")
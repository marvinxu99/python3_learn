# https://realpython.com/python-with-statement/

# with expression as target_var:
#    do_something(target_var)


with open("input.txt") as in_file, open("output.txt", "w") as out_file:
    # Read content from input.txt
    # Transform the content
    # Write the transformed content to output.txt
    pass

/* Pyhtonic way of file handling */
'''
Path is a class that represents concrete paths to physical files in your computer. 
Calling .open() on a Path object that points to a physical file opens it just like 
open() would do. So, Path.open() works similarly to open(), but the file path is 
automatically provided by the Path object you call the method on.

Since pathlib provides an elegant, straightforward, and Pythonic way to manipulate 
file system paths, you should consider using Path.open() in your with statements 
as a best practice in Python.

'''
import pathlib
import logging

file_path = pathlib.Path("hello.txt")

try:
    with file_path.open(mode="w") as file:
        file.write("Hello, World!")

except OSError as error:
    logging.error("Writing to file %s failed due to: %s", file_path, error)
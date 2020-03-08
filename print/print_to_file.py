'''
Printing to a File:

Believe it or not, print() doesn’t know how to turn messages into text on your 
screen, and frankly it doesn’t need to. That’s a job for lower-level layers of 
code, which understand bytes and know how to push them around.

print() is an abstraction over these layers, providing a convenient interface that 
merely delegates the actual printing to a stream or file-like object. A stream can 
be any file on your disk, a network socket, or perhaps an in-memory buffer.

In addition to this, there are three standard streams provided by the operating system:
stdin: standard input
stdout: standard output
stderr: standard error
'''
import sys

print(sys.stdin)
print(sys.stdin.fileno())

print(sys.stdout)
print(sys.stdout.fileno())

print(sys.stderr)
print(sys.stderr.fileno())

# writing to a file.
with open('file.txt', mode='w') as file_object:
    print('hello world', file=file_object)
	
# If working with binary, use the .write()
with open('file.dat', 'wb') as file_object:
    file_object.write(bytes(4))
    file_object.write(b'\xff')
	
'''
If you wanted to write raw bytes on the standard output, then 
this will fail too because sys.stdout is a character stream:
'''	
# the following will fail...
sys.stdout.write(bytes(4))

# encoding UTF-8
with open('file.txt', mode='w', encoding='iso-8859-1') as file_object:
    print('über naïve café', file=file_object)
	
# Instead of a real file existing somewhere in your file system, you can 
# provide a fake one, which would reside in your computer’s memory.
import io
fake_file = io.StringIO()
print('hello word', fake_file)
print(fake_file.getvalue())
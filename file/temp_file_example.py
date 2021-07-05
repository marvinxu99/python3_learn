# Tempfile module
import tempfile

# Create a temporary file
tempFile = tempfile.TemporaryFile()

# Write to a temporary file
tempFile.write(b"Save this special bumber for me:5678309")
tempFile.seek(0)

# Read the temporary file
print(tempFile.read().decode('utf-8'))

tempFile.close()

"""
Using context manager
"""
with tempfile.TemporaryFile() as fp:
    fp.write(b'Hello world!')
    fp.seek(0)
    print(fp.read().decode('utf-8'))


"""
create a temporary directory using the context manager
"""
with tempfile.TemporaryDirectory() as tmpdirname:
    print('created temporary directory', tmpdirname)
# directory and contents have been removed
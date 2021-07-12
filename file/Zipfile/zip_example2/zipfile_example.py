# Working with ZIP files in Python
import zipfile


# TODO: Create a new ZIP archive
# zfile = zipfile.ZipFile("archive.zip", 'w')
# with zipfile.ZipFile("archive.zip", 'w') as zfile:
#     zfile.write('file1.txt')
#     zfile.write('file2.txt')
#     zfile.write('file3.txt')


# TODO: Check validity of the file
print(zipfile.is_zipfile("archive.zip"))

# TODO: Read the properties of a ZIP archive
zfile = zipfile.ZipFile("archive.zip")
print(zfile.namelist())
print(zfile.infolist())

# TODO: Read the properties of ZIP contents
zinfo = zfile.getinfo("file1.txt")
print(zinfo.file_size)
print(zfile.read("file3.txt"))

# TODO: Extract ZIP file contents
# zfile.extract("file2.txt")
# zfile.extractall()

# TODO: Ensure that the file is closed
zfile.close()
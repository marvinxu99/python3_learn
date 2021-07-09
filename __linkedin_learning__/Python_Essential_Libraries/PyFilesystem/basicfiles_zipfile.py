# Python Essential Libraries by Joe Marini course example
# Example file for using PyFilesystem

# import the PyFilesystem library
from fs.osfs import OSFS
from fs.zipfs import ZipFS

# TODO: open a local filesystem for the current directory
# with OSFS(".") as myfs:
#     if not myfs.exists("testdir"):
#         myfs.makedir("testdir")

#     with myfs.open("testdir/samplefile.txt", mode='w') as f:
#         f.write("this is some test")

#     with myfs.open("testdir/samplefile.txt") as f:
#         content = f.read()
#         print(content)

#     info = myfs.getinfo("testdir/samplefile.txt", namespaces=['details'])
#     print(info.name, info.is_dir, info.size, info.type, info.modified)


'''Below uses standard library'''
# import os
# if not os.path.exists('testdir2'):
#     os.makedirs('testdir2')

# with open('testdir2/smaplefile2.txt', mode='w') as f:
#     f.write("this is some text2")

# with open('testdir2/smaplefile2.txt') as f:
#     print(f.read())


# TODO: try opening and reading a ZIP archive
with ZipFS("FileExamples.zip") as thezip:
    if thezip.exists("FileExamples/File1.txt"):
        with thezip.open("FileExamples/File1.txt") as f:
            print(f.read())


'''
    Using standard lib as below:
'''
import os
import zipfile

print("-------------------")
with zipfile.ZipFile('FileExamples.zip') as z:
    # for filename in z.namelist():
    #     if not os.path.isdir(filename):
    #         # read the file
    #         with z.open(filename) as f:
    #             for line in f:
    #                 print(line)
    with z.open("FileExamples/File1.txt") as f:
        print(f.read().decode('utf-8'))
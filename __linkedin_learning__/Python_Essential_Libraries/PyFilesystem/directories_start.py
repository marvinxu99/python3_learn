# Python Essential Libraries by Joe Marini course example
# Example file for using PyFilesystem directory functions
from fs.osfs import OSFS

# TODO: print a directory tree listing
# with OSFS(".") as myfs:
#     myfs.tree()

# TODO: use directory operation functions
with OSFS(".") as myfs:
    dirlist = myfs.listdir("FileExamples")
    print(dirlist)

    # ['Dir1', 'Dir2', 'File1.txt', 'File2.txt', 'File3.txt']

    dirlist = list(myfs.scandir("FileExamples"))
    print(dirlist)
    # [<dir 'Dir1'>, <dir 'Dir2'>, <file 'File1.txt'>, <file 'File2.txt'>, <file 'File3.txt'>]

    dirlist = list(myfs.filterdir("FileExamples", files=["*.txt"]))
    print(dirlist)

# TODO: Use resource info with scandir
with OSFS(".") as myfs:
    dirlist = myfs.scandir("FileExamples", namespaces=['details'])
    for info in dirlist:
        print(info.name, info.size)
"""
Dir1 0
Dir2 0
File1.txt 434
File2.txt 190
File3.txt 481
"""

# TODO: make a copy of a directory
# with OSFS(".") as myfs:
#     myfs.copydir("FileExamples", "CopyOfFileExamples", create=True)

# TODO: remove a directory
with OSFS(".") as myfs:
    if myfs.exists("CopyOfFileExamples"):
        # myfs.removedir("CopyOfFileExamples", )  # gives an error if dir is not empty
        myfs.removetree("CopyOfFileExamples", )

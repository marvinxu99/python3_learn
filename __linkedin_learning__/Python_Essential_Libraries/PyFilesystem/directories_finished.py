# Python Essential Libraries by Joe Marini course example
# Example file for using PyFilesystem directory functions
from fs.osfs import OSFS

# TODO: print a directory tree listing
with OSFS(".") as myfs:
    myfs.tree()

# TODO: use directory operation functions
# with OSFS(".") as myfs:
#     dirlist = myfs.listdir("FileExamples")
#     print(dirlist)

# with OSFS(".") as myfs:
#     dirlist = list(myfs.scandir("FileExamples"))
#     print(dirlist)

# with OSFS(".") as myfs:
#     dirlist = list(myfs.filterdir("FileExamples", files=["*.txt"]))
#     print(dirlist)

# TODO: Use resource info with scandir
# with OSFS(".") as myfs:
#     dirlist = myfs.scandir("FileExamples", namespaces=["details"])
#     for info in dirlist:
#         print(info.name, info.size)

# TODO: make a copy of a directory
# with OSFS(".") as myfs:
#     myfs.copydir("FileExamples", "CopyOfFileExamples", create=True)

# TODO: remove a directory
# with OSFS(".") as myfs:
#     if (myfs.exists("CopyOfFileExamples")):
#         # myfs.removedir("CopyOfFileExamples")
#         myfs.removetree("CopyOfFileExamples")

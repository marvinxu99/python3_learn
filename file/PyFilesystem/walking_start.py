# Python Essential Libraries by Joe Marini course example
# Example file for using the File System walker

from fs.osfs import OSFS
from fs.zipfs import ZipFS

# create a basic file walker
with OSFS(".") as myfs:
    print("-- Files --")
    # TODO: use the files walker to process files
    # for path in myfs.walk.files():
    for path in myfs.walk.files(filter=["*.txt"]):
        print(path)

    print("-- Directories --")
    # TODO: use the dirs walker for directories
    for path in myfs.walk.dirs():
        print(path)

# TODO: use the info property to step through items
print("-- info --")
with OSFS(".") as myfs:
    for path, info in myfs.walk.info(namespaces=['details']):
        print(path, info.is_dir, info.size)
    
# Calculat total file size
with OSFS("FileExamples") as myfs:
    total_size = 0
    for path, info in myfs.walk.info(namespaces=['details']):
        if path.endswith(".txt") and not info.is_dir:
            total_size += info.size
    
    print("total size:", total_size)


# TODO: Use the walk object by itself:
print("-- steps --")
# with OSFS(".") as myfs:
with OSFS("FileExamples") as myfs:
    for step in myfs.walk():
        print(step.path)
        print(step.files)
        print(step.dirs)

# TODO: Use the walker with a ZIP
print("-- Zip steps --")
with ZipFS("FileExamples.zip") as zipfs:
    for step in zipfs.walk():
        print(step.path)
        print(step.files)
        print(step.dirs)



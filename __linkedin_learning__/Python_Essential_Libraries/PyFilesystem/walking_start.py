# Python Essential Libraries by Joe Marini course example
# Example file for using the File System walker

from fs.osfs import OSFS
from fs.zipfs import ZipFS

# create a basic file walker
with OSFS(".") as myfs:
    print("-- Files --")
    # TODO: use the files walker to process files

    print("-- Directories --")
    # TODO: use the dirs walker for directories

# TODO: use the info property to step through items

# TODO: Use the walk object by itself:

# TODO: Use the walker with a ZIP

# Solution to programming challenge for Python Essential Libraries course by Joe Marini

from fs.osfs import OSFS

# Challenge - figure out the total size of all text files in a folder structure
totalsize = 0

# Create a file walker to walk the FileExamples directory
with OSFS(".") as myfs:
    # We need to specify the details namespace to get size info
    for path, info in myfs.walk.info(namespaces=["details"]):
        # Check for an ending extension of .txt
        if path.endswith(".txt") and not info.is_dir:
            totalsize += info.size

    # print the final results
    print("Total size of files is: {0}".format(totalsize))

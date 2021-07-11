# Find paths to files with identical contents.

"""
Method #1 Using PyFilesystem (pip install fs)
"""
from collections import defaultdict
from hashlib import md5
from fs import open_fs

file_hashes = defaultdict(list)
with open_fs('.') as fs:
    for path in fs.walk.files():
        file_hash = md5(fs.readbytes(path)).hexdigest()
        file_hashes[file_hash].append(path)

for paths in file_hashes.values():
    if len(paths) > 1:
        print("Duplicate files found:")
        print(*paths, sep='\n')
else:
    print("No duplicate found.")

"""
Method #2 using pathlib
https://github.com/PyFilesystem/pyfilesystem2/blob/master/examples/find_dups.py
"""
# from collections import defaultdict
# from hashlib import md5
from pathlib import Path


def find_files(filepath):
    for path in Path(filepath).rglob('*'):
        if path.is_file():
            yield path


file_hashes = defaultdict(list)

for path in find_files(Path.cwd()):
    file_hash = md5(path.read_bytes()).hexdigest()
    file_hashes[file_hash].append(path)

for paths in file_hashes.values():
    if len(paths) > 1:
        print("Duplicate files found:")
        print(*paths, sep='\n')
else:
    print("no dups found.")
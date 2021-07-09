from fs import open_fs


"""
Method #1
"""
extension = '.py'
with open_fs('.') as fs:
    count = fs.glob(f"**/*{extension}").count().files
print(f"{count} Python files found")

"""
method #2
"""
from fs.osfs import OSFS

with OSFS(".") as myfs:  
    # count = sum( 1 for _ in myfs.walk.files(filter=["*.gif", '*.jpeg', '*.png']):   
    count = sum(1 for _ in myfs.walk.files(filter=['*.py']))
    print(f"{count} files with .py")
        

"""
Method #3
Using pathlib
"""
from pathlib import Path

extension = '.py'
count = 0
count = sum(1 for _ in Path('.').rglob(f'*{extension}'))
print(f"{count} Python files found")
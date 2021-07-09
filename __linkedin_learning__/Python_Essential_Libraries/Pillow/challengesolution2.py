# Example file for Python Essential Libraries course by Joe Marini
# demonstrates simple image operations using the Pillow library

from PIL import Image
from fs.osfs import OSFS
import fs.path

# define a thumbnail size
thumbsize = (128, 128)
num_img = 0

# Remove all the tumbnail files in the folder
with OSFS("ImagesArchive") as myfs:
    # TODO: use the files walker to process files
    for path in myfs.walk.files(filter=["*thumb.*"]):
        myfs.remove(path)

# process each image file
with OSFS("ImagesArchive") as myfs:  
    # TODO: use the files walker to process files
    for path in myfs.walk.files(filter=["*.gif", '*.jpeg', '*.png']):
        filename, ext = fs.path.splitext(path) 
        with Image.open("ImagesArchive/" + path) as imgfile:
            imgfile.thumbnail(thumbsize)
            imgfile.save("ImagesArchive/" + filename + ".thumb" + ext)
        num_img += 1

print(f"{num_img} images processed.")
        

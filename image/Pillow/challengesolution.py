# Example file for Python Essential Libraries course by Joe Marini
# demonstrates simple image operations using the Pillow library

from PIL import Image
import glob
import os

# define a thumbnail size
thumbsize = (128, 128)
num_img = 0

images = glob.glob("ImagesArchive/*.*")
for image in images:
    if image.endswith(".jpeg") or image.endswith(".png") or image.endswith(".gif"):
        fn = os.path.basename(image)
        filename, ext = os.path.splitext(fn)
        with Image.open(image) as imgfile:
            imgfile.thumbnail(thumbsize)
            imgfile.save("ImagesArchive/" + filename + ".thumb" + ext)
        num_img += 1
print(f"{num_img} images processed.")
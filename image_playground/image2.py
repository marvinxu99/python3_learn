from PIL import Image

img = Image.open('./ww_logo.png')
print(img)
print(img.format)
print(img.size)
print(img.mode)
print(img.getcolors())


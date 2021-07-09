from PIL import Image, ImageFilter

img = Image.open('./Pokedex/pikachu.jpg')
print(img)
# print(img.format)
# print(img.size)
# print(img.mode)

print(dir(img))

filtered_img = img.filter(ImageFilter.BLUR)
filtered_img.save('blur.png', 'png')

filtered_img = img.filter(ImageFilter.SMOOTH)
filtered_img.save('smooth.png', 'png')

filtered_img = img.filter(ImageFilter.SHARPEN)
filtered_img.save('sharpened.png', 'png')

filtered_img = img.convert('L')
filtered_img.save('greyed.png', 'png')

# filtered_img.show()

crooked = filtered_img.rotate(45)
crooked.save('crooked.png', 'png')

resized = filtered_img.resize((300, 300))
resized.save('resized.png', 'png')

img2 = Image.open('./resized.png')
print(img2)
# print(img2.format)
# print(img2.size)
# print(img2.mode)

box = (100, 100, 400, 400)
region = filtered_img.crop(box)
region.save('cropped.png', 'png')

img3 = Image.open('./astro.jpg')
print(img3)
# thumbnail = img3.resize((400, 400))
# thumbnail.save('thumbnail.png', 'png')
img3.thumbnail((400, 400))  # thumbnail will keep the aspect ratio
img3.save('thumbnail2.png', 'png')



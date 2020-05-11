from PIL import Image, ImageFilter

img = Image.open('./winter_winter.png')

filtered_img = img.filter(ImageFilter.SHARPEN)
filtered_img.save('sharpened.png', 'png')

resized = filtered_img.resize((300, 300))
resized.save('resized.png', 'png')

# thumbnail = img3.resize((400, 400))
# thumbnail.save('thumbnail.png', 'png')
img3.thumbnail((400, 400))  # thumbnail will keep the aspect ratio
img3.save('thumbnail2.png', 'png')



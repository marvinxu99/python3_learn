# Example file for Python Essential Libraries course by Joe Marini
# demonstrates image editing using the Pillow library
from PIL import Image, ImageDraw, ImageFont

# TODO: use the ImageDraw routines to modify an image
infile = "ImagesArchive/Coding.png"
# with Image.open(infile) as img:
#     # create a drawing context from the image
#     draw = ImageDraw.Draw(img)

#     # draw two lines on the image
#     draw.line((0, 0) + img.size, width=40, fill=128)
#     draw.line((0, img.size[1], img.size[0], 0), width=40, fill=128)
#     img.show()

# TODO: use the ImageDraw routines to modify an image
infile = "ImagesArchive/BrainHand.jpeg"
# with Image.open(infile) as img:
#     # create a drawing context from the image
#     draw = ImageDraw.Draw(img)

#     # define some drawing parameters - text and font to use
#     textstr = "This is some sample text"
#     # On Mac, use "Arial.ttf" - capitalize the A
#     txtfont = ImageFont.truetype("arial.ttf", size=150)

#     # measure the text size so we can position the string
#     # right along the bottom edge of the image
#     txtsize = draw.textsize(textstr, font=txtfont)
#     # The textsize function returns a tuple:
#     # [0] is the length, [1] is the height of the text
#     location = (20, img.height - txtsize[1])

#     # draw and show the text
#     draw.text(location, textstr, (255, 255, 255), font=txtfont)
#     img.show()

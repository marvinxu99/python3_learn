from colorthief import ColorThief
color_thief = ColorThief('ww_logo.png')
# get the dominant color
dominant_color = color_thief.get_color(quality=1)

print("dominant_color: %x", % dominant_color)
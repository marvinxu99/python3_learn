import sys
import os
from PIL import Image

# Grab the first and second argument
if len(sys.argv) != 3:
    print('not enough arguments')
    exit(1)

jpg_folder = sys.argv[1]
png_folder = sys.argv[2]

if not os.path.exists(jpg_folder) or not os.path.isdir(jpg_folder):
    print("JPG folder is not valid.")
    exit(1)

# Check if new/ exists, if nor create it
if not os.path.exists(png_folder):
    os.makedirs(png_folder)

# Loop through Pokedex
for filename in os.listdir(jpg_folder):
    img = Image.open(f'{jpg_folder}{filename}')
    clean_name = os.path.splitext(filename)[0]
    img.save(f'{png_folder}{clean_name}.png', 'png')

from PIL import Image
import os

for file in os.listdir():

    print(file)
    if file != "main.py":
        picture = Image.open(file)
        picture.save("compressed_"+file, optimize = True, quality = 60)
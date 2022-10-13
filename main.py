from PIL import Image
import os
import shutil

for file in os.listdir("./originals"):
    name, extension = file.split(".")

    if extension in ['jpg', 'jpeg', 'png']:
        picture = Image.open("./originals/" + file)
        picture.save("./compressions/compressed_" + file, optimize = True, quality = 60)

    else:
        shutil.copy("./originals/" + file, "./unable_to_compress/" + file)
from PIL import Image
import os
import shutil
import matplotlib.pyplot as plt
import time

starting_time = time.time()
n_files = 0

for file in os.listdir("./originals"):
    name, extension = file.split(".")

    if extension in ['jpg', 'jpeg', 'png']:
        try:
            picture = Image.open("./originals/" + file)
            picture.save("./compressions/compressed_" + file, optimize = True, quality = 75)
            n_files += 1
        except:
            shutil.copy("./originals/" + file, "./unable_to_compress/" + file)

    else:
        shutil.copy("./originals/" + file, "./unable_to_compress/" + file)

size_originals = 0
size_compressions = 0
size_unable = 0

for file in os.listdir("./originals"):
    size_originals += os.stat("./originals/" + file).st_size

for file in os.listdir("./compressions"):
    size_compressions += os.stat("./compressions/" + file).st_size

for file in os.listdir("./unable_to_compress"):
    size_unable += os.stat("./unable_to_compress/" + file).st_size

before_compression = size_originals / (1024 * 1024)
after_compression = (size_compressions + size_unable) / (1024 * 1024)
reduction = (after_compression - before_compression) / before_compression * 100

print('\n')
print('{} files compressed in {:.2f} seconds'.format(n_files, time.time() - starting_time))
print('\n')
print('Size before compression: {:.2f} MB'.format(before_compression))
print('Size after compression:  {:.2f} MB'.format(after_compression))
print('Compression percentage:  {:.2f} %'.format(reduction))

x = ['Before Compression', 'After Compression']
y = [before_compression, after_compression]

plt.bar(x, y)
plt.title('Sizes before and after compression')

for i, value in enumerate(y):
    plt.text(i, value/2, str(round(value, 2)) + ' MB', fontweight = 'bold')

plt.show()
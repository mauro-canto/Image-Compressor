# Image-Compressor

The following code is devoted to compress images decreasing it size. Only images with extensions ".jpg", ".jpeg" and ".png" will be compressed.

The code consist of 3 folders and a "main.py" python executable:
- originals: This is the folder to place the original files.
- compressions: After the code execution, this folder will contain the compressed images. In addition the images names will start with "compressed_" followed by the original name.
- unable_to_compress: Here all the files which could not be compressed will be placed, either because they do not contain the specific extensions to be compressed or because they suffered an error during the compression process.
- main.py: Python main programm to be executed once all the original files have been placed in their respective folder.

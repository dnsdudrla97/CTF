import zipfile
import os



for i in range(1000, 0, -1):
    print(i)
    zipfile.ZipFile(f'layer{i}.zip').extractall()

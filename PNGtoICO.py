from os import walk
from PIL import Image

for root, dirs, files in walk("."):
    for filename in files:
        if filename.endswith(".png"):
            img = Image.open(filename)
            img.save(filename.rstrip(".png")+".ico")
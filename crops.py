import os
from PIL import Image

for root, dirs, files in os.walk('./'):
    for idx, file in enumerate(files):
        fname, ext = os.path.splitext(file)
        if ext in ['.png']:
            im = Image.open(file)
            width, height = im.size

            crop_image = im.crop((0, 0, width, height-10)) #crop((left, top, right, bottom))
            crop_image.save(im.filename.split('.png')[0] + str(idx) + '.png')

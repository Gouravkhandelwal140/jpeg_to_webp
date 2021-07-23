import os
from PIL import Image
import PIL
import os

for subdir, dirs, files in os.walk(r'C:\Users\S K\Desktop\New folder (14)\New folder',topdown=True):
    for filename in files:

        filepath = subdir + os.sep + filename
        
        if filepath.endswith(".jpg") or filepath.endswith(".png"):

        	image = Image.open(filepath)
        	image = image.convert('RGB')
        	f=filepath
        	f=f.split('.')[0]
        	f=f+'.webp'
        	image.save(f,'webp')
        	os.remove(filepath)
            


# image = Image.open('download.jpg')
# image = image.convert('RGB')
# image.save('download.webp', 'webp')
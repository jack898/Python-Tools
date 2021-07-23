# Usage: compressor.py (file path to image which can be jpg, png, webp, bmp, gif, or tiff) (desired percentage compression)
# Desired percentage compression being a number, e.g. 5 = compress the image to 5% of the original size. Minimum compression is 1% because I hate floats.
from PIL import Image
import os, sys

filePath = sys.argv[1] # compressor.py (file path) 
perc = sys.argv[2] # compressor.py (file path) (desired percentage compression)

image = Image.open(filePath)
if 'jpg' in filePath:
	ext = "jpg"
if 'png' in filePath:
	ext = "png"
if 'webp' in filePath:
	ext = "webp"
if 'bmp' in filePath:
	ext = "bmp"
if 'jpeg' in filePath:
	ext = "jpg"
if 'gif' in filePath:
	ext = "gif"
if 'tiff' in filePath: # nobody still uses this format.. right?
	ext = "tiff"
			
image.save(filePath + "_scaled." + ext,quality=int(perc)) # saves the compressed image to the same folder, adding _scaled to the name and ext being the original image file extension
print("Your image is done being compressed to roughly " + perc +"% of the original size. It is named " + filePath + "_scaled." + ext)
exit()



	

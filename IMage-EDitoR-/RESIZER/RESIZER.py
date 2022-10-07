from PIL import Image, ImageEnhance, ImageFilter
import os 

img1=Image.open('nature.jpg')
MAX_SIZE=(250,250)
img1.thumbnail(MAX_SIZE)
img1.save('RESIZED.jpg')
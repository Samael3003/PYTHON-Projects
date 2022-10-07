from PIL import Image, ImageEnhance, ImageFilter
import os 

img1 = Image.open('nature.jpg')
enhancer = ImageEnhance.Sharpness(img1)
enhancer.enhance(5).save('sharpen.jpg')
# 0: blurry
#1: original image
#2: sharpen image
from PIL import Image, ImageEnhance, ImageFilter
import os 

img1 = Image.open('nature.jpg')
enhancer = ImageEnhance.Color(img1)
enhancer.enhance(0).save('B&W.jpg')
# 0: B&W
#1: original image
#2: Saturated

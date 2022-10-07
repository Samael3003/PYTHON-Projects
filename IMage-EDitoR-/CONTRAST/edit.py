from PIL import Image, ImageEnhance, ImageFilter
import os 

img1 = Image.open('nature.jpg')
enhancer = ImageEnhance.Contrast(img1)
enhancer.enhance(0.5).save('contrast.jpg')
# 0: REDUCE CONTRAST
#1: original image
#2:  INCREASE CONTRAST
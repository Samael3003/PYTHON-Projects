from PIL import Image, ImageEnhance, ImageFilter
import os 

img1 = Image.open('nature.jpg')
enhancer = ImageEnhance.Brightness(img1)
enhancer.enhance(1.5).save('Bright.jpg')
# 0: REDUCE BRIGHTNESS
#1: original image
#2:  INCREASE BRIGHTNESS
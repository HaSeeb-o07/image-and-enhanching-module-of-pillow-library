import numpy as np
from PIL import Image, ImageEnhance
import os

# -----------------image extension change and show

# img1=Image.open('cat1.jpg')
# img1.save('cat1.png')
# img1.show()

# ---------------------image size changing
# size=(250,250)
# img1.thumbnail(size)
# img1.save('cat1.png')
# img1.show()

# ----------------------------converting all jpeg and jpg in png
# for i in os.listdir():
#     if i.endswith('.jpg') or i.endswith('.jpeg'):
#         images=Image.open(i)
#         name,extension=os.path.splitext(i)
#         images.save(f'{name}.png')

# ---------------------------------------resizing all images
# for i in os.listdir():
#     if i.endswith('.jpg') or i.endswith('.jpeg'):
#         images=Image.open(i)
#         size=(250,250)
#         images.thumbnail(size)
#         images.show()

# ----------------------------------------------sharpness

# img1=Image.open('cat1.jpg')
# enhancer=ImageEnhance.Sharpness(img1)
# enhancer.enhance(10).save('edited image.jpg')
# img2=Image.open('edited image.jpg')
# img2.show()


# 0  blurry
# 1  original
# 2 sharpness increased

# ---------------COLOUR-----------------
# img1=Image.open('cat2.jpeg')
# enhancer=ImageEnhance.Color(img1)
# enhancer.enhance(3).save('colour image.jpg')
# img2=Image.open('colour image.jpg')
# img2.show()
# # 0  black and white
# # 1  original
# # 2  colour increased
# ------------------- contrast-----------
# img1=Image.open('cat3.jpeg')
# enhancer=ImageEnhance.Contrast(img1)
# enhancer.enhance(3).save('3_image.jpg')
# img2=Image.open('3_image.jpg')
# img2.show()

# ------------------- BRIGHTNESS -----------
# img1=Image.open('cat3.jpeg')
# enhancer=ImageEnhance.Brightness(img1)
# enhancer.enhance(3).save('BRIGHT_image.jpg')
# img2=Image.open('BRIGHT_image.jpg')
# img2.show()



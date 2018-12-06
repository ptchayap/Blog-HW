import cv2
import numpy as np
img = cv2.imread(r'E:\Image_Processing\Blog-HW\imageprocessing\image\im.jpeg',0)
h = img.shape[0]
w = img.shape[1]
for x in range(0,h,3):
    for y in range(0,w,3):
        print(img[x:x+2,y:y+2])
        
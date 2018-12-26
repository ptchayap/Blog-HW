import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread(r'E:\Image_Processing\Blog-HW\image\binary.jpg',0)
# a = cv2.erode(img,(10,10))
# b = cv2.dilate(img,(10,10))

# Open
a = cv2.erode(img,(10,10))
b = cv2.dilate(a,(10,10))
# Close
c = cv2.dilate(img,(10,10))
d = cv2.erode(c,(10,10))

plt.subplot(1,2,1)
plt.imshow(b,cmap='gray')
plt.title("Opening")
plt.subplot(1,2,2)
plt.imshow(d,cmap='gray')
plt.title("Closing")
# plt.subplot(2,2,3)
# plt.imshow(img,cmap='gray')
# plt.title("Original Image")
# plt.subplot(2,2,4)
# plt.imshow(c,cmap='gray')
# plt.title("Dilation")
plt.show()
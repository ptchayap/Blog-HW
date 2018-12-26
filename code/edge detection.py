import cv2
import numpy as np
from matplotlib import pyplot as plt
img = cv2.imread(r'E:\Image_Processing\Blog-HW\image\python.png',0)

a = cv2.Laplacian(img,cv2.CV_64F)
b = cv2.Sobel(img,cv2.CV_64F,1,0,ksize=3)
c = cv2.Sobel(img,cv2.CV_64F,0,1,ksize=3)
img_gaussian = cv2.GaussianBlur(img,(3,3),0)
kernelx = np.array([[1,1,1],[0,0,0],[-1,-1,-1]])
kernely = np.array([[-1,0,1],[-1,0,1],[-1,0,1]])
img_prewittx = cv2.filter2D(img_gaussian, -1, kernelx)
img_prewitty = cv2.filter2D(img_gaussian, -1, kernely)
imgsobel = a+b
img_prewit = img_prewittx+img_prewitty
plt.subplot(2,2,1)
plt.imshow(img,cmap='gray')
plt.title("Original Image")
plt.subplot(2,2,2)
plt.imshow(a,cmap='gray')
plt.title("Result Image from Laplacian")
plt.subplot(2,2,3)
plt.imshow(imgsobel,cmap='gray')
plt.title("Result Image from Sobel Operation")
plt.subplot(2,2,4)
plt.imshow(img_prewit,cmap='gray')
plt.title("Result Image from Prewitt Operation")
plt.show()
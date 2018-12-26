import numpy as np
import cv2

class LinearFilter():
    def __init__(self,img,width,high):
        self.img = img
        self.result = img[0:img.shape[0]-(width-1),0:img.shape[1]-(high-1)]*0
        self.w = img.shape[0]
        self.h = img.shape[1]
        self.filter_w = width
        self.filter_h = high

    def boxfilter(self):
        self.filter = np.ones(9).reshape(3,-1)
        for x in range(0,self.w-(self.filter_w-1)):
            for y in range(0,self.h-(self.filter_h-1)):
                self.result[x,y] = int(np.sum(self.img[x:x+(self.filter_w-1),y:y+(self.filter_h-1)])/(self.filter_w*self.filter_h))
        return self.result
    

if __name__ == "__main__":
    import cv2
import numpy as np
from matplotlib import pyplot as plt
img = cv2.imread(r'E:\Image_Processing\Blog-HW\image\salt_pepper.png',0)

a = cv2.boxFilter(img,-1,(3,3))
b = cv2.GaussianBlur(img,(3,3),5)
c = cv2.medianBlur(img,3)
plt.subplot(2,2,1)
plt.imshow(img,cmap='gray')
plt.title("Original Image")
plt.subplot(2,2,2)
plt.imshow(a,cmap='gray')
plt.title("Result Image from Box Filter")
plt.subplot(2,2,3)
plt.imshow(b,cmap='gray')
plt.title("Result Image from Gaussian Filter")
plt.subplot(2,2,4)
plt.imshow(c,cmap='gray')
plt.title("Result Image from Median Filter")
plt.show()

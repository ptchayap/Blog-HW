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
    img = cv2.imread(r'E:\Image_Processing\Blog-HW\imageprocessing\image\im.jpeg',0)
    cv2.imshow('mg',img)
    cv2.waitKey(0)
    test = LinearFilter(img,7,11)
    a = test.boxfilter()
    cv2.imshow('img',a)
    cv2.waitKey(0)

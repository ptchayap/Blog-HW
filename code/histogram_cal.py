import numpy as np
from math import floor


class histogram_cal():
    def __init__(self, img):
        self.img = img
        self.width = img.shape[0]
        self.high = img.shape[1]
        self.h = [0]*256
        self.eq = self.img*0
        self.h2 = [0]*256

    def cal_hist(self):
        for x in range(self.width):
            for y in range(self.high):
                i = self.img[x,y]
                self.h[i] = self.h[i]+1
        return self.h
            

    def cal_cum(self):
        self.h = self.cal_hist()
        for x in range(256):
            if (x==0):
                self.h2[x]=self.h[x]
            else:
                self.h2[x]= self.h2[x-1]+self.h[x]
        return self.h2

    def equalize(self):
        self.h = self.cal_hist()
        self.h2 = self.cal_cum()
        print(self.h2[255])
        for x in range(self.width):
            for y in range(self.high):
                i = self.img[x,y]
                self.eq[x,y] = floor((self.h2[i]/self.h2[255])*255)
        return self.eq
    
    
   
    
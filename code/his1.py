from matplotlib import pyplot as plt
from PIL import Image
import numpy as np
import math
from histogram_cal import histogram_cal

filepath = r'E:\Image_Processing\Blog-HW\imageprocessing\image\im.jpeg' # change to path of desired image
img =Image.open(filepath) # import photo
img = img.convert("L") # Convert photo to gray scale
img = np.asarray(img) # convert variable type to numpy array


## calc the histogram of the image ##
image = histogram_cal(img)
hist = image.cal_hist()

## plot the image and histogram ##
plt.subplot(121) 
implot = plt.imshow(img,cmap="gray", vmin=0, vmax=255)

plt.subplot(122)
plt.xlim([0,255])
plt.plot(hist)
plt.show()

## cumulative histogram ##
h2 = image.cal_cum()
        
plt.subplot(121)
plt.xlim([0,255])
plt.plot(hist)


plt.subplot(122)
plt.xlim([0,255])
plt.plot(h2)
plt.show()

## Equalization ##
eq = image.equalize()

## Calc hist and calc cumulative hist ##
equal = histogram_cal(eq)
hist_eq = equal.cal_cum()
        
plt.subplot(221)
plt.title('Original Image')
plt.imshow(img,cmap = 'gray')
plt.subplot(222)
plt.title("Cumulative Histogram of Original Image")
plt.xlim([0,255])
plt.plot(h2)
plt.subplot(223)
plt.title("Equalize Image ")
plt.imshow(eq,cmap = 'gray')
plt.subplot(224)
plt.title("Cumulative Histogram of Equalize Image")
plt.xlim([0,255])
plt.plot(hist_eq)
plt.show()

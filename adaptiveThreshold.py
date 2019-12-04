import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt

img = cv.imread('Pictures/Cropped.jpg',0)

def simple_thresholding(img):

    ret,thresh1 = cv.threshold(img,127,255,cv.THRESH_BINARY)
    ret,thresh2 = cv.threshold(img,127,255,cv.THRESH_BINARY_INV)
    ret,thresh3 = cv.threshold(img,127,255,cv.THRESH_TRUNC)
    ret,thresh4 = cv.threshold(img,127,255,cv.THRESH_TOZERO)
    ret,thresh5 = cv.threshold(img,127,255,cv.THRESH_TOZERO_INV)
    titles = ['Original Image','BINARY','BINARY_INV','TRUNC','TOZERO','TOZERO_INV']
    images = [img, thresh1, thresh2, thresh3, thresh4, thresh5]

    for i in range(6):
        plt.subplot(2,3,i+1),plt.imshow(images[i],'gray')
        plt.title(titles[i])
        plt.xticks([]),plt.yticks([])

    plt.show()

def adaptive_thresholding(img, satisfaction, blocksize, C):
    img = img.copy()
    img = cv.medianBlur(img, 5)
    ret,th1 = cv.threshold(img, 127, satisfaction, cv.THRESH_BINARY_INV)
    th2 = cv.adaptiveThreshold(img, satisfaction, cv.ADAPTIVE_THRESH_MEAN_C,\
                cv.THRESH_BINARY, blocksize, C)
    th3 = cv.adaptiveThreshold(img, satisfaction, cv.ADAPTIVE_THRESH_GAUSSIAN_C,\
                cv.THRESH_BINARY, blocksize, C)
    titles = ['Original Image', 'Global Thresholding (v = 127)',
                'Adaptive Mean Thresholding', 'Adaptive Gaussian Thresholding']
    images = [img, th1, th2, th3]
    for i in range(4):
        plt.subplot(2,2,i+1),plt.imshow(images[i],'gray')
        plt.title(titles[i])
        plt.xticks([]),plt.yticks([])
    plt.show()

def test(img, satisfaction: int, blocksize: int, C: int):
    img = img.copy()
    img = cv.medianBlur(img, 5)
    thresh = cv.adaptiveThreshold(img, satisfaction, cv.ADAPTIVE_THRESH_MEAN_C,\
                cv.THRESH_BINARY, blocksize, C)
    thresh = cv.medianBlur(thresh, 5)
    ret, thresh = cv.threshold(thresh, 127, satisfaction, cv.THRESH_BINARY_INV)
    kernel = np.ones((5,5),np.uint8)
    thresh = cv.morphologyEx(thresh, cv.MORPH_OPEN, kernel)

    cv.imshow(".", thresh)


#simple_thresholding(img)
#adaptive_thresholding(img, 255, 1001, 80)
test(img, 255, 501, 70)
#test(img, 255, 199, 5)

cv.waitKey(0)
cv.destroyAllWindows()

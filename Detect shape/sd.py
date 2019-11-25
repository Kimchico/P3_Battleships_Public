import cv2
import numpy as np


def mouseRGB(event,x,y,flags,param):
    if event == cv2.EVENT_LBUTTONDOWN: #checks mouse left button down condition
        colorsB = imageHSV[y,x,0]
        colorsG = imageHSV[y,x,1]
        colorsR = imageHSV[y,x,2]
        colors = image[y,x]


        print("H: ",colorsB)
        print("S: ", colorsG)
        print("V: ", colorsR)
        print("Coordinates of pixel: X: ",x,"Y: ",y)

# Read an image, a window and bind the function to window
image = cv2.imread("Pictures/all_sizes.jpg")
imageHSV = cv2.cvtColor(image,cv2.COLOR_BGR2HSV)
cv2.namedWindow('mouseRGB')
cv2.setMouseCallback('mouseRGB',mouseRGB)

#Do until esc pressed
while(1):
    cv2.imshow('mouseRGB',image)
    if cv2.waitKey(20) & 0xFF == 27:
        break
#if esc pressed, finish.
cv2.destroyAllWindows()
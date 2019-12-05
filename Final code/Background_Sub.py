# Python code for Background subtraction using OpenCV
import numpy as np
import cv2

back = cv2.imread('Pictures/picture4.png')
back_grey = cv2.cvtColor(back, cv2.COLOR_BGR2GRAY)
back_greyB = cv2.GaussianBlur(back_grey, (7, 7), 0)
current = cv2.imread('Pictures/size2_v2.jpg')
current_grey = cv2.cvtColor(current, cv2.COLOR_BGR2GRAY)
current_greyB = cv2.GaussianBlur(current_grey,(7,7),0)

difference = cv2.absdiff(back_greyB, current_greyB)
 #   _, difference = cv2.threshold(difference, 25, 255, cv2.THRESH_BINARY)
cv2.imshow('back',back_greyB)
cv2.imshow('current',current_greyB)
cv2.imshow('dif',difference)
img_binary = cv2.threshold(difference, 5,255, cv2.THRESH_BINARY)[1]
cv2.imshow('final',img_binary)
kernel = np.ones((3,3), np.uint8)
dilation = cv2.dilate(img_binary,kernel,iterations = 1)
cv2.imshow('withDil',dilation)
cv2.waitKey(0)
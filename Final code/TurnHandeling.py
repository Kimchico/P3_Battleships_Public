"""""
import cv2

cap = cv2.VideoCapture (1)

while True:
    ret, frame = cap.read()

    cv2.imshow("frame", frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
cap.release()
cv2.destroyAllWindows()
"""""

import cv2
import numpy as np
from blob import extract_blobs
from fixMinMax import *
import os
#from cropping import *
#Video capture, the number is which camera, 0 is laptop, 1 is webcam

video = cv2.VideoCapture (1)

def conversion(image):
    image = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
    lower_red = np.array([140, 80, 80]); upper_red = np.array([190, 255, 255])

    mask_red =  cv2.inRange(image, lower_red, upper_red)
    #cv2.imshow(".", mask_red)
    blob_red = extract_blobs(mask_red)
    correct_red = []

    print("red")
    for red in blob_red:
        print(len(red))
        if len(red) > 4000:
            correct_red.append(red)

    red_positions = coordinates(correct_red)
    #green_positions = coordinates(correct_green)
    print(red_positions)
    return red_positions


def denoise(feed):
    feed = cv2.medianBlur(feed, 5)
    feed = cv2.GaussianBlur(feed, (5, 5), 0)
    feed = cv2.cvtColor(feed, cv2.COLOR_BGR2GRAY)
    return feed

def findBlobs(image):
    img = image
    blobs = extract_blobs(img)
    blobs2 = []
    for blob in blobs:
        if len(blob) > 4000:
            blobs2.append(blob)

def backgroundSubtraction (background, crops):
    t = 0

    background = background[crops[0][0][1]:crops[0][1][1], crops[0][0][0]:crops[0][1][0]]
    background = denoise(background)
   # background = background[307:368, 33:78]
    while True:
        ret, frame = video.read()
        #frame = frame[307:368, 33:78]
        frame = frame[crops[0][0][1]:crops[0][1][1], crops[0][0][0]:crops[0][1][0]]
        frame = denoise(frame)
        substraction = cv2.absdiff(background, frame)
        (thresh, bi) = cv2.threshold(substraction, 5, 255, cv2.THRESH_BINARY)


    #every time t is hundred, it takes an image and resets t to 0
        if t >= 10:
            ret, background = video.read()
            #background = background[307:368, 33:78]
            background = background[crops[0][0][1]:crops[0][1][1], crops[0][0][0]:crops[0][1][0]]
            background = denoise(background)
            #print(t)
            t = 0
        t += 1
        #print(t)

        key = cv2.waitKey(20)
        if key == 27:
            break

        contours, ret = cv2.findContours(bi, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

        for cnt in contours:
           cv2.drawContours(bi, [cnt], 0, (0, 255, 0))
        #print(contours)

        #counting the amount of contours, like polygons
        cntArea = cv2.contourArea(cnt)
        #approx function, is to remove noise by removing some of the contours, by averaging them out (look up decleration)
        approx = cv2.approxPolyDP(cnt, 0.02*cv2.arcLength(cnt, True), True)

        if cntArea > 50 and cntArea < 100:
            cv2.drawContours(bi, [approx], 0, (255, 0, 0),0)
            if len(approx) < 100:
                return True
                print(contours)

        #cv2.imshow('first frame', background)
        #cv2.imshow('webcam', frame)
        #cv2.imshow('difference', bi)

        #print(bi.dtype)
        #print(bi.shape)
    #return  bi

def backgroundSubtraction_2 (background, crops):
    t = 0
    background = background[crops[1][0][1]:crops[1][1][1], crops[1][0][0]:crops[1][1][0]]
    background = denoise(background)
   # background = background[307:368, 33:78]
    while True:
        ret, frame = video.read()
        #frame = frame[307:368, 33:78]
        frame = frame[crops[1][0][1]:crops[1][1][1], crops[1][0][0]:crops[1][1][0]]
        frame = denoise(frame)
        substraction = cv2.absdiff(background, frame)
        (thresh, bi) = cv2.threshold(substraction, 5, 255, cv2.THRESH_BINARY)


    #every time t is hundred, it takes an image and resets t to 0
        if t >= 10:
            ret, background = video.read()
            #background = background[307:368, 33:78]
            background = background[crops[1][0][1]:crops[1][1][1], crops[1][0][0]:crops[1][1][0]]
            background = denoise(background)
            #print(t)
            t = 0
        t += 1
        #print(t)

        key = cv2.waitKey(20)
        if key == 27:
            break

        contours, ret = cv2.findContours(bi, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

        for cnt in contours:
           cv2.drawContours(bi, [cnt], 0, (0, 255, 0))
        #print(contours)

        #counting the amount of contours, like polygons
        cntArea = cv2.contourArea(cnt)
        #approx function, is to remove noise by removing some of the contours, by averaging them out (look up decleration)
        approx = cv2.approxPolyDP(cnt, 0.02*cv2.arcLength(cnt, True), True)

        if cntArea > 50 and cntArea < 100:
            cv2.drawContours(bi, [approx], 0, (255, 0, 0),0)
            if len(approx) < 100:
                return True
                print(contours)



#ret, background = cap.read()
#crops = conversion(background)
#background = background[307:368, 33:78]
"""
video = cv2.VideoCapture(1)
ret, frame = video.read()
crops = conversion(frame)


if backgroundSubtraction(frame, crops):
    os.system("say 'player 1 hand'")
if backgroundSubtraction_2(frame, crops):
    os.system("say 'player 2 hand'")


#background = background[307:368, 33:78]


video.release()
cv2.waitKey(1)
cv2.destroyAllWindows()
"""

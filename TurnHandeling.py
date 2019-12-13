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
#Video capture, the number is which camera, 0 is laptop, 1 is webcam
cap = cv2.VideoCapture (0)


def denoise(feed):
    feed = cv2.medianBlur(feed, 5)
    feed = cv2.GaussianBlur(feed, (7, 7), 0)
    feed = cv2.cvtColor(feed, cv2.COLOR_BGR2GRAY)
    return feed

def findBlobs(image):
    img = image
    blobs = extract_blobs(img)
    blobs2 = []
    for blob in blobs:
        if len(blob) > 500:
            blobs2.append(blob)

def backgroundSubtraction (background):
    t = 0
    background = denoise(background)

    while True:
        ret, frame = cap.read()
        frame = denoise(frame)
        substraction = cv2.absdiff(background, frame)
        (thresh, bi) = cv2.threshold(substraction, 5, 255, cv2.THRESH_BINARY)


    #every time t is hundred, it takes an image and resets t to 0
        if t >= 100:
            ret, background = cap.read()
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

        if cntArea > 500 and cntArea < 600:
            cv2.drawContours(bi, [approx], 0, (255, 0, 0),0)
            if len(approx) <= 4:
                print("hand detected")
                print(contours)
        cv2.imshow('first frame', background)
        cv2.imshow('webcam', frame)
        cv2.imshow('difference', bi)

        #print(bi.dtype)
        #print(bi.shape)
    return  bi


ret, background = cap.read()
backgroundSubtraction(background)

cap.release()
cv2.destroyAllWindows()

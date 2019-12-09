import cv2
import numpy as np
import time
#Video capture, the number is which camera, 0 is laptop, 1 is webcam
cap = cv2.VideoCapture(1)

#maybe make a loop here, where it will capture first 20 frames
delayCounter = 0
frameCount = 0
images = []
startTime = time.time()
#ret, firstFrame = cap.read()

#def denoise(firstFrame):

    #firstFrame = cv2.medianBlur(firstFrame, 5)
    #firstFrame = cv2.GaussianBlur(firstFrame, (7, 7), 0)

    #return firstFrame
#firstFrame = denoise(firstFrame)
#gray = cv2.cvtColor(firstFrame, cv2.COLOR_BGR2GRAY)

#while True:

    #images.append(gray)
    #if frameCount == 19:
     #   break
    #frameCount += 1

#print(len(images))

#meanImage = sum(images) / len(images)
#print(meanImage)


#Run through the frame continuously
while True:


        ret, frame = cap.read()
        ret, firstFrame = cap.read()
        gray = cv2.cvtColor(firstFrame, cv2.COLOR_BGR2GRAY)


        if time.time() - startTime >= 50:
            ret, firstFrame = cap.read()
            secFrame = "openCV10SecFrame.png".format(delayCounter)
            cv2.imwrite(secFrame, firstFrame)
            startTime = time.time()
        delayCounter += 1


        def denoise(firstFrame):

            firstFrame = cv2.medianBlur(firstFrame, 5)
            firstFrame = cv2.GaussianBlur(firstFrame, (9, 9), 0)

            return firstFrame


        firstFrame = denoise(firstFrame)
        frame = denoise(frame)

        gray2 = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        #substraction = gray2 - gray
        #substraction = grey - [images for image in images]
        #substraction = gray2 - [gray for image in gray]
        subtraction = cv2.absdiff(gray2, gray)
        #subtraction = cv2.absdiff(gray2, [images for image in images])
        ret, binary = cv2.threshold(subtraction, 5, 255, cv2.THRESH_BINARY)

        cv2.imshow('soething', firstFrame)
        cv2.imshow('first frame', gray)
        cv2.imshow('webcam', gray2)
        cv2.imshow('difference', binary)

        key = cv2.waitKey(20)

        if key == 27:
            break

cap.release()
cv2.destroyAllWindows()

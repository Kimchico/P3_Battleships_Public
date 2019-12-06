import cv2
import numpy as np
#Video capture, the number is which camera, 0 is laptop, 1 is webcam
cap = cv2.VideoCapture (0)

#maybe make a loop here, where it will capture first 20 frames
frameCount = 0
images = []

ret, firstFrame = cap.read()


#while True:

#    images.append(firstFrame)
 #   if frameCount == 19:
  #      break
   # frameCount += 1

#print(len(images))

#meanImage = sum(images) / len(images)
#print(meanImage)

#def denoise(frame):

 #   frame = cv2.medianBlur(frame, 5)
  #  frame = cv2.GaussianBlur(frame, (7, 7), 0)

   # return frame

#Run through the frame continuously
while True:

        ret, frame = cap.read()
        substraction = frame - firstFrame
        #substraction = frame - [images for image in images]
        (thresh, bi) = cv2.threshold(substraction, 127, 255, cv2.THRESH_BINARY)

        cv2.imshow('first frame', firstFrame)
        cv2.imshow('webcam', frame)
        cv2.imshow('difference',substraction)

        key = cv2.waitKey(20)

        if key == 27:
            break

cap.release()
cv2.destroyAllWindows()

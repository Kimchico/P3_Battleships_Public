import cv2
import numpy as np
# from blob import extract_blobs;


image_calibration = cv2.imread('testingShit.jpg')
image_calibration = cv2.cvtColor(image_calibration, cv2.COLOR_BGR2HSV)
cv2.imshow("test", image_calibration)

cv2.waitKey(0)
cv2.destroyAllWindows()




# Imports
import cv2
import numpy as np
from Colors import *

# Converter (DOESNT WORK)
"""
def convert(image):
    w , h, _ = image.shape
    for x in range(int(w)):
        for y in range(int(h)):
            newR = int(image[x, y][2]) / 255
            newG = int(image[x, y][1]) / 255
            newB = int(image[x, y][0]) / 255

            cMax = max(newR, newG, newB)
            cMin = min(newR, newG, newB)

            delta = cMax - cMin

            if cMax == cMin:
                h = 0

            elif cMax == newR:
                h = (60 * ((newG - newB) / delta) + 360) % 360

            elif cMax == newG:
                h = (60 * ((newB - newR) / delta) + 120) % 360

            elif cMax == newB:
                 h = (60 * ((newR - newG) / delta) + 240) % 360

            if cMax == 0:
                s = 0
            else:
                s = (delta / cMax) * 100

            v = cMax * 100
            image[x, y] = h, s, v

    return image
"""
def color(color, hsv):
    mask = cv2.inRange(hsv, LOW_THRESHOLD[color], HIGH_THRESHOLD[color])
    cv2.imshow(str(color), mask)

# Read the camera.
cap = cv2.VideoCapture(0)

# While loop that runs while true.
while(1):

    # Get camera feed.
    _, frame = cap.read()
    kernel = np.ones((5,5),np.uint8)
    frame = cv2.GaussianBlur(frame, (5,5), cv2.BORDER_DEFAULT)
    frame = cv2.morphologyEx(frame, cv2.MORPH_OPEN, kernel)

    # Convert the camera feed to HSV.
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    # Show the frames (maybe use numpy.concatenate).
    color(Color.RED, hsv)
    color(Color.GREEN, hsv)
    color(Color.BLUE, hsv)


    # Set variable k equal to keypressed.
    k = cv2.waitKey(1) & 0xFF

    # If the k variable is equal to q then quit the program.
    if k == ord('q'):
        break

# Delete all windows.
cv2.destroyAllWindows()

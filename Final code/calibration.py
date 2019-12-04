# This modules purpose is to find the coordinates for each grid

import cv2
import numpy as np
from blob import extract_blobs

image = cv2.imread("Pictures/fourblobs.png")

def calibration(image_to_crop):
    # Blur image
    blurred_image = cv2.GaussianBlur(image_to_crop, (17, 17), cv2.BORDER_DEFAULT)

    # Threshold and mask white
    lower_white = np.array([200, 200, 200]); upper_white = np.array([255, 255, 255])
    binary_image = cv2.inRange(image_to_crop, lower_white, upper_white)

    # Find blob
    image_blobs = extract_blobs(binary_image)

    # Find placement grids
    player1_placement = (image_blobs[0][0], image_blobs[0][-1])
    player2_placement = (image_blobs[-1][0], image_blobs[-1][-1])

    # Find attack grids
    player1_attack = (image_blobs[1][0], image_blobs[1][-1])
    player2_attack = (image_blobs[2][0], image_blobs[2][-1])

    # Return the coordinates to the function, hence turning the function into these values
    # These values can be accessed by refering to them as an array
    return ((player1_placement, player2_placement), (player1_attack, player2_attack))


video = cv2.VideoCapture(0)
#cap.set(cv2.CAP_PROP_AUTO_EXPOSURE, 0.25)
#cap.set(cv2.CAP_PROP_EXPOSURE, -3)
temp = 0
while True:
    check, frame = video.read()
    cv2.imshow("Capturing",frame)

    if temp == 10:
        break

    temp += 1

positions = calibration(image)
print(positions)
video.release()
cv2.destroyAllWindows()

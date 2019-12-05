# This modules purpose is to find the coordinates for each grid
import cv2
import numpy as np
from blob import extract_blobs

image = cv2.imread("/Users/mikkelsangmeebaunsgaard/Desktop/blobs.jpg")

def calibration(image_to_crop):
    # Blur image
    blurred_image = cv2.GaussianBlur(image_to_crop, (5, 5), cv2.BORDER_DEFAULT)

    # Threshold and mask white
    lower_white = np.array([110, 110, 110]); upper_white = np.array([255, 255, 255])
    binary_image = cv2.inRange(blurred_image, lower_white, upper_white)

    cv2.imshow("mask", binary_image)
    # Find blob
    image_blobs = extract_blobs(binary_image)
    #image_blobs.pop()

    """
    for blob in image_blobs:
        tempx = blob[-1][1] - blob[0][1]
        tempy = blob[-1][0] - blob[0][0]
        print(tempx, tempy)
        if (abs(tempx/tempy) < 0.85):
            image_blobs.remove(blob)
    """
    image_blobs.pop()



    # Find placement grids
    player1_placement = (image_blobs[0][0], image_blobs[0][-1])
    player2_placement = (image_blobs[-1][0], image_blobs[-1][-1])

    # Find attack grids
    player1_attack = (image_blobs[1][0], image_blobs[1][-1])
    player2_attack = (image_blobs[2][0], image_blobs[2][-1])

    # Return the coordinates to the function, hence turning the function into these values
    # These values can be accessed by refering to them as an array
    return ((player1_placement, player2_placement), (player1_attack, player2_attack))


video = cv2.VideoCapture(1)
#video.set(cv2.CAP_PROP_AUTO_EXPOSURE, 0.25)
#video.set(cv2.CAP_PROP_EXPOSURE, -3)
temp = 0
while True:
    check, frame = video.read()

    if temp == 20:
        break

    temp += 1

positions = calibration(image)
print(positions)
video.release()
cv2.waitKey(0)
cv2.destroyAllWindows()

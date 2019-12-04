import numpy as np
import cv2
from blob import extract_blobs
from calibration import *

# Image = the image you want to crop
# Player = what player it should do its operations for
# Type = defines if it is the attack or placement grid it should make
# Coordinates = the coordinate set it should derive its coordinates for
def detectShapes(image, player : int, type : int, cord):
    image = cv2.GaussianBlur(image, (5, 5), cv2.BORDER_DEFAULT)
    lower_red = np.array([0, 0, 80])
    higher_red = np.array([25, 20, 255])

    if player == 1:
        if type == 0:
            cropped_image = image[cord[1][0][0][1]:cord[1][0][1][1], cord[1][0][0][0]:cord[1][0][1][0]]
            print(cord[1][0][0][1], cord[1][0][1][1], cord[1][0][0][0], cord[1][0][1][0])
            cv2.imshow("Cropped", cropped_image)
            binary_image = cv2.inRange(cropped_image, lower_red, higher_red)
            ship_positions = extract_blobs(binary_image)
        if type == 1:
            cropped_image = image[cord[0][1][0][1]:cord[0][1][1][1], cord[0][1][0][0]:cord[0][1][1][0]]
            cv2.imshow("Cropped", cropped_image)
            binary_image = cv2.inRange(cropped_image, lower_red, higher_red)
            ship_positions = extract_blobs(binary_image)

detectShapes(cv2.imread("/Users/mikkelsangmeebaunsgaard/Desktop/test_1.jpg"), 1, 0, positions)

cv2.waitKey(0)
cv2.destroyAllWindows()
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
    #lower_red = np.array([0, 0, 80])
    #higher_red = np.array([25, 20, 255])

    if player == 1:
        if type == 0:
            cropped_image = image[cord[0][0][0][1]:cord[0][0][1][1], cord[0][0][0][0]:cord[0][0][1][0]]
            #binary_image = cv2.inRange(cropped_image, lower_red, higher_red)
            #ship_positions = extract_blobs(binary_image)
            cv2.imshow("Cropped", cropped_image)

        if type == 1:
            cropped_image = image[cord[1][0][0][1]:cord[0][0][1][1], cord[1][0][0][0]:cord[0][1][1][0]]
            #binary_image = cv2.inRange(cropped_image, lower_red, higher_red)
            #ship_positions = extract_blobs(binary_image)
            cv2.imshow("Cropped", cropped_image)

    elif player == 2:
        if type == 0:
            cropped_image = image[cord[0][1][0][1]:cord[0][1][1][1], cord[0][1][0][0]:cord[0][1][1][0]]
            #binary_image = cv2.inRange(cropped_image, lower_red, higher_red)
            #ship_positions = extract_blobs(binary_image)
            cv2.imshow("Cropped", cropped_image)

        if type == 1:
            cropped_image = image[cord[1][1][0][1]:cord[1][1][1][1], cord[1][1][0][0]:cord[1][1][1][0]]
            #binary_image = cv2.inRange(cropped_image, lower_red, higher_red)
            #ship_positions = extract_blobs(binary_image)
            cv2.imshow("Cropped", cropped_image)

    cv2.imwrite("Pictures/cropped_witships.jpg", cropped_image)

video = cv2.VideoCapture(1)
#video.set(cv2.CAP_PROP_AUTO_EXPOSURE, 0.25)
#video.set(cv2.CAP_PROP_EXPOSURE, -3)
#video.set(cv2.CAP_PROP_FRAME_WIDTH, 1280);
#video.set(cv2.CAP_PROP_FRAME_HEIGHT, 720);
#video.set(3, 1920)
#video.set(4, 900)

while True:
    check, frame = video.read()
    cv2.imshow("Frame", frame)
    key = cv2.waitKey(1)
    if key == ord('q'):
        break


cv2.imwrite("Pictures/frame_2.jpg", frame)
detectShapes(frame, 1, 0, positions)
#detectShapes(frame, 1, 1, positions)
#detectShapes(frame, 2, 0, positions)
#detectShapes(frame, 2, 1, positions)

video.release()
cv2.waitKey(0)
cv2.destroyAllWindows()

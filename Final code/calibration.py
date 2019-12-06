# This modules purpose is to find the coordinates for each grid
import cv2
import numpy as np
from blob import extract_blobs

#image = cv2.imread("/Users/mikkelsangmeebaunsgaard/Desktop/mikkelTHIS.jpg"
def coordinates(blobs):
    coordinates = []
    for blob in blobs:
        x = []
        y = []
        for pixel in blob:
            x.append(pixel[-1])
            y.append(pixel[0])
        x.sort(); y.sort()

        coordinates.append(((x[0], y[0]), (x[-1], y[-1])))
    return coordinates

def calibration(image_to_crop):
    # Blur image
    blurred_image = cv2.cvtColor(image_to_crop, cv2.COLOR_BGR2GRAY)
    blurred_image = cv2.GaussianBlur(blurred_image, (21, 21), cv2.BORDER_DEFAULT)

    # Threshold and mask white
    #lower_white = np.array([90, 90, 90]); upper_white = np.array([255, 255, 255])

    binary_image = cv2.inRange(blurred_image, 130, 255)
    cv2.imshow("gray", blurred_image)
    cv2.imshow("mask", binary_image)
    # Find blob
    image_blobs = extract_blobs(binary_image)
    #image_blobs.pop()

    correct_blobs = []

    for blob in image_blobs:
        if len(blob) > 50000:
            correct_blobs.append(blob)

    coord = coordinates(correct_blobs)

    #for blob in image_blobs:
    #    print(blob[0], blob[-1])

    # Find placement grids
    player1_placement = (coord[0][0], coord[0][-1])
    player2_placement = (coord[-1][0], coord[-1][-1])

    # Find attack grids
    player1_attack = (coord[1][0], coord[1][-1])
    player2_attack = (coord[2][0], coord[2][-1])

    # Return the coordinates to the function, hence turning the function into these values
    # These values can be accessed by refering to them as an array
    return ((player1_placement, player2_placement), (player1_attack, player2_attack))


video = cv2.VideoCapture(1)
#video.set(cv2.CAP_PROP_AUTO_EXPOSURE, 0.25)
#video.set(cv2.CAP_PROP_EXPOSURE, -3)
#video.set(CV_CAP_PROP_FRAME_WIDTH, 1280);
#video.set(CV_CAP_PROP_FRAME_HEIGHT, 720);
#video.set(3, 1920)
#video.set(4, 900)

temp = 0
while True:
    check, frame = video.read()
    #cv2.imshow("frame", frame)
    if temp == 20:
        break

    temp += 1

#cv2.imshow("frame", frame)
#cv2.imwrite("/Users/mikkelsangmeebaunsgaard/Desktop/whiteblobs.jpg", frame)
cv2.imwrite("Pictures/withoutSquares.jpg", frame)
positions = calibration(frame)

print(positions)
video.release()
cv2.waitKey(0)
cv2.destroyAllWindows()

import cv2
import numpy as np
from blob import extract_blobs


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




image = cv2.imread("/Users/mikkelsangmeebaunsgaard/Desktop/Photo on 05-12-2019 at 11.03.jpg")

def conversion(image):

image = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

lower_red = np.array([155, 100, 100]); upper_red = np.array([170, 255, 255])
lower_green = np.array([50, 100, 30]); upper_green = np.array([65, 255, 255])

mask_red =  cv2.inRange(image, lower_red, upper_red)
mask_green = cv2.inRange(image, lower_green, upper_green)



blob_red = extract_blobs(mask_red)
blob_green = extract_blobs(mask_green)


correct_red = []
correct_green = []

for red in blob_red:
    if len(red) > 1000:
        correct_red.append(red)

for green in blob_green:
    if len(green) > 1000:
        correct_green.append(green)

red_positions = coordinates(correct_red)
green_positions = coordinates(correct_green)



red = image[red_positions[0][0][1]:red_positions[0][1][1], red_positions[0][0][0]:red_positions[0][-1][0]]
green = image[green_positions[0][0][1]:green_positions[0][1][1], green_positions[0][0][0]:green_positions[0][-1][0]]

cv2.imshow("green", green)
cv2.imshow("image", image)
cv2.imshow("red", red)

cv2.waitKey(0)
cv2.destroyAllWindows()

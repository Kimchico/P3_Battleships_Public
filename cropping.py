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

red_positions = []; green_positions = []

def conversion(image):
    image = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
    cv2.imshow("image", image)
    lower_red = np.array([140, 100, 100]); upper_red = np.array([180, 255, 255])
    lower_green = np.array([40, 100, 40]); upper_green = np.array([80, 255, 255])

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
    print(red_positions)
    print(green_positions)

def crop_1(image):
    red = image[red_positions[0][0][1]:red_positions[0][1][1], red_positions[0][0][0]:red_positions[0][-1][0]]
    return red

def crop_2(image):
    green = image[green_positions[0][0][1]:green_positions[0][1][1], green_positions[0][0][0]:green_positions[0][-1][0]]
    return green

"""

def crop_1(image):
    red = image[100:200, 100:200]

    return red
def crop_2(image):
    green = image[400:500, 500:600]
    return green
"""
video = cv2.VideoCapture(1)
#ret, frame = video.read()
#image = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
#cv2.imshow("frame", image)
#cv2.imshow("image", image)

#cv2.imshow("player 1", crop_1(frame))
#cv2.imshow("player 2", crop_2(frame))
conversion(image)
cv2.imshow("player 1", crop_1(image))
cv2.imshow("player 2", crop_2(image))
"""
while True:
    ret, frame = video.read()
    key = cv2.waitKey(1)
    #conversion(frame)
    cv2.imshow("player 1", crop_1(frame))
    cv2.imshow("player 2", crop_2(frame))
    if key == ord('q'):
        break
"""
#conversion(image)
cv2.waitKey(0)
cv2.destroyAllWindows()

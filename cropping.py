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
    lower_red = np.array([160, 80, 80]); upper_red = np.array([190, 255, 255])
    #lower_green = np.array([20, 100, 40]); upper_green = np.array([80, 255, 255])

    mask_red =  cv2.inRange(image, lower_red, upper_red)
    cv2.imshow("mask", mask_red)
    #mask_green = cv2.inRange(image, lower_green, upper_green)



    blob_red = extract_blobs(mask_red)
    #blob_green = extract_blobs(mask_green)


    correct_red = []
    #correct_green = []

    print("red")
    for red in blob_red:
        print(len(red))
        if len(red) > 4000:
            correct_red.append(red)
    """
    print("green")
    for green in blob_green:
        print(len(green))
        if len(green) > 1000:
            correct_green.append(green)
    """
    red_positions = coordinates(correct_red)
    #green_positions = coordinates(correct_green)
    print(red_positions)
    return red_positions
    #red = image[red_positions[0][0][1]:red_positions[0][1][1], red_positions[0][0][0]:red_positions[0][-1][0]]

    #green = image[green_positions[0][0][1]:green_positions[0][1][1], green_positions[0][0][0]:green_positions[0][-1][0]]

    #cv2.imshow("red", red)
    #cv2.imshow("green", green)


"""

def crop_1(image):
    red = image[100:200, 100:200]

    return red
def crop_2(image):
    green = image[400:500, 500:600]
    return green
"""
video = cv2.VideoCapture(1)
ret, frame = video.read()
#ret, frame = video.read()
#image = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
#cv2.imshow("frame", image)
#cv2.imshow("image", image)

#cv2.imshow("player 1", crop_1(frame))
#cv2.imshow("player 2", crop_2(frame))
#conversion(image)
crops = conversion(frame)


"""

while True:
    ret, frame = video.read()
    key = cv2.waitKey(1)
    cv2.imshow("player1", frame[crops[0][0][1]:crops[0][1][1], crops[0][0][0]:crops[0][1][0]])
    cv2.imshow("player2", frame[crops[1][0][1]:crops[1][1][1], crops[1][0][0]:crops[1][1][0]])

    if key == ord('q'):
        break


#conversion(image)
cv2.waitKey(0)
cv2.destroyAllWindows()
"""
cv2.waitKey(0)
cv2.destroyAllWindows()

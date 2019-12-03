import cv2
import numpy as np
from blob import extract_blobs

image = cv2.imread("Pictures/green.png")

def gammaCorrection(image):
    image = cv2.GaussianBlur(image, (5, 5), cv2.BORDER_DEFAULT)
    gammaImage = np.zeros(image.shape, image.dtype)

    for y in range(image.shape[0]):
        for x in range(image.shape[1]):
            for c in range(image.shape[2]):
                gammaImage[y, x, c] = np.clip(3 * image[y, x ,c] + (0), 0, 255)


    #gammaImage = np.array([np.clip(3 * (pixel[index in range(0, 2)]), 0, 255) for pixel in image])
    #ammaImage = np.array(image)

    #for pixel in gammaImage:
    #    np.clip(pixel[index for index in range(2)], 0, 255)

    #print(gammaImage.shape)
    cv2.imshow(".", gammaImage)
    return gammaImage

def normalThreshold(image, color : str):
    image = cv2.cvtColor(image, cv2.COLOR_BGR2YUV)
    cv2.imshow("YUV color space", image)
    if color == "red":
        mask = cv2.inRange(image, np.array([80, 80, 230]), np.array([129, 122, 255]))
    elif color == "green":
        mask = cv2.inRange(image, np.array([197, 80, 60]), np.array([237, 121, 102]))
    return mask

def adaptiveMean(image):
    mask =  cv2.adaptiveThreshold(grayImage, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 11, 2)
    return mask

#maybe implement otsu method on different color channels?


def findBlobs(image):
    blobs = extract_blobs(image)

    for blob in blobs:
        print(blob[0], blob[-1])

findBlobs(normalThreshold(gammaCorrection(image), "green"))
cv2.imshow("Normal mask", normalThreshold(gammaCorrection(image), "green"))
#cv2.imshow("Mean mask", adaptiveMean(gammaCorrection(image)))
cv2.waitKey(0)
cv2.destroyAllWindows()

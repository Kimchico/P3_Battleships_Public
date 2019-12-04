import cv2
import numpy as np
import pygame
# from blob import extract_blobs;


image_calibration = cv2.imread('Pictures/gridBlob.jpg')
image = cv2.imread('Pictures/test_2.jpg')
#cv2.imshow('original', image)
#cv2.imshow('calibrate', image_calibration)

# Victors cap settings below:
#cap.set(cv2.CAP_PROP_AUTO_EXPOSURE, 0.25)
#cap.set(cv2.CAP_PROP_EXPOSURE, -3)

def extract_blobs(binary_image):
    blobs = []
    for y in range(0, binary_image.shape[0]):
        for x in range(0, binary_image.shape[1]):
            if binary_image[y, x] > 0:
                binary_image[y, x] = 0
                blob_pixels = []
                queue = [[y, x]]

                while len(queue) > 0:

                    y_temp = queue[0][0]
                    x_temp = queue[0][1]

                    if x_temp + 1 < binary_image.shape[1] and binary_image[y_temp, x_temp + 1] > 0:
                        binary_image[y_temp, x_temp + 1] = 0
                        queue.append([y_temp, x_temp + 1])
                    if y_temp + 1 < binary_image.shape[0] and binary_image[y_temp + 1, x_temp] > 0:
                        binary_image[y_temp + 1, x_temp] = 0
                        queue.append([y_temp + 1, x_temp])
                    if x_temp - 1 > 0 and binary_image[y_temp, x_temp - 1] > 0:
                        binary_image[y_temp, x_temp - 1] = 0
                        queue.append([y_temp, x_temp - 1])
                    if y_temp - 1 > 0 and binary_image[y_temp - 1, x_temp] > 0:
                        binary_image[y_temp - 1, x_temp] = 0
                        queue.append([y_temp - 1, x_temp])

                    blob_pixels.append(queue.pop(0))
                blobs.append(blob_pixels)
    return blobs


def threshold(image):
    image = cv2.GaussianBlur(image, (17, 17), cv2.BORDER_DEFAULT)
    #image_2 = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
    lower = np.array([200, 200, 200])
    upper = np.array([255, 255, 255])
    mask = cv2.inRange(image, lower, upper)
    #cv2.imshow('mask', mask)
    return mask


def find_shapes(image):
    binary_image = threshold(image)
    blobs = extract_blobs(binary_image)

    min_value = (0, 0)
    max_value = (0, 0)

    for blob in blobs:
        min_value = list(map(int, blob[0]))
        max_value = list(map(int, blob[-1]))

        yield (min_value, max_value)

def crop(image_calibration, imageToCrop, imageName : str):
    points_toCrop = []

    for points in find_shapes(image_calibration):
        points_toCrop.append(points)

    offset = 5
    crop_img = image[points_toCrop[0][0][0]-offset:points_toCrop[0][1][0]+offset, points_toCrop[0][0][1]-offset:points_toCrop[0][1][1]+offset]
    cv2.imwrite('Pictures/' + imageName, crop_img)


if __name__ == '__main__':
    cv2.waitKey(0)
    cv2.destroyAllWindows()

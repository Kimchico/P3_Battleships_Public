import cv2
import numpy as np
import pygame;
# from blob import extract_blobs;


image = cv2.imread('C:/Users/David/Desktop/P3/v3.png')
cv2.imshow('original', image)

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
    image = cv2.GaussianBlur(image, (9,9), cv2.BORDER_DEFAULT)
    image_2 = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
    lower = np.array([0, 0, 0])
    upper = np.array([1, 1, 1])
    mask = cv2.inRange(image_2, lower, upper)
    cv2.imshow('mask', mask)
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

points_toCrop = []

for points in find_shapes(image):
    points_toCrop.append(points)

print(points_toCrop)
crop_img = image[points_toCrop[0][1][0]:points_toCrop[1][0][0], points_toCrop[0][1][1]:points_toCrop[1][0][1]]
cv2.imshow('Cropped', crop_img)

cv2.waitKey()
cv2.destroyAllWindows()

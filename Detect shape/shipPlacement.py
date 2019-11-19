import pygame; import cv2; import numpy as np;
from blob import extract_blobs;

def threshold_red(image):
    result = image.copy()
    image = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
    lower = np.array([155,25,0])
    upper = np.array([179,255,255])
    mask = cv2.inRange(image, lower, upper)
    #result = cv2.bitwise_and(result, result, mask=mask)
    return mask






def find_shapes(path_image: str, path_template: str, threshold: float):
    image = cv2.imread(path_image)
    binary_image = threshold_red(image)
    cv2.imshow("test", binary_image)
    blobs = extract_blobs(binary_image)

    min_value = (0, 0)
    max_value = (0, 0)

    for blob in blobs:
        min_value = blob[0]
        max_value = blob[-1]

        yield (min_value, max_value)





if __name__ == "__main__":
    # Processing goes here
    for test in find_shapes('Pictures/picture_2.png', 'Pictures/red.png',  1):
        print(test)
    cv2.waitKey(0)
    cv2.destroyAllWindows()









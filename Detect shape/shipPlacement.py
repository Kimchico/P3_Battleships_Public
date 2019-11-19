import pygame; import cv2; import numpy as np; import colorsys as cs


def find_shapes(path) -> str:
    image = cv2.imread(path)
    kernel = np.ones((5,5),np.uint8)
    image = cv2.GaussianBlur(image, (5, 5), cv2.BORDER_DEFAULT)
    image = cv2.morphologyEx(image, cv2.MORPH_OPEN, kernel)
    hsv_image = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
    hsv_values = cs.rgb_to_hsv(234, 33, 45)
    mask = cv2.inRange(hsv_image, (hsv_values[0] - 10, hsv_values[1], hsv_values[2]),
                      (hsv_values[0] + 50, 255, 255))

    result = cv2.bitwise_and(image, image, mask=mask)
    cv2.imshow("Original", image)
    cv2.imshow("Mask", mask)
    cv2.imshow("Bitmask", result)

if __name__ == "__main__":
    # Processing goes here
    find_shapes('Pictures/picture_2.png')
    cv2.waitKey(0)
    cv2.destroyAllWindows()









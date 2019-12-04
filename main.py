# This is the main thread of the P3 program.
# libraries::
import numpy as np
import cv2
import pygame

# modules::
from crop import *
from checkingGrid import *


## Image to calibrate where the grid is located
image_calibration = cv2.imread('Pictures/gridBlob.jpg')

## Image to actually crop (should be the orignal one)
image = cv2.imread('Pictures/test_2.jpg')

crop(image_calibration, image, "Grid_Image.jpg")

# PATH TO NEW IMAGE IS Pictures/Grid_Image.jpg !!

for point in find_shapes('Pictures/Grid_Image.jpg'):
    print(point)
    for MinMax in shape_positions(image,point):
        print(MinMax)
        fill_array(MinMax,placementArr)
#PRINTING THE ARRAY< FOR DEBUGGING
for row in placementArr:
    print(row)





















if __name__ == "__main__":
    cv2.waitKey(0)
    cv2.destroyAllWindows()

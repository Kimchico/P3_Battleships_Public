# Python code for Background subtraction using OpenCV
import numpy as np
import cv2
from blob import extract_blobs
from fixMinMax import coordinates
import pygame
import random
def detectShapePosition(back,curent,thresh, type):
    awr = random.randrange(100000)
    img = cv2.imread('Pictures/', 0)
    img2 = img.copy()
    template = cv2.imread('template.jpg', 0)
    w, h = template.shape[::-1]
    '''
    current=cv2.resize(curent,(width,height))
    current_grey = cv2.cvtColor(current, cv2.COLOR_BGR2GRAY)
    current_greyB = cv2.GaussianBlur(current_grey, (7, 7), 0)
    back_greyB = cv2.GaussianBlur(back_grey, (7, 7), 0)
    difference = cv2.absdiff(back_greyB, current_greyB)
    kernel = np.ones((5,5), np.uint8)
    img_binary = cv2.threshold(difference, thresh,255, cv2.THRESH_BINARY)[1]
    erosion = cv2.erode(img_binary,kernel,iterations=2)
    for point in find_shapes(erosion):
        for MinMax in shape_positions(point,width,height):
            positions = shape_gridP(MinMax)
            print(positions)
            yield positions
    '''
    cv2.waitKey(0)
def cvimage_to_pygame(image):
    """Convert cvimage into a pygame image"""
    return pygame.image.frombuffer(image.tostring(), image.shape[1::-1],
                                   "RGB")
def shape_positions(coord,width,height):
    cubeWidth = int(width / 10)
    cubeHeight = int(height / 10)
    print(cubeWidth)
    print(cubeHeight)
    shapeXMin = coord[0][0]
    shapeYMin = coord[0][1]
    shapeXMax = coord[1][0]
    shapeYMax = coord[1][1]
    shapeRowMin = 0
    shapeColumnMin = 0
    shapeRowMax = 0
    shapeColumnMax = 0
    xMin = 0
    xMax = 10
    yMin = 0
    yMax = 10
    while (xMin * cubeWidth) <= (shapeXMin) and xMin <= 10:
        print('XMIN')
        print(str(xMin * cubeWidth) + ' is smaller than ' + str(shapeXMin))
        shapeColumnMin = xMin
        print(str(shapeColumnMin))
        xMin += 1
    xMin=0
    print('STOP')
    while (yMin * cubeHeight) <= (shapeYMin) and yMin <= 10:
        print('YMIN')
        print(str(yMin * cubeHeight) + ' is smaller than ' + str(shapeYMin))
        shapeRowMin = yMin
        print(str(shapeRowMin))
        yMin += 1
    yMin=0
    print('STOP')
    while (xMax * cubeWidth) >= shapeXMax  and xMax <= 10:
        print('XMAX')
        print(str(xMax * cubeWidth) + ' is bigger than ' + str(shapeXMax))
        shapeColumnMax = xMax
        print(str(shapeColumnMax))
        xMax -= 1
    xMax=0
    print('STOP')
    while ((yMax * cubeHeight)) >= shapeYMax  and yMax <= 10:
        print('YMAX')
        print(str(yMax * cubeHeight) + ' is bigger than ' + str(shapeYMax))
        shapeRowMax = yMax
        print(str(shapeRowMax))
        yMax -= 1
    print((shapeColumnMin,shapeColumnMax,shapeRowMin,shapeRowMax))
    if (shapeXMax>(cubeWidth*10)):
        shapeColumnMax=10
    if (shapeYMax>(cubeHeight*10)):
        shapeRowMax=10
    diffColumn=shapeColumnMax-shapeColumnMin
    diffRows=shapeRowMax-shapeRowMin
    if(diffColumn==0):
        shapeColumnMax=shapeColumnMax+1
    if(diffRows==0):
        shapeRowMax=shapeRowMax+1
    if(diffColumn>=2 and diffRows>=2):
        if(diffColumn==2 and diffRows==2):
            if ((shapeYMax - shapeYMin) > (shapeXMax - shapeXMin)):
                shapeColumnMax = shapeColumnMax - 1
            elif ((shapeYMax - shapeYMin) < (shapeXMax - shapeXMin)):
                shapeRowMax = shapeRowMax - 1
        else:
            if(diffColumn>diffRows):
                shapeRowMax=shapeRowMax-1
            if(diffRows>diffColumn):
                shapeColumnMax=shapeColumnMax-1
    yield(shapeColumnMin,shapeColumnMax,shapeRowMin,shapeRowMax)
def shape_gridP(MinMax):
    Vmin = MinMax[0]
    Vmax = MinMax[1]
    Hmin = MinMax[2]
    Hmax = MinMax[3]
    positions=[]
    if Vmax - Vmin == 1:
        if Hmax - Hmin == 1:
            positions.append([Vmin,Hmin])
        else:
            for i in range(Hmin, Hmax):
                positions.append([Vmin,i])
    if Hmax - Hmin == 1:
            for j in range(Vmin, Vmax):
                positions.append([j,Hmin])
    return positions
def find_shapes(image):
    img = image
    blobs = extract_blobs(img)
    blobs2 = []
    h,w=img.shape
    y=h/10
    x=w/10

    for blob in blobs:
        min_value = blob[0]
        max_value = blob[-1]
        if max_value[1]-min_value[1] < x*5 and max_value[0]-min_value[0] < y*5:
            blobs2.append(blob)
    for blob2 in blobs2:
        print('after removing '+str(len(blob2)))
    blobs3=coordinates(blobs2)
    for blob3 in blobs3:
        min_value = blob3[0]
        max_value = blob3[-1]
        print('Min Value: '+str(min_value))
        print('Max Value: ' + str(max_value))
        yield (min_value, max_value)
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
back = cv2.imread('Pictures/empty.png')
curent = cv2.imread('Pictures/barrage.png')
cv2.imshow('smth',back)
cv2.imshow('smth2',curent)
w,h,c=back.shape
current_grey = cv2.cvtColor(curent, cv2.COLOR_BGR2GRAY)
current_greyB = cv2.GaussianBlur(current_grey, (7, 7), 0)
back_grey = cv2.cvtColor(back, cv2.COLOR_BGR2GRAY)
back_greyB = cv2.GaussianBlur(back_grey, (7, 7), 0)
difference = cv2.absdiff(back_greyB, current_greyB)
cv2.imshow('smth2',difference)
kernel = np.ones((5, 5), np.uint8)
img_binary = cv2.threshold(difference, 16, 255, cv2.THRESH_BINARY)[1]
erosion = cv2.erode(img_binary, kernel, iterations=2)
cv2.imshow('smth',erosion)
for r in extract_blobs(erosion):
    min_value = r[0]
    max_value = r[-1]
    print(min_value,max_value)
    for MinMax in shape_positions(r, w, h):
        print(MinMax)


cv2.waitKey(0)
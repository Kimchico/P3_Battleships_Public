# Python code for Background subtraction using OpenCV
import numpy as np
import cv2
from blob import extract_blobs
from fixMinMax import coordinates
import pygame


back = cv2.imread('Pictures/Cropped.jpg')
back_grey = cv2.cvtColor(back, cv2.COLOR_BGR2GRAY)
back_greyBH = cv2.equalizeHist(back_grey)
curent = cv2.imread('Pictures/shipsCropped.jpg')
height,width,c=back.shape

current=cv2.resize(curent,(width,height))



current_grey = cv2.cvtColor(current, cv2.COLOR_BGR2GRAY)
current_greyBH = cv2.equalizeHist(current_grey)
back_greyBH = cv2.GaussianBlur(back_greyBH, (7,7), 0)
current_greyBH = cv2.GaussianBlur(current_greyBH, (7, 7), 0)
cv2.imshow('back',back_greyBH)
cv2.imshow('current',current_greyBH)
difference = cv2.absdiff(back_greyBH, current_greyBH)
 #   _, difference = cv2.threshold(difference, 25, 255, cv2.THRESH_BINARY)

cv2.imshow('diff',difference)
kernel = np.ones((5,5), np.uint8)
img_binary = cv2.threshold(difference, 14,255, cv2.THRESH_BINARY)[1]
cv2.imshow('smth',img_binary)
erosion = cv2.erode(img_binary,kernel,iterations=2)
cv2.imshow('dif',erosion)
cv2.imwrite( "Pictures/erosion.jpg", erosion)
'''
cv2.imshow('final',img_binary)
kernel = np.ones((5,5), np.uint8)
erosion = cv2.erode(img_binary,kernel,iterations=2)
cv2.imshow('with erod',erosion)
dilation = cv2.dilate(erosion,kernel,iterations = 2)
cv2.imshow('withDil',dilation)
'''
def cvimage_to_pygame(image):
    """Convert cvimage into a pygame image"""
    return pygame.image.frombuffer(image.tostring(), image.shape[1::-1],
                                   "RGB")
def shape_positions(coord):


    cubeWidth = int(width / 10)
    cubeHeight = int(height / 10)
    print(str(width))
    print(height)
    print('Cube Width: ' + str(cubeWidth) + ' Cube Height: '+ str(cubeHeight))
    shapeXMin = coord[0][0]
    shapeYMin = coord[0][1]
    shapeXMax = coord[1][0]
    shapeYMax = coord[1][1]
    print(shapeXMin)
    print(shapeXMax)
    print(shapeYMin)
    print(shapeYMax)
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
    #print('STOP')
    while (yMin * cubeHeight) <= (shapeYMin) and yMin <= 10:
        print('YMIN')
        print(str(yMin * cubeHeight) + ' is smaller than ' + str(shapeYMin))
        shapeRowMin = yMin
        print(str(shapeRowMin))
        yMin += 1
    yMin=0
    #print('STOP')
    while (xMax * cubeWidth) >= shapeXMax  and xMax <= 10:
        print('XMAX')
        print(str(xMax * cubeWidth) + ' is bigger than ' + str(shapeXMax))
        shapeColumnMax = xMax
        print(str(shapeColumnMax))
        xMax -= 1
    xMax=0
    #print('STOP')
    while ((yMax * cubeHeight)) >= shapeYMax  and yMax <= 10:
        print('YMAX')
        print(str(yMax * cubeHeight) + ' is bigger than ' + str(shapeYMax))
        shapeRowMax = yMax
        print(str(shapeRowMax))
        yMax -= 1

    yMax=0
    #print('The shape starts on vertical line ' + str(shapeColumnMin) + ' and ends in vertical line ' + str(shapeColumnMax))
    #print('The shape starts on horizontal line ' + str(shapeRowMin) + ' and ends in horizontal line ' + str(shapeRowMax))
    #print('The shape is between rows ' + str(shapeRowMin) + ' and ' + str(shapeRowMax) + ' and between columns ' + str(shapeColumnMin) + ' and '+ str(shapeColumnMax))
    #print('The shape is between vertical lines ' + str(shapeRowMin)+ ' and '+ str(shapeRowMax) +' and column '+ str(shapeColumnMax))
    diffColumn=shapeColumnMax-shapeColumnMin
    diffRows=shapeRowMax-shapeRowMin
    if(diffColumn==0):
        shapeColumnMax=shapeColumnMax+1
    if(diffRows==0):
        shapeRowMax=shapeRowMax+1
    if(diffColumn>=2 and diffRows>=2):
        if(diffColumn>diffRows):
            shapeRowMax=shapeRowMax-1
        if(diffRows>diffColumn):
            shapeColumnMax=shapeColumnMax-1
    yield(shapeColumnMin,shapeColumnMax,shapeRowMin,shapeRowMax)
    print(str(shapeColumnMin) + ' ' + str(shapeColumnMax)+ ' '+str(shapeRowMin)+ ' '+str(shapeRowMax))
def shape_gridP(MinMax):
    Vmin = MinMax[0]
    Vmax = MinMax[1]
    Hmin = MinMax[2]
    Hmax = MinMax[3]
    positions=[]
    if Vmax - Vmin == 1:
        if Hmax - Hmin == 1:
            positions.append([Vmax,Hmin])
        else:
            for i in range(Hmin+1, Hmax+1):
                positions.append([Vmax,i])

    if Hmax - Hmin == 1:
        for j in range(Vmin+1, Vmax+1):
            positions.append([j,Hmax])
    return positions
def find_shapes(image):
    img = image
    blobs = extract_blobs(img)
    blobs2 = []
    h,w=img.shape
    y=h/10
    x=w/10

    for blob in blobs:
        print('before removing '+ str(len(blob)))
        min_value = blob[0]
        max_value = blob[-1]

        if max_value[1]-min_value[1] < x*5 and max_value[0]-min_value[0] < y*5 and len(blob)>((x-2)*(y-2)):
            blobs2.append(blob)
    for blob2 in blobs2:
        print('after removing '+str(len(blob2)))
    blobs3=coordinates(blobs2)
    for blob3 in blobs3:
        min_value = blob3[0]
        max_value = blob3[-1]
        yield (min_value, max_value)

for point in find_shapes(erosion):

    for MinMax in shape_positions(point):

        positions=shape_gridP(MinMax)
        print(positions)
cv2.waitKey(0)

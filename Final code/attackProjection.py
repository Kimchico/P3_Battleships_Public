import pygame
import cv2
from blob import extract_blobs
from detectShapePosition import *
from PlacementModule import *

fourblobs = cv2.imread("Final Pictures/fourblobs.png", 0)

def cvimage_to_pygame(image):
    """Convert cvimage into a pygame image"""
    return pygame.image.frombuffer(image.tostring(), image.shape[1::-1],
                                   "RGB")


def projectAttacks(surface, feed, player):
    dsurface=surface
    gridWidth = 32.6
    gridHeight = 32.6
    cols = 10
    rows = 10
    arr = [[0 for i in range(cols)] for j in range(rows)]
    for y in range(0,10):
        for x in range(0,10):
            arr[x][y] = feed[9-x][9-y]

    if player == 2:
        centerX = 895
        centerY = 391
        centerXp = 59
        centerYp = 367
        for i in range(0,10):
            for j in range(0,10):
                if feed[i][j] == 2:
                    x = j
                    y = 9- i
                    ccenterXp = centerXp + x * (gridWidth) + gridWidth/2
                    ccenterYp = centerYp + y * (gridHeight) + gridHeight/2

                    pygame.draw.circle(dsurface, (255,255,0), (int(ccenterXp), int(ccenterYp)), 3)
                if feed[i][j] == 3:
                    x = j
                    y = 9-i
                    ccenterXp = centerXp + x * (gridWidth) + gridWidth / 2
                    ccenterYp = centerYp + y * (gridHeight) + gridHeight / 2

                    pygame.draw.circle(dsurface, (255, 0, 0), (int(ccenterXp), int(ccenterYp)), 3)
        for i in range(0, 10):
            for j in range(0, 10):
                if arr[i][j] == 2:
                    x = j
                    y = 9 - i
                    ccenterX = centerX + x * (gridWidth) + gridWidth / 2
                    ccenterY = centerY + y * (gridHeight) + gridHeight / 2

                    pygame.draw.circle(dsurface, (255, 255, 0), (int(ccenterX), int(ccenterY)), 3)

                if arr[i][j] == 3:
                    x = j
                    y = 9-i
                    ccenterX = centerX + x * (gridWidth) + gridWidth / 2
                    ccenterY = centerY + y * (gridHeight) + gridHeight / 2

                    pygame.draw.circle(dsurface, (255, 0, 0), (int(ccenterX), int(ccenterY)), 3)
    if player == 1:
        centerX = 59
        centerY = 5
        centerXp = 893
        centerYp = 27
        for i in range(0, 10):
            for j in range(0, 10):
                if feed[i][j] == 2:
                    x = j
                    y = 9-i
                    ccenterXp = centerXp + x * (gridWidth) + gridWidth / 2
                    ccenterYp = centerYp + y * (gridHeight) + gridHeight / 2

                    pygame.draw.circle(dsurface, (255, 255, 0), (int(ccenterXp), int(ccenterYp)), 3)

                if feed[i][j] == 3:
                    x = j
                    y = 9-i
                    ccenterXp = centerXp + x * (gridWidth) + gridWidth / 2
                    ccenterYp = centerYp + y * (gridHeight) + gridHeight / 2

                    pygame.draw.circle(dsurface, (255, 0, 0), (int(ccenterXp), int(ccenterYp)), 3)
        for i in range(0, 10):
            for j in range(0, 10):
                if arr[i][j] == 2:
                    x = j
                    y = 9-i
                    ccenterX = centerX + x * (gridWidth) + gridWidth / 2
                    ccenterY = centerY + y * (gridHeight) + gridHeight / 2

                    pygame.draw.circle(dsurface, (255, 255, 0), (int(ccenterX), int(ccenterY)), 3)

                if arr[i][j] == 3:
                    x = j
                    y = 9-i
                    ccenterX = centerX + x * (gridWidth) + gridWidth / 2
                    ccenterY = centerY + y * (gridHeight) + gridHeight / 2

                    pygame.draw.circle(dsurface, (255, 0, 0), (int(ccenterX), int(ccenterY)), 3)

    pygame.display.update()

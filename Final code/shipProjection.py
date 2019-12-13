import pygame
import cv2
from blob import extract_blobs
from detectShapePosition import *

def projectShips(surface, ships, player):
    dsurface = surface
    gridWidth = 32.6
    gridHeight = 32.6
    if player == 2:
        centerX = 895
        centerY = 391
        for s in ships:
            positions = s.positions
            x = positions[0][0]
            y = positions[0][1]
            xf = positions[-1][0]
            yf = positions[-1][1]
            rectx = centerX + x * (gridWidth)
            recty = centerY + y * (gridHeight)
            if (y == yf):
                pygame.draw.rect(dsurface, (0, 0, 255),
                                 (rectx + 3, recty + 2, (gridWidth - 3) * (s.type), (gridHeight - 5)))
            if (x == xf):
                pygame.draw.rect(dsurface, (0, 0, 255),
                                 (rectx + 5, recty + 2, (gridWidth - 8), (gridHeight - 2) * (s.type)))
    if player == 1:
        centerX = 59
        centerY = 5
        for s in ships:
            positions = s.positions
            x = positions[0][0]
            y = positions[0][1]
            xf = positions[-1][0]
            yf = positions[-1][1]
            rectx = centerX + x * (gridWidth)
            recty = centerY + y * (gridHeight)
            if (y == yf):
                pygame.draw.rect(dsurface, (0, 0, 255),
                                 (rectx + 3, recty + 3.6, (gridWidth - 2) * (s.type), (gridHeight - 5)))
            if (x == xf):
                pygame.draw.rect(dsurface, (0, 0, 255),
                                 (rectx + 5, recty + 4, (gridWidth - 8), (gridHeight - 2) * (s.type)))
#project(grid)
#cv2.waitKey(0)
#cv2.destroyAllWindows()

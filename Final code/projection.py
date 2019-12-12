import pygame
import cv2
from blob import extract_blobs


fourblobs = cv2.imread("Pictures/fourblobs.png", 0)
grid = cv2.imread("Pictures/grid.png")

def project(image_to_crop,ships):
    # Find blob
    player1Placement = image_to_crop[7:499, 86:578]
    player2Placement = image_to_crop[582:1074, 1340:1832]
    w,h=image_to_crop.shape
    gridWidth = w/10
    gridHeight = h/10
    for s in ships:
        positions = s.positions
        x = positions[0][0]
        y = positions[0][1]
        rectx = x*gridWidth
        recty = x*gridHeight



    



project(grid)

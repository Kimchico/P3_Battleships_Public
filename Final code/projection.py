import pygame
import cv2
from blob import extract_blobs


fourblobs = cv2.imread("Pictures/fourblobs.png", 0)
grid = cv2.imread("Pictures/grid.png")




def project(image_to_crop):
    # Find blob

    binary_image = cv2.inRange(image_to_crop, 200, 255)

    image_blobs = extract_blobs(binary_image)

    #coordinates = []

    #for blob in image_blobs:
        #coordinates.append((blob[0], blob[-1]))


    player1Placement = image_to_crop[7:499, 86:578]
    player2Placement = image_to_crop[582:1074, 1340:1832]





project(grid)

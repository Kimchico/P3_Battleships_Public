import pygame
import cv2
from blob import extract_blobs
from detectShapePosition import *

#fourblobs = cv2.imread("Pictures/fourblobs.png", 0)
#grid = cv2.imread("Pictures/grid.png")

def project(image, surface, ships, player):
    # Find blob
    if player == 1:
        placement = image[7:499, 86:578]
    elif player == 2:
        placement = image[582:1074, 1340:1832]

    w, h = placement.shape
    gridWidth = w/10
    gridHeight = h/10
    for s in ships:
        positions = s.positions
        x = positions[0][0]
        y = positions[0][1]
        rectx = x*gridWidth
        recty = y*gridHeight
        pygame.draw.rect(placement, (0, 0, 255), (recty, rectx, gridWidth, gridHeight))

    if player == 1:
        surface.blit(placement, (7, 86))
    elif player == 2:
        surface.blit(placement, (582, 1340))

pygame.init()
image = pygame.image.load("Final Pictures/grid.png")
image = pygame.transform.scale(image, (1280,720))
display_surface = pygame.display.set_mode((1280, 720),pygame.FULLSCREEN)


pap1 = [[0 for i in range(cols)] for j in range(rows)]
p1ships = []

for shipPos in detectShapePosition(background_images[0], shapes[0], 30):
    PlaceShip(pap1, shipPos, p1ships)

state = True
while state:
    display_surface.blit(image, (0, 0))

    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            state = False

    pygame.display.update()

#project(grid)

import pygame
import cv2
from blob import extract_blobs
from detectShapePosition import *
from PlacementModule import *

fourblobs = cv2.imread("Final Pictures/fourblobs.png", 0)
#grid = cv2.imread("Pictures/grid.png")
#cv2.imshow("fa", fourblobs)

def cvimage_to_pygame(image):
    """Convert cvimage into a pygame image"""
    return pygame.image.frombuffer(image.tostring(), image.shape[1::-1],
                                   "RGB")

"""
def calibration(image_to_crop):
    # Blur image
    #blurred_image = cv2.cvtColor(image_to_crop, cv2.COLOR_BGR2GRAY)
    #blurred_image = cv2.GaussianBlur(image_to_crop, (21, 21), cv2.BORDER_DEFAULT)

    # Threshold and mask white
    #lower_white = np.array([90, 90, 90]); upper_white = np.array([255, 255, 255])

    binary_image = cv2.inRange(image_to_crop, 130, 255)
    #cv2.imshow("gray", blurred_image)
    #cv2.imshow("mask", binary_image)
    #cv2.imwrite("Pictures/blobs.jpg", binary_image)

    blobs = extract_blobs(binary_image)

    coordinates = []
    # Find blob

    for blob in blobs:
        coordinates.append((blob[0], blob[-1]))

    return coordinates
"""

def project(surface, ships, player):
    # Find blob
    #convert image to cv2.image
    image = cv2.imread("Final Pictures/grid.png")
    image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

    if player == 1:
        placement = image[6:405, 70:470]
        cv2.imwrite("Final Pictures/cropped.jpg", placement)
    elif player == 2:
        placement = image[473:873, 1090:1489]


    h, w, c = placement.shape
    gridWidth = w/10
    gridHeight = h/10

    placement = cvimage_to_pygame(placement)


    for s in ships:
        positions = s.positions
        x = positions[0][0]
        y = positions[0][1]
        rectx = x*gridWidth
        recty = y*gridHeight
        pygame.draw.rect(placement, (0, 0, 255), (recty, rectx, gridWidth, gridHeight))

    #placement = pygame.transform.scale(placement, (1280, 800))

    if player == 1:
        surface.blit(placement, (6, 70))
    elif player == 2:
        surface.blit(placement, (473, 1090))

rows, cols = (10, 10)
pygame.init()
image = pygame.image.load("Final Pictures/grid.png")
image = pygame.transform.scale(image, (1280, 800))
display_surface = pygame.display.set_mode((1280, 800), pygame.FULLSCREEN)

pap1 = [[0 for i in range(cols)] for j in range(rows)]
p1ships = []

for shipPos in detectShapePosition(cv2.imread("Pictures/Cropped_3.jpg"), cv2.imread("Pictures/shipsCropped_3.jpg"), 30):
    PlaceShip(pap1, shipPos, p1ships)

#print(calibration(fourblobs))

#project(display_surface, p1ships, 1)

state = True
while state:
    display_surface.blit(image, (0, 0))
    project(display_surface, p1ships, 1)
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            state = False

    pygame.display.update()

#project(grid)
#cv2.waitKey(0)
#cv2.destroyAllWindows()

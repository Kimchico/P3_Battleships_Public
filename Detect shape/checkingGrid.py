import sys, pygame, cv2, numpy as np
from pygame import Color

pygame.init()
image = cv2.imread('Pictures/picture_2.png')
imageRGB = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
height, width, channels = image.shape
size = width, height
screen = pygame.display.set_mode(size)
cubeWidth = width / 10
cubeHeight = height / 10
print(cubeWidth)
print(cubeHeight)
shapeXMin = 520
shapeYMin = 420
shapeXMax = 600
shapeYMax = 500
shapeRowMin = 0
shapeColumnMin = 0
shapeRowMax = 0
shapeColumnMax = 0
xMin = 1
xMax = 10
yMin = 1
yMax = 10


def cvimage_to_pygame(image):
    """Convert cvimage into a pygame image"""
    return pygame.image.frombuffer(image.tostring(), image.shape[1::-1],
                                   "RGB")


pyImage = cvimage_to_pygame(imageRGB)
screen.blit(pyImage, (0, 0))


while (xMin * cubeWidth) < shapeXMin and xMin <= 10:

    shapeColumnMin = xMin
    xMin += 1
while (yMin * cubeHeight) < shapeYMin and yMin <= 10:

    shapeRowMin = yMin
    yMin += 1
while (xMax * cubeWidth) > shapeXMax and xMax <= 10:

    shapeColumnMax = xMax
    xMax -= 1
while (yMax * cubeHeight) > shapeYMax and yMax <= 10:

    shapeRowMax = yMax
    yMax -= 1
print('The shape starts on column ' + str(shapeColumnMin) + ' and ends in column ' + str(shapeColumnMax))
print('The shape starts on row ' + str(shapeRowMin) + ' and ends in row ' + str(shapeRowMax))
while True:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

    pygame.display.flip()

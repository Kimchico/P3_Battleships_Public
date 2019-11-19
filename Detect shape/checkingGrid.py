import sys, pygame, cv2, numpy as np
from pygame import Color

pygame.init()
image = cv2.imread('Pictures/picture_3.png')
imageRGB = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
height, width, channels = image.shape
size = width, height
screen = pygame.display.set_mode(size)
cubeWidth = width / 10
cubeHeight = height / 10
print(cubeWidth)
print(cubeHeight)
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
def threshold_red(image):
    result = image.copy()
    image = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
    lower = np.array([155,25,0])
    upper = np.array([179,255,255])
    mask = cv2.inRange(image, lower, upper)
    #result = cv2.bitwise_and(result, result, mask=mask)
    return mask






def find_shapes(path_image: str):
    image = cv2.imread(path_image)
    binary_image = threshold_red(image)

    blobs = extract_blobs(binary_image)

    min_value = (0, 0)
    max_value = (0, 0)

    for blob in blobs:
        min_value = blob[0]
        max_value = blob[-1]

        yield (min_value, max_value)

for points in find_shapes('Pictures/picture_3.png'):
    shapeXMin = points[0][1]
    shapeYMin = points[0][0]
    shapeXMax = points[1][1]
    shapeYMax = points[1][0]
    print(str(shapeXMin)+' '+str(shapeXMax)+' '+str(shapeYMin)+' '+str(shapeYMax))

shapeRowMin = 0
shapeColumnMin = 0
shapeRowMax = 0
shapeColumnMax = 0
xMin = 0
xMax = 10
yMin = 0
yMax = 10


def cvimage_to_pygame(image):
    """Convert cvimage into a pygame image"""
    return pygame.image.frombuffer(image.tostring(), image.shape[1::-1],
                                   "RGB")


pyImage = cvimage_to_pygame(imageRGB)
screen.blit(pyImage, (0, 0))

for i in range(0,width,int(cubeWidth)):
    pygame.draw.line(screen, (255,0,0), (i,0), (i,width))
for j in range(0,height,int(cubeHeight)):
    pygame.draw.line(screen, (255,0,0), (0,j), (height,j))
while (xMin * cubeWidth) < (shapeXMin + 20) and xMin <= 10:
    print('XMIN')
    print(str(xMin * cubeWidth) + ' is smaller than ' + str(shapeXMin + 20))
    shapeColumnMin = xMin
    print(str(shapeColumnMin))
    xMin += 1
xMin=0
print('STOP')
while (yMin * cubeHeight) < (shapeYMin + 20) and yMin <= 10:
    print('YMIN')
    print(str(yMin * cubeHeight) + ' is smaller than ' + str(shapeYMin + 20))
    shapeRowMin = yMin
    print(str(shapeRowMin))
    yMin += 1
yMin=0
print('STOP')
while ((xMax * cubeWidth) + 20) > shapeXMax  and xMax <= 10:
    print('XMAX')
    print(str(xMax * cubeWidth) + ' is bigger than ' + str(shapeXMax))
    shapeColumnMax = xMax
    print(str(shapeColumnMax))
    xMax -= 1
xMax=0
print('STOP')
while ((yMax * cubeHeight) + 20) > shapeYMax  and yMax <= 10:
    print('YMAX')
    print(str(yMax * cubeHeight) + ' is bigger than ' + str(shapeYMax))
    shapeRowMax = yMax
    print(str(shapeRowMax))
    yMax -= 1

yMax=0
#print('The shape starts on vertical line ' + str(shapeColumnMin) + ' and ends in vertical line ' + str(shapeColumnMax))
#print('The shape starts on horizontal line ' + str(shapeRowMin) + ' and ends in horizontal line ' + str(shapeRowMax))
#print('The shape is between rows ' + str(shapeRowMin) + ' and ' + str(shapeRowMax) + ' and between columns ' + str(shapeColumnMin) + ' and '+ str(shapeColumnMax))
print('The shape is on row ' + str(shapeRowMax)+ ' and column '+ str(shapeColumnMax))
while True:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

    pygame.display.flip()

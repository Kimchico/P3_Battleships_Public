import sys, pygame, cv2, numpy as np
from pygame import Color



pygame.init()
#all_sizes.jpg
#size2_v1.jpg
#size2_v1_hor.jpg
#size2_v2.jpg
#size2_v2_hor.jpg
#Size_3_vertical.jpg
#Size_3_horizontal.jpg
#Size_4_horizontal.png
#Size__4_vertical.jpg
image = cv2.imread('Pictures/Circle_Hit.jpg')
imageRGB = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
image2 = cv2.imread('Pictures/Cropped.png')
height, width, channels = image.shape
size = width, height
print(size)
screen = pygame.display.set_mode(size)

# START OF BLOB EXTRACTION
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

def threshold_red(image,bmin,gmin,rmin,bmax,gmax,rmax):
    image = cv2.GaussianBlur(image, (5,5),cv2.BORDER_DEFAULT)
    #image_2 = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
    #lower = np.array([0, 0, 80]) FOR ACTUAL CROPPED PICTURE
    #upper = np.array([25, 20, 255])
    #lower = np.array([32,25,230]) FOR PHOTOSHOPED
    #upper = np.array([38,35,240])
    lower = np.array([bmin,gmin,rmin])
    upper = np.array([bmax,gmax,rmax])
    mask = cv2.inRange(image, lower, upper)
    return mask




def find_shapes(path_image: str,bmin,gmin,rmin,bmax,gmax,rmax):
    image = cv2.imread(path_image)
    binary_image = threshold_red(image,bmin,gmin,rmin,bmax,gmax,rmax)
    cv2.imshow("Display window", binary_image)
    blobs = extract_blobs(binary_image)

    min_value = (0, 0)
    max_value = (0, 0)

    for blob in blobs:
        min_value = blob[0]
        max_value = blob[-1]

        yield (min_value, max_value)
#END OF BLOB EXTRACTION

#CONVERTING CV IMAGE TO PYGAME IMAGE

def cvimage_to_pygame(image):
    """Convert cvimage into a pygame image"""
    return pygame.image.frombuffer(image.tostring(), image.shape[1::-1],
                                   "RGB")

#DETECTING THE LINES THAT CONTAIN SHIPS

def shape_positions(image,coord):

    height, width, channels = image.shape
    cubeWidth = width / 10
    cubeHeight = height / 10
    print('Cube Width: ' + str(cubeWidth) + ' Cube Height: '+ str(cubeHeight))
    shapeXMin = coord[0][1]
    shapeYMin = coord[0][0]
    shapeXMax = coord[1][1]
    shapeYMax = coord[1][0]

    shapeRowMin = 0
    shapeColumnMin = 0
    shapeRowMax = 0
    shapeColumnMax = 0
    xMin = 0
    xMax = 10
    yMin = 0
    yMax = 10


    for i in range(0,width,int(cubeWidth)):
        pygame.draw.line(screen, (0,0,0), (i,0), (i,width))
        #print('Printing I: '+ str(i)+' ')
    for j in range(0,height,int(cubeHeight)):
        pygame.draw.line(screen, (0,0,0), (0,j), (height,j))
        #print('Printing J: '+ str(i)+' ')
    while (xMin * cubeWidth) < (shapeXMin + 3) and xMin <= 10:
        #print('XMIN')
        #print(str(xMin * cubeWidth) + ' is smaller than ' + str(shapeXMin + 20))
        shapeColumnMin = xMin
        #print(str(shapeColumnMin))
        xMin += 1
    xMin=0
    #print('STOP')
    while (yMin * cubeHeight) < (shapeYMin + 3) and yMin <= 10:
        #print('YMIN')
        #print(str(yMin * cubeHeight) + ' is smaller than ' + str(shapeYMin + 20))
        shapeRowMin = yMin
        #print(str(shapeRowMin))
        yMin += 1
    yMin=0
    #print('STOP')
    while (xMax * cubeWidth) > shapeXMax  and xMax <= 10:
        #print('XMAX')
        #print(str(xMax * cubeWidth+3) + ' is bigger than ' + str(shapeXMax))
        shapeColumnMax = xMax
        #print(str(shapeColumnMax))
        xMax -= 1
    xMax=0
    #print('STOP')
    while ((yMax * cubeHeight) + 3) > shapeYMax  and yMax <= 10:
        #print('YMAX')
        #print(str(yMax * cubeHeight) + ' is bigger than ' + str(shapeYMax))
        shapeRowMax = yMax
        #print(str(shapeRowMax))
        yMax -= 1

    yMax=0
    #print('The shape starts on vertical line ' + str(shapeColumnMin) + ' and ends in vertical line ' + str(shapeColumnMax))
    #print('The shape starts on horizontal line ' + str(shapeRowMin) + ' and ends in horizontal line ' + str(shapeRowMax))
    #print('The shape is between rows ' + str(shapeRowMin) + ' and ' + str(shapeRowMax) + ' and between columns ' + str(shapeColumnMin) + ' and '+ str(shapeColumnMax))
    #print('The shape is between vertical lines ' + str(shapeRowMin)+ ' and '+ str(shapeRowMax) +' and column '+ str(shapeColumnMax))
    yield(shapeColumnMin,shapeColumnMax,shapeRowMin,shapeRowMax)
    print(str(shapeColumnMin) + ' ' + str(shapeColumnMax)+ ' '+str(shapeRowMin)+ ' '+str(shapeRowMax))

#CREATING THE ARRAY FOR THE PLACEMENT

rows, cols = (10,10)
placementArr = [[0 for i in range(cols)] for j in range(rows)]
attackArr = [[0 for i in range(cols)] for j in range(rows)]

#FUNCTION THAT WOULD MODIFY THE ARRAY ACCORDING TO THE SHAPES

def fill_array(MinMax,arr):
    Vmin = MinMax[0]
    Vmax = MinMax[1]
    Hmin = MinMax[2]
    Hmax = MinMax[3]
    if Vmax - Vmin == 1:
        if Hmax - Hmin == 1:
            arr[Hmin][Vmin] = 1
        else:
            for i in range(Hmin, Hmax):
                arr[i][Vmin] = 1

    if Hmax - Hmin == 1:
        for j in range(Vmin, Vmax):
            arr[Hmin][j] = 1


#FINDING THE POSITION OF EACH SHAPE RECURSIVLY AND CREATING THE ARRAY

for point in find_shapes('Pictures/Circle_Hit.jpg',32,25,230,38,35,240):

    for MinMax in shape_positions(image,point):

        fill_array(MinMax,attackArr)
for point2 in find_shapes('Pictures/Cropped.png',0, 0, 80,25, 20, 255):
    print(point2)
    for MinMax2 in shape_positions(image2,point2):

        fill_array(MinMax2,placementArr)

#PRINTING THE ARRAY< FOR DEBUGGING

for row in attackArr:
    print(row)
print('\n')
print('\n')
print('\n')
for row2 in placementArr:
    print(row2)
pyImage = cvimage_to_pygame(imageRGB)
screen.blit(pyImage, (0, 0))

while True:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

    pygame.display.flip()




import pygame
import cv2
def cvimage_to_pygame(image):
    """Convert cvimage into a pygame image"""
    return pygame.image.frombuffer(image.tostring(), image.shape[1::-1],
                                   "RGB")
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

image = cv2.imread('Pictures/erosion67237.jpg')
imageRGB = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

height, width, channels = image.shape
size = width, height
print(size)
screen = pygame.display.set_mode(size)
height, width, channels = image.shape
cubeWidth = int(width / 10)
cubeHeight = int(height / 10)
pyImage = cvimage_to_pygame(imageRGB)
screen.blit(pyImage, (0, 0))
print('Cube Width: ' + str(cubeWidth) + ' Cube Height: ' + str(cubeHeight))
for i in range(0, width, int(cubeWidth)):
    pygame.draw.line(screen, (255, 255, 255), (i, 0), (i, (10*cubeHeight)))
    print('I From: ' + '('+str(i)+','+str(0)+')' + ' to : (' + str(i)+','+ str(10*cubeHeight)+')')
for j in range(0, height, int(cubeHeight)):
    pygame.draw.line(screen, (255, 255, 255), (0, j), ((10*cubeWidth), j))
    print('J From: ' + '('+str(0)+','+str(j)+')' + ' to : (' + str((10*cubeWidth))+','+ str(j)+')')



while True:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

    pygame.display.flip()

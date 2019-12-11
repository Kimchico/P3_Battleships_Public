import numpy as np
import cv2
from blob import extract_blobs
from calibration import *
import pygame


pg1 = []; pg2 = []; ag1 = []; ag2 = [];
background_images = []; shapes = []
green = []; pink = []

def gridPositions(pg1, pg2, ag1, ag2):
    #pg1.append((positions[0][0][0][1], positions[0][0][1][1], positions[0][0][0][0], positions[0][0][1][0]))
    #pg2.append((positions[0][1][0][1], positions[0][1][1][1], positions[0][1][0][0], positions[0][1][1][0]))
    #ag1.append((positions[1][0][0][1], positions[0][0][1][1], positions[1][0][0][0], positions[0][1][1][0]))
    #ag2.append((positions[1][1][0][1], positions[1][1][1][1], positions[1][1][0][0], positions[1][1][1][0]))
    pg1.append((positions[0][0][0][1], positions[0][0][1][1], positions[0][0][0][0], positions[0][0][1][0]))
    pg2.append((positions[0][1][0][1], positions[0][1][1][1], positions[0][1][0][0], positions[0][1][1][0]))
    ag1.append((positions[1][0][0][1], positions[1][0][1][1], positions[1][0][0][0], positions[1][0][1][0]))
    ag2.append((positions[1][1][0][1], positions[1][1][1][1], positions[1][1][0][0], positions[1][1][1][0]))




def cropGrid(image, grid):
    cropped_image = image[grid[0][0]:grid[0][1], grid[0][2]:grid[0][3]]
    return cropped_image

video = cv2.VideoCapture(1)
video.set(cv2.CAP_PROP_AUTO_EXPOSURE, 0.25)
video.set(cv2.CAP_PROP_EXPOSURE, -3)
#video.set(cv2.CAP_PROP_FRAME_WIDTH, 1280);
#video.set(cv2.CAP_PROP_FRAME_HEIGHT, 720);
#video.set(3, 1920)
#video.set(4, 900)
#gridPositions(pg1, pg2, ag1, ag2)
gridPositions(ag2, ag1, pg1, pg2)





#cv2.namedWindow("window", cv2.WND_PROP_FULLSCREEN)
#cv2.setWindowProperty("window",cv2.WND_PROP_FULLSCREEN,cv2.WINDOW_FULLSCREEN)
#cv2.imshow("window", cv2.imread("Pictures/grid.png"))

image = pygame.image.load("Pictures/grid.png")
image = pygame.transform.scale(image, (1280,720))
display_surface = pygame.display.set_mode((1280, 720),pygame.FULLSCREEN)

state = True

os.system("say 'Press q to take an image without any shapes on then afterwards press e to take a picture with both mines and ships on'")

while state:
    display_surface.blit(image, (0, 0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
        if event.type == pygame.KEYDOWN:
            check, frame = video.read()
            if event.unicode == 'q':
                background_images.append(cropGrid(frame, pg1))
                background_images.append(cropGrid(frame, pg2))
                background_images.append(cropGrid(frame, ag1))
                background_images.append(cropGrid(frame, ag2))
            if event.unicode == 'e':
                shapes.append(cropGrid(frame, pg1))
                shapes.append(cropGrid(frame, pg2))
                shapes.append(cropGrid(frame, ag1))
                shapes.append(cropGrid(frame, ag2))
                state = False
    pygame.display.update()

"""
os.system("say 'Take image WITHOUT any shapes in'")
while True:
    check, frame = video.read()
    #cv2.imshow("Frame", frame)
    key = cv2.waitKey(1)
    if key == ord('q'):
        break
"""


#background_images.append(cropGrid(frame, pg1))
#background_images.append(cropGrid(frame, pg2))
#background_images.append(cropGrid(frame, ag1))
#background_images.append(cropGrid(frame, ag2))
"""
os.system("say 'Place your ships'")
while True:
    check, frame = video.read()
    #cv2.imshow("Frame", frame)
    key = cv2.waitKey(1)
    if key == ord('q'):
        break
"""
#shapes.append(cropGrid(frame, pg1))
#shapes.append(cropGrid(frame, pg2))
#shapes.append(cropGrid(frame, ag1))
#shapes.append(cropGrid(frame, ag2))

cv2.imwrite('Pictures/Cropped.jpg', background_images[0]) #player 1 placement without
cv2.imwrite('Pictures/shipsCropped.jpg', shapes[0]) # player 1 placement with shapes
cv2.imwrite("Pictures/Cropped_2.jpg", background_images[2]) # player 1 attack without
cv2.imwrite("Pictures/shipsCropped_2.jpg", shapes[2]) # player 1 attack without
cv2.imwrite('Pictures/Cropped_3.jpg', background_images[1]) # player 2 attack with
cv2.imwrite('Pictures/shipsCropped_3.jpg', shapes[1]) # player 2 attack with
cv2.imwrite("Pictures/Cropped_4.jpg", background_images[3]) # player 2 placement without
cv2.imwrite("Pictures/shipsCropped_4.jpg", shapes[3]) # player 2 placement with

'''
cv2.imshow("Player 1 placement grid without", background_images[0])
cv2.imshow("Player 2 placement grid without", background_images[1])
cv2.imshow("Player 1 attack grid without", background_images[2])
cv2.imshow("Player 2 attack grid without", background_images[3])

cv2.imshow("Player 1 placement grid", shapes[0])
cv2.imshow("Player 2 placement grid", shapes[1])
cv2.imshow("Player 1 attack grid", shapes[2])
cv2.imshow("Player 2 attack grid", shapes[3])
'''
video.release()
#cv2.waitKey(0)
cv2.destroyAllWindows()

from calibration import *
import pygame
from detectShapePosition import detectShapePosition
pg1 = []; pg2 = []; ag1 = []; ag2 = [];
background_images = []; shapes = []
green = []; pink = []

def cropGrid(image, grid):
    cropped_image = image[grid[0][0]:grid[0][1], grid[0][2]:grid[0][3]]
    return cropped_image
video = cv2.VideoCapture(1)
video.set(cv2.CAP_PROP_AUTO_EXPOSURE, 0.25)
video.set(cv2.CAP_PROP_EXPOSURE, -3)
image = pygame.image.load("Final Pictures/grid.png")
image = pygame.transform.scale(image, (1280,720))
display_surface = pygame.display.set_mode((1280, 720),pygame.FULLSCREEN)

state = True

os.system("say 'Press q first to get a background image, then press e in order to capture an image of the tested shape and detect it")
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
                detectShapePosition(background_images[0],pg1,30)
    pygame.display.update()

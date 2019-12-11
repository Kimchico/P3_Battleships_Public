# import pygame module in this program
import pygame
from pygame.locals import *

pygame.init()

image = pygame.image.load("FOURBLOBS.png")

window = pygame.display.set_mode((1920, 1080), pygame.FULLSCREEN)
pygame.display.set_caption('image')


while True:
    window.blit(image, (0, 0))
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            pygame.quit()
            quit()

        pygame.display.update()

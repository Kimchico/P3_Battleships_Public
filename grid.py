import sys, pygame
from pygame.locals import *
w = 600
h = 400
x = 20
y = 20



screen = pygame.display.set_mode((w,h))
pygame.draw.line(screen, (0, 200, 200), (x, y), (580, x), (1))
pygame.draw.line(screen, (0, 200, 200), (x, y), (x, 380), (1))

clock = pygame.time.Clock()

while 1:
    clock.tick(60)
    pygame.display.update()
    for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
                elif event.type == KEYDOWN and event.key == K_ESCAPE:
                    sys.exit()
    x+=20
    y+=20
    pygame.draw.line(screen, (0, 200, 200), (20, y), (580, x), (1))
    pygame.draw.line(screen, (0, 200, 200), (x, 20), (x, 380), (1))

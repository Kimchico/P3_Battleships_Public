import cv2
import numpy as np
from blob import extract_blobs
from calibration import *
from cropAndDetect import *
from detectShapePosition import *
from PlacementModule import *
from Ship import ship
import random
from attack import *
import pygame
import os
from shipProjection import projectShips
#from projection import project
from attackProjection import projectAttacks

pygame.init()
state = True
player1_turn = True; player2_turn = False
video = cv2.VideoCapture(1)
rows, cols = (10, 10)
shipsNr1 = 0; shipsNr2 = 0
amountOfShips1 = 0; amountOfShips2 = 0

#image = pygame.transform.scale(image, (1280,720))
#pygame.mouse.set_visible(False)
image = pygame.image.load("Final Pictures/grid.png")
image = pygame.transform.scale(image, (1280,720))
display_surface = pygame.display.set_mode((1280, 720),pygame.FULLSCREEN)

#window = pygame.display.set_mode((1920, 1080), pygame.FULLSCREEN)
pygame.display.set_caption('image')

## Setup phase
pap1 = [[0 for i in range(cols)] for j in range(rows)]; feed1 = [[0 for ii in range(cols)] for jj in range(rows)]; p1ships = [];
pap2 = [[0 for f in range(cols)] for s in range(rows)]; feed2 = [[0 for ff in range(cols)] for ss in range(rows)]; p2ships = [];

for shipPos in detectShapePosition(background_images[0], shapes[0], 30):
    PlaceShip(pap1, shipPos, p1ships)

for shipPos in detectShapePosition(background_images[1], shapes[1], 30):
    PlaceShip(pap2, shipPos, p2ships)

for s1 in p1ships:
    amountOfShips1 = amountOfShips1 +1
for s2 in p2ships:
    amountOfShips2 = amountOfShips2 +1



#insert projection code here
#project(image, display_surface, p1ships, 1)
#project(image, display_surface, p2ships, 2)




for minePos1 in detectShapePosition(background_images[2], shapes[2], 40):
    CheckMines(minePos1, pap2, feed1)

for minePos2 in detectShapePosition(background_images[3], shapes[3], 40):
    CheckMines(minePos2, pap1, feed2)



os.system("say 'Player 1 starts, attack!    '")

#state = True
desShip1 = 0
desShip2 = 0
while state:
    _, frame = video.read()
    display_surface.blit(image, (0, 0))
    projectShips(display_surface, p1ships, 1)
    projectShips(display_surface, p2ships, 2)
    projectAttacks(display_surface, feed1, 1)
    projectAttacks(display_surface, feed2, 2)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
        if event.type == pygame.KEYDOWN:
            if event.unicode == 'q':
                if (player1_turn == True and player2_turn == False):
                    for row in pap2:
                        print(row)
                    for attackCoord in detectShapePosition(background_images[2], cropGrid(frame, ag1), 30):
                        print("Player 1 attack cord")
                        print(attackCoord)

                        shot =  attack(attackCoord, feed1, pap2, p2ships)
                        projectAttacks(display_surface, feed1, 1)
                        print("feed 1")
                        for row in feed1:
                            print(row)
                    for s2 in p2ships:
                        s2.check_health()
                        if(s2.isDestroyed == True):
                            desShip2 = desShip2+1
                        print("deship2")
                        print(desShip2)

                        if amountOfShips2 == desShip2:
                            state = False
                        else:
                            desShip2 = 0

                        print(amountOfShips1)
                    if shot:
                        player1_turn = True
                        player2_turn = False
                    else:
                        player1_turn = False
                        player2_turn = True

            if event.unicode == 'e':
                if (player1_turn == False and player2_turn == True):
                    for row in pap1:
                        print(row)
                    for attackCoord in detectShapePosition(background_images[3], cropGrid(frame, ag2), 30):
                        print("Player 2 attack cord")
                        print(attackCoord)
                        shot = attack(attackCoord, feed2, pap1, p1ships)
                        projectAttacks(display_surface, feed2, 2)
                        print("feed 2")
                        for row in feed2:
                            print(row)

                    for s1 in p1ships:
                        s1.check_health()
                        if(s1.isDestroyed == True):
                            desShip1 = desShip1+1
                        print("deship1")
                        print(desShip1)

                        if amountOfShips1 == desShip1:
                            state = False
                        else:
                            desShip1 = 0
                        print(amountOfShips2)
                    if shot:
                        player1_turn = False
                        player2_turn = True
                    else:
                        player1_turn = True
                        player2_turn = False

            pygame.display.update()


    #pygame.display.flip()

print("PLAYER 1")
for row in pap1:
    print(row)

for s in p1ships:
    print(s.get_Type())

for row in feed1:
    print(row)

print("##############")

print("PLAYER 2")
for row in pap2:
    print(row)

for s in p2ships:
    print(s.get_Type())

for row in feed2:
    print(row)

"""
# Gameplay
while True:
    key = cv2.waitKey(0)

    # Player 1 turn
    if key == ord('q'):
"""
cv2.waitKey(0)
cv2.destroyAllWindows()

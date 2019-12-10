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
import keyboard

state = False
player1_turn = True; player2_turn = False
video = cv2.VideoCapture(1)
rows, cols = (10, 10)



## Setup phase
pap1 = [[0 for i in range(cols)] for j in range(rows)]; feed1 = [[0 for ii in range(cols)] for jj in range(rows)]; p1ships = [];
pap2 = [[0 for f in range(cols)] for s in range(rows)]; feed2 = [[0 for ff in range(cols)] for ss in range(rows)]; p2ships = [];

for shipPos in detectShapePosition(background_images[0], shapes[0], 30):
    PlaceShip(pap1, shipPos, p1ships)

for shipPos in detectShapePosition(background_images[1], shapes[1], 30):
    PlaceShip(pap2, shipPos, p2ships)


for minePos1 in detectShapePosition(background_images[2], shapes[2], 30):
    CheckMines(minePos1, pap2, feed1)

for minePos2 in detectShapePosition(background_images[3], shapes[3], 30):
    CheckMines(minePos2, pap1, feed2)

cv2.destroyAllWindows()

state = True

"""
while state:
    _, frame = video.read()
    cv2.imshow("frame", frame)
    key = cv2.waitKey(1)
    if key == ord('q'):
        if player1_turn and (player2_turn == False):
                for attackCoord in detectShapePosition(background_images[-1], cropGrid(frame, ag2), 14):
                    print("pap2")
                    for row in pap2:
                        print(row)
                    print("attack cord")
                    print(attackCoord)

                    print("p2ships")
                    for f in p2ships:
                        print(f.get_Type())

                    attack(attackCoord, feed1, pap2, p2ships)

                    print("feed1")
                    for row in feed1:
                        print(row)
"""

desShip1 = 0
desShip2 = 0
while state:
    _, frame = video.read()
    input("Player button 1")
    if (player1_turn == True and player2_turn == False):
        for row in pap2:
            print(row)
        for attackCoord in detectShapePosition(background_images[2], cropGrid(frame, ag1), 30):
            print("Player 1 attack cord")
            print(attackCoord)
            attack(attackCoord, feed1, pap2, p2ships)
            print("feed 1")
            for row in feed1:
                print(row)
        player1_turn = False
        player2_turn = True
    input("Player 2 button")
    if (player1_turn == False and player2_turn == True):
        for row in pap1:
            print(row)
        for attackCoord in detectShapePosition(background_images[3], cropGrid(frame, ag2), 30):
            print("Player 2 attack cord")
            print(attackCoord)
            attack(attackCoord, feed2, pap1, p1ships)
            print("feed 2")
            for row in feed2:
                print(row)
        player1_turn = True
        player2_turn = False
    for s1 in p1ships:
        if(s1.isDestroyed == True):
            desShip1 = desShip1+1
    if len(p1ships) == desShip1:
        state = False
    else:
        desShip1 = 0

    for s2 in p2ships:
        if(s2.isDestroyed == True):
            desShip2 = desShip2+1
    if len(p2ships) == desShip2:
        state = False
    else:
        desShip2 = 0

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

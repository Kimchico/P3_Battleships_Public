import cv2
import numpy as np
from blob import extract_blobs
from calibration import *
from cropAndDetect import *
from detectShapePosition import *
from PlacementModule import *
from Ship import ship

state = True
player1_pressed = False; player2_pressed = False
video = cv2.VideoCapture(1)
rows, cols = (10, 10)

pap1 = [[0 for i in range(cols)] for j in range(rows)]; feed1 = [[0 for ii in range(cols)] for jj in range(rows)]; p1ships = [];
pap2 = [[0 for f in range(cols)] for s in range(rows)]; feed2 = [[0 for ff in range(cols)] for ss in range(rows)]; p2ships = [];

for shipPos in detectShapePosition(background_images[0], background_images[0]):
    PlaceShip(pap1, shipPos, p1ships)

for minePos in detectShapePosition(background_images[-1], shapes[-1]):
    CheckMines(minePos, pap1, feed1)

for shipPos in detectShapePosition(background_images[2], shapes[2]):
    PlaceShip(pap2, shipPos, p2ships)

for minePos in detectShapePosition(background_images[1], shapes[1]):
    CheckMines(minePos, pap2, feed2)



"""
print("PLAYER 1")
for row in pap1:
    print(row)

for s in p1ships:
    print(s.get_Type())

for row in feed1:
    print(row)
"""


print("PLAYER 2")
for row in pap2:
    print(row)

for s in p2ships:
    print(s.get_Type())

for row in feed2:
    print(row)

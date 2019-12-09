import cv2
import numpy as np
from blob import extract_blobs
#from calibration import *
#from cropAndDetect import *
from detectShapePosition import *
from PlacementModule import *
from Ship import ship

state = True
player1_pressed = False; player2_pressed = False
video = cv2.VideoCapture(1)
rows, cols = (10, 10)

pap1 = [[0 for i in range(cols)] for j in range(rows)]
p1ships = []

for shipPos in detectShapePosition(cv2.imread("Pictures/Cropped.jpg"), cv2.imread("Pictures/shipsCropped.jpg")):
        PlaceShip(pap1, shipPos, p1ships)

for row in pap1:
    print(row)

for s in p1ships:
    print(s.get_Type())

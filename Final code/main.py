import cv2
import numpy as np
from blob import extract_blobs
from calibration import *
from cropAndDetect import *
from detectShapePositon import *

state = True
player1_pressed = False; player2_pressed = False
video = cv2.VideoCapture(1)
player1_ships = detectShapePositon(background_images[0], shapes[0])
player2_ships = detectShapePositon(background_images[1], shapes[1])

while state:
    _, frame = video.read()


    if player1_pressed and player2_pressed:


        #do some image segmentation on temp1_attack


        #do some image segmentation on temp2_attack

    # if player is dead:
        #break

    else: continue

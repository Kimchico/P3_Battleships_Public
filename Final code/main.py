import cv2
import numpy as np
from blob import extract_blobs
from calibration import *
from cropAndDetect import *

state = True
player1_pressed = False; player2_pressed = False
video = cv2.VideoCapture(1)

while state:
    _, frame = video.read()


    if player1_pressed:
        temp1_attack = cropGrid(frame, ag1)


        #do some image segmentation on temp1_attack

    elif player2_pressed:
        temp2_attack = cropGrid(frame, ag2)

        #do some image segmentation on temp2_attack

    # if player is dead:
        #break

    else: continue

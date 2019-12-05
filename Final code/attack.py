import cv2
import numpy as np
def attack(coord,feedArray,placementArray,shipsArray):
    a=coord[0]
    b=coord[1]
    for p in placementArray: #this might need to be modified
        if p[a][b]==1:
            feedArray[a][b]==2 #2 is shot and hit
        if p[a][b]==0:
            feedArray[a][b]==3 #3 is shot and missed
    for i in shipsArray:
        if i.isDestroyed == False:
            for j in i.positions:
                if j[0]==a and j[1]==b:
                    i.health=i.health-1

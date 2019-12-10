import cv2
import numpy as np
def attack(coord,feedArray,placementArray,shipsArray):
    x=coord[0][1]
    y=coord[0][0]
    #for p in placementArray: #this might need to be modified
    if placementArray[x][y]==1:
        feedArray[x][y]=2 #2 is shot and hit
    if placementArray[x][y]==0:
        feedArray[x][y]=3 #3 is shot and missed
    for i in shipsArray:
        if i.isDestroyed == False:
            for j in i.positions:
                if j[0]==x and j[1]==y:
                    i.health=i.health-1

import cv2
import numpy as np
import os

def attack(coord,feedArray,placementArray,shipsArray):
    print(coord)
    for c in coord:
        x = c[0]
        y = c[1]
        if y == 10:
            y = y - 1
        if x == 10:
            x = x - 1
        x = 9 - x
        y = 9 - y

        for i in shipsArray:
            if i.isDestroyed == False:
                for j in i.positions:
                    if j[0]==x and j[1]==y:
                        i.health=i.health-1

        #for p in placementArray: #this might need to be modified
        if placementArray[y][x]==1:
            feedArray[y][x]=2 #2 is shot and hit
            os.system("say 'You hit'")
            return True
        if placementArray[y][x]==0:
            feedArray[y][x]=3 #3 is shot and missed
            os.system("say 'You miss'")
            return False

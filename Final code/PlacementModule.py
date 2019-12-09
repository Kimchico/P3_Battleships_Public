from Ship import ship
import cv2
'''
rows, cols = (10, 10)

ShipArr = [[0 for i in range(cols)] for j in range(rows)]
shipArray=[]
coord=[[2,3],[2,4],[2,5]]
MineCoords=[[2,3],[2,8],[6,7]]
'''
def PlaceShip(placeArray,coord,shipArray):
    i=0
    for c in coord:
        x = c[0]
        y = c[1]
        placeArray[y][x] = 1
        i=i+1
    shipArray.append(ship(i,coord,i))

def CheckMines(MineCoords,placeArray,feedBackArr):
    Mx = MineCoords[0]
    My = MineCoords[1]
    if placeArray[Mx][My] == 0:
        feedBackArr[Mx][My] = 3
    if placeArray[Mx][My] == 1:
        feedBackArr[Mx][My] = 2
'''
PlaceShip(ShipArr,coord,shipArray)

for row in ShipArr:
    print(row)
print('\n')

CheckMines(MineCoords,ShipArr)

for s in shipArray:
    print(s.get_Type())
print('\n')

for row in ShipArr:
    print(row)
'''

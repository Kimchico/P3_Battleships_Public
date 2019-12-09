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
        placeArray[y][x]=1
        i=i+1
    shipArray.append(ship(i,coord,i))

def CheckMines(MineCoords,shipArray):
    NrOfMines=0
    for Mc in MineCoords:
        Mx = Mc[0]
        My = Mc[1]
        if shipArray[Mx][My] == 0:
            shipArray[Mx][My] = 3
        if shipArray[Mx][My] == 1:
            shipArray[Mx][My] = 2

        NrOfMines=NrOfMines+1
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

import numpy

array =([[ 0,  0,  0,  0,  0,  0,  0,  0,  0,  0],
        [ 0,  0,  0,  0,  0,  0,  0,  0,  0,  0],
        [ 0,  0,  0,  0,  0,  0,  0,  0,  0,  0],
        [ 0,  0,  0,  0,  0,  0,  0,  0,  0,  0],
        [ 0,  1,  0,  0,  0,  0,  0,  0,  0,  0],
        [ 0,  1,  0,  0,  0,  0,  0,  0,  0,  0],
        [ 0,  1,  0,  0,  0,  0,  0,  0,  0,  0],
        [ 0,  1,  0,  0,  0,  0,  0,  0,  0,  0],
        [ 0,  0,  0,  0,  0,  0,  0,  0,  0,  0],
        [ 0,  0,  0,  0,  0,  0,  0,  0,  0,  0],
         ])
coord=[1,4]
w, h = 10, 10
array2 = [[0 for x in range(w)] for y in range(h)]
for row in array:
        print(row)
for y in range(0,10):
        for x in range(0,10):
                if array[y][x]==1:
                        print('Shape fills space: ('+str(x)+','+str(y)+')')
array2 = list(zip(*array[::-1]))
print('Computer sees it')
for y in range(0,10):
        for x in range(0,10):
                if array2[y][x]==1:
                        print('Shape fills space: ('+str(x)+','+str(y)+')')
#for i in range(0,h):
     #   for j in range(0,w):
        #        print(array[i][j], end=' ')
        #print()
for row in array2:
        print(row)
for i in coord:
        print(i)
print(coord)
#coord2 = zip(*coord[::-1])
#print(coord2)
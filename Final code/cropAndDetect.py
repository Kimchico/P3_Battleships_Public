import numpy as np
import cv2
from blob import extract_blobs
from calibration import *


pg1 = []; pg2 = []; ag1 = []; ag2 = []
background_images = []; shapes = []


def gridPositions(pg1, pg2, ag1, ag2):
    pg1.append((positions[0][0][0][1], positions[0][0][1][1],  positions[0][0][0][0], positions[0][0][1][0]))
    pg2.append((positions[0][1][0][1], positions[0][1][1][1], positions[0][1][0][0], positions[0][1][1][0]))
    ag1.append((positions[1][0][0][1], positions[0][0][1][1], positions[1][0][0][0], positions[0][1][1][0]))
    ag2.append((positions[1][1][0][1], positions[1][1][1][1], positions[1][1][0][0], positions[1][1][1][0]))

def cropGrid(image, grid):
    cropped_image = image[grid[0][0]:grid[0][1], grid[0][2]:grid[0][3]]
    return cropped_image

video = cv2.VideoCapture(1)
#video.set(cv2.CAP_PROP_AUTO_EXPOSURE, 0.25)
#video.set(cv2.CAP_PROP_EXPOSURE, -3)
#video.set(cv2.CAP_PROP_FRAME_WIDTH, 1280);
#video.set(cv2.CAP_PROP_FRAME_HEIGHT, 720);
#video.set(3, 1920)
#video.set(4, 900)
gridPositions(pg1, pg2, ag1, ag2)


print("Take image WITHOUT any shapes in")
while True:
    check, frame = video.read()
    cv2.imshow("Frame", frame)
    key = cv2.waitKey(1)
    if key == ord('q'):
        break
cv2.destroyAllWindows()

background_images.append(cropGrid(frame, pg1))
background_images.append(cropGrid(frame, pg2))
background_images.append(cropGrid(frame, ag1))
background_images.append(cropGrid(frame, ag2))

print("Place ships")
while True:
    check, frame = video.read()
    cv2.imshow("Frame", frame)
    key = cv2.waitKey(1)
    if key == ord('q'):
        break

shapes.append(cropGrid(frame, pg1))
shapes.append(cropGrid(frame, pg2))
shapes.append(cropGrid(frame, ag1))
shapes.append(cropGrid(frame, ag2))

cv2.imshow("Player 1 placement grid without", background_images[0])
cv2.imwrite('Pictures/Cropped.jpg', background_images[0])
cv2.imshow("Player 2 placement grid without", background_images[1])
cv2.imshow("Player 1 attack grid without", background_images[2])
cv2.imshow("Player 2 attack grid without", background_images[3])

cv2.imshow("Player 1 placement grid", shapes[0])
cv2.imwrite('Pictures/shipsCropped.jpg',shapes[0])
cv2.imshow("Player 2 placement grid", shapes[1])
cv2.imshow("Player 1 attack grid", shapes[2])
cv2.imshow("Player 2 attack grid", shapes[3])


video.release()
cv2.waitKey(0)
cv2.destroyAllWindows()

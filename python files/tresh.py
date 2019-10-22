# Imports
import cv2
import numpy as np

# Converter (DOESNT WORK)
def convert(image):
    w , h, _ = image.shape
    for x in range(int(w)):
        for y in range(int(h)):
            newR = int(image[x, y][2]) / 255
            newG = int(image[x, y][1]) / 255
            newB = int(image[x, y][0]) / 255

            cMax = max(newR, newG, newB)
            cMin = min(newR, newG, newB)

            delta = cMax - cMin

            if cMax == cMin:
                h = 0

            elif cMax == newR:
                h = (60 * ((newG - newB) / delta) + 360) % 360

            elif cMax == newG:
                h = (60 * ((newB - newR) / delta) + 120) % 360

            elif cMax == newB:
                 h = (60 * ((newR - newG) / delta) + 240) % 360

            if cMax == 0:
                s = 0
            else:
                s = (delta / cMax) * 100

            v = cMax * 100
            image[x, y] = h, s, v

    return image

# Read the camera.
cap = cv2.VideoCapture(0)

# While loop that runs while true.
while(1):

    # Get camera feed.
    _, frame = cap.read()
    frame = cv2.GaussianBlur(frame, (5,5), cv2.BORDER_DEFAULT)

    # Convert the camera feed to HSV.
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    # Input thresholded color RGB value.
    green = np.uint8([[[0, 255, 0]]])

    # Convert that color to HSV.
    hsv_green = cv2.cvtColor(green, cv2.COLOR_BGR2HSV)

    # Set the upper and lower threshold with a offset that suits you.
    lower_green = np.array([71 - 30, 100, 100])
    upper_green = np.array([71 + 30, 255, 255])

    # Make a mask with the converted camera feed and the thresholded values.
    mask = cv2.inRange(hsv, lower_green, upper_green)

    # Show the frames (maybe use numpy.concatenate).
    cv2.imshow("Normal", frame)
    cv2.imshow("Thresh", mask)

    # Set variable k equal to keypressed.
    k = cv2.waitKey(1) & 0xFF

    # If the k variable is equal to q then quit the program.
    if k == ord('q'):
        break

# Delete all windows.
cv2.destroyAllWindows()

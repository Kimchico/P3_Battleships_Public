import cv2
import numpy as np
import PIL as IMAGE
import pygame;
#from blob import extract_blobs;

image = cv2.imread('C:/Users/David/Desktop/P3/v3.jpg', 0)

# inverting?
# cv2.imshow("Pic", image)
# inv = cv2.bitwise_not(image)
# ret, thresh1 = cv2.threshold(inv, 200, 255, cv2.THRESH_BINARY)
# cv2.imshow("trash", thresh1)
# end of invert

params = cv2.SimpleBlobDetector_Params()

params.filterByCircularity = True
params.minCircularity = 0.7
params.maxCircularity = 0.8

params.filterByArea = True
params.minArea = 900
params.maxArea = 1200

params.filterByInertia = False
params.minInertiaRatio = 0.01
params.maxInertiaRatio = 0.5


if cv2.__version__.startswith('2.'):
    detector = cv2.SimpleBlobDetector(params)
else:
    detector = cv2.SimpleBlobDetector_create(params)

# detector = cv2.SimpleBlobDetector()
keypoints = detector.detect(image)
im_with_keypoints = cv2.drawKeypoints(image, keypoints, np.array([]), (0,255,0), cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)

points_toCrop = []

for keypoint in keypoints:
    x = int(keypoint.pt[0])
    y = int(keypoint.pt[1])
    points_toCrop.append((x, y))

print(points_toCrop)

crop_img = image[points_toCrop[0][1]:points_toCrop[1][1], points_toCrop[0][0]:points_toCrop[1][0]]


#temp_image_PIL = IMAGE.fromarray(image)
#image_crop_PIL = temp_image_PIL.crop((100, 200, 300, 400))
#crop_img = np.asarray(image_crop_PIL)

cv2.imshow("cropped", crop_img)


cv2.imshow("Keypoints", im_with_keypoints)
cv2.waitKey()
cv2.destroyAllWindows()

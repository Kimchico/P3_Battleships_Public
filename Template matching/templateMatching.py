import cv2
import numpy as np

image = cv2.imread('/Users/mikkelsangmeebaunsgaard/Repositories/P3_Battleships_Public/Template matching/74889346_588703121892864_26878214576013312_n (1).png')
image_gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
template = cv2.imread('/Users/mikkelsangmeebaunsgaard/Repositories/P3_Battleships_Public/Template matching/Screenshot 2019-11-19 at 09.48.57.png',  0)
w, h = template.shape[: : -1]

res = cv2.matchTemplate(image_gray, template, cv2.TM_CCOEFF_NORMED)
threshold = 0.78

loc = np.where(res >= threshold)

for pt in zip(*loc[::-1]):
    cv2.rectangle(image, pt, (pt[0] + w, pt[1] + h), (0, 255, 255), 2)
    print(pt)


cv2.imshow('Detected', image)
cv2.waitKey(0)
cv2.destroyAllWindows()

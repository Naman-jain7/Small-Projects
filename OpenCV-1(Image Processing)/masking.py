import cv2 as cv
import numpy as np

img = cv.imread("Photos/cats 2.jpg")
blank = np.zeros(img.shape[:2], dtype="uint8") # size of mask same as that of image or it won't work

circular_mask = cv.circle(blank.copy(), (img.shape[1]//2 + 45, img.shape[0]//2), 100, 255, -1)
rectangular_mask = cv.rectangle(blank.copy(), (30,30), (370,370), 255, -1)
weird_mask = cv.bitwise_and(circular_mask, rectangular_mask)

masked = cv.bitwise_and(img, img, mask=circular_mask)
cv.imshow("Masked Image", masked)

cv.waitKey(0)
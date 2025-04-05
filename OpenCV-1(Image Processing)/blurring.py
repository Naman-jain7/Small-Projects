import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt

img = cv.imread("Photos/cats.jpg")

# Averaging : higher kernel size implies more blur
average = cv.blur(img, (3,3))
# cv.imshow("Average", average)

# Gaussian Blur: in basics. weighted towards the center

# Median Blur : not for higher kernel size. replaces each pixel's value with median value of surrounding pixels in kernel
median = cv.medianBlur(img, 3)
# cv.imshow("Median Blur",median)

# Bilateral Blur: used in facial image processing
bilateral = cv.bilateralFilter(img, 10, 15, 15)
cv.imshow("Bilateral", bilateral)

cv.waitKey(0)
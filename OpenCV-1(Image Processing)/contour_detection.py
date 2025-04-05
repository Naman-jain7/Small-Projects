import cv2 as cv
import numpy as np

img = cv.imread("Photos/cats.jpg")
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
blur = cv.GaussianBlur(gray, (5,5), cv.BORDER_DEFAULT)
canny = cv.Canny(blur, 125, 175)
blank = np.zeros(img.shape, dtype = 'uint8')

# Binarizing Image: either black or white
ret, thresh = cv.threshold(gray, 125, 255, cv.THRESH_BINARY)   # if intensity of pixel is < 125, it will be set to 0.
# cv.imshow("Thresh", thresh)

# Contour Detection: highlight boundaries by finding areas with significant intensity changes. used in object detection, motion tracking
contours, hierarchies = cv.findContours(thresh, cv.RETR_LIST, cv.CHAIN_APPROX_NONE)
# print(f"{len(contours)}")      # list of contours found. hierarchies represent relation b/w contours(like nested contour)


# Drawing Contours: -1 to draw all contours
cv.drawContours(blank, contours, -1, (0, 0, 255), thickness=1)
cv.imshow("Contours Drawn", blank)

cv.waitKey(0)
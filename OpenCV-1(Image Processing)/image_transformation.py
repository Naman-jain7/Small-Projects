import cv2 as cv
import numpy as np

img = cv.imread("Photos/park.jpg")

# Translation: negative x --> left and negative y --> up
def translate(img, x, y):
    transMat = np.float32([[1,0,x], [0,1,y]])
    dimensions = (img.shape[1], img.shape[0]) #ensuring that the translated image retains the same size as the original
    return cv.warpAffine(img, transMat, dimensions)

# translated = translate(img, 100, 100)
# cv.imshow("Translated", translated)

# Rotation
def rotate(img, angle, rotPoint=None):
    (height, width) = img.shape[:2]
    if rotPoint is None:
        rotPoint = (width//2, height//2)
    rotMat = cv.getRotationMatrix2D(rotPoint, angle, 0.5)
    dimensions=(width, height)
    return cv.warpAffine(img, rotMat, dimensions)

# rotated = rotate(img, 45)
# cv.imshow("Rotated", rotated)

# Resizing
# resized = cv.resize(img, (500,500), interpolation=cv.INTER_CUBIC)   # inter_area for shrinking and inter_cubic/inter_linear for enlarging
# cv.imshow("Resized", resized)

# Flipping
# flipped = cv.flip(img, -1)
# cv.imshow("Flipped", flipped)

cv.waitKey(0)
import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt

# HSV - hue(type of color(red, green, blue)), saturation(intensity of color), value(brightness)
# LAB - lightness(brightness), A(color spectrum from green to red), B(color spectrum from blue to yellow)
img = cv.imread("Photos/park.jpg")
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY) # cannot convert grayscale image to hsv directly. gray --> bgr --> hsv
blank = np.zeros(img.shape[:2], dtype = 'uint8')


# BGR to HSV
hsv = cv.cvtColor(img, cv.COLOR_BGR2HSV)
# cv.imshow("BGR-->HSV", hsv)
# HSV to BGR

# BGR to L*a*b
lab = cv.cvtColor(img, cv.COLOR_BGR2LAB)
# cv.imshow("BGR-->LAB", lab)
#LAB2BGR

# BGR to RGB
rgb = cv.cvtColor(img, cv.COLOR_BGR2RGB)
# cv.imshow("BGR-->RGB", rgb)
# plt.imshow(rgb)
# plt.show()


# COLOR CHANNELS
b,g,r = cv.split(img)                  # returns np array
blue = cv.merge([b, blank, blank])
green = cv.merge([blank, g, blank])
red = cv.merge([blank, blank, r])
# cv.imshow("Blue",blue)
# cv.imshow("Green",green)
# cv.imshow("Red",red)
# print(img.shape)
# print(b.shape)
# print(g.shape)
# print(r.shape)

# Merge Channels
merged = cv.merge([b,g,r])
cv.imshow("Merged image", merged)

cv.waitKey(0)
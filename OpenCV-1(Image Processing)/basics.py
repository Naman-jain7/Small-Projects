import cv2 as cv
import numpy as np

# Blank Image
blank = np.zeros((500,500,3),dtype='uint8')    # dtype of an img

# Paint the blank image: [up:down, left:right]
# blank[100:200, 200:800] = 0,255,0              # blank[:] for full image
# cv.imshow("Green",blank)

# Draw a line
# cv.line(blank, (0,0), (blank.shape[1]//2, blank.shape[0]//2), (16, 124, 65), thickness=3)
# cv.imshow("Line",blank)

# Draw a rectangle on blank image
# cv.rectangle(blank, (0,0), (blank.shape[1]//2, blank.shape[0]//2), (0,255,0), thickness=cv.FILLED)
# cv.imshow("Rectangle",blank)

# Draw a circle
# cv.circle(blank, (blank.shape[1]//2, blank.shape[0]//2), 40, (0,0,255), thickness=3)
# cv.imshow("Circle",blank)

# Put text
# cv.putText(blank, "Hello, my name is Naman Jain", (0,225), cv.FONT_HERSHEY_TRIPLEX, 0.8, (0,255,0), thickness=2)
# cv.imshow("Text",blank)

img = cv.imread("Photos/cat.jpg")
img2 = cv.imread("Photos/park.jpg")

# Converting to grayscale
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
# cv.imshow("Gray",gray)

# Gaussian Blur
blur = cv.GaussianBlur(img2, (3,3), cv.BORDER_DEFAULT)
# cv.imshow("Blur",blur)

# Edge Cascade: lower and upper threshold for edge gradient intensity.
canny = cv.Canny(img2, 125, 175)
blur_canny = cv.Canny(blur, 125, 175)
# cv.imshow("Canny Edges in Normal Image",canny)
# cv.imshow("Canny Edges in Blur image",blur_canny)

# Dilating the image: expanding edges of binary image. used for contour detection, fills gaps
dilated = cv.dilate(img, (7,7), iterations=3)
blur_canny_dilated = cv.dilate(blur_canny, (7,7), iterations=3)
# cv.imshow("Dilated",dilated)
# cv.imshow("Blur Canny Dilated",blur_canny_dilated)

# Eroding : opp of dilate. emphasizing the background, separating object
eroded = cv.erode(blur_canny_dilated, (7,7), iterations=3)
# cv.imshow("Eroded",eroded)

# Cropping
cropped = img2[50:200, 200:400]
# cv.imshow("Cropped", cropped)

cv.waitKey(0)
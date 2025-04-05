import cv2 as cv

# WORKFLOW : read images and convert to grayscale for haar_cascade --> load CascadeClassifier --> detect no. of faces --> draw rectangles around faces

img = cv.imread("Photos/lady.jpg")
img2 = cv.imread("Photos/group 1.jpg")
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
gray2 = cv.cvtColor(img2, cv.COLOR_BGR2GRAY)

haar_cascade = cv.CascadeClassifier("haar_face.xml")

faces_rect = haar_cascade.detectMultiScale(img2, scaleFactor=1.1, minNeighbors=1)   # returns np array
print(f"No. of faces found = {len(faces_rect)}")

for (x,y,w,h) in faces_rect:
    cv.rectangle(img2, (x,y), (x + w, y + h), (0,255,0), thickness=2)
cv.imshow("Detected Faces", img2)

cv.waitKey(0)
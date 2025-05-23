import numpy as np
import cv2 as cv

# WORKFLOW : load haar cascade, define list of people --> load the trained model --> load the image and convert to gray, detect face in it --> loop over detected faces --> mark region of interest and use the model to predict. draw rectangle and write its name

haar_cascade = cv.CascadeClassifier("haar_face.xml")
people = ["Ben Afflek", "Elton John", "Jerry Seinfield", "Madonna", "Mindy Kaling"]

face_recognizer = cv.face.LBPHFaceRecognizer_create()
face_recognizer.read("face_trained.yml")

img = cv.imread(r"D:\IP\language\4. python\OpenCV\val\Madonna\4.jpg")
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
faces_rect = haar_cascade.detectMultiScale(gray, 1.1, 4)

for (x,y,w,h) in faces_rect:
    faces_roi = gray[y:y+h, x:x+h]
    label, confidence = face_recognizer.predict(faces_roi)
    print(f"Label = {people[label]} with confidence of {confidence}")
    cv.putText(img, str(people[label]), (20,20), cv.FONT_HERSHEY_COMPLEX, 1.0, (0,255,0), thickness=2)
    cv.rectangle(img, (x,y), (x+w,y+h), (0,255,0), thickness=2)
cv.imshow("Detected Face", img)
cv.waitKey(0)
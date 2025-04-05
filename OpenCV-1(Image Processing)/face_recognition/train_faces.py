import os
import cv2 as cv
import numpy as np

#  WORKFLOW : add names of people in list --> load haar cascade --> create function to train --> convert data to numpy array to be compatible with face recognizer --> Create a Local Binary Pattern Histogram(LBPH) --> Train the recognizer and save model, data

# WORKFLOW OF FUNCTION : get person's folder's path and label person with index in people list --> Iterate over images of folder --> read images as numpy array and convert to grayscale --> detect face(s) --> for each face in an image, mark region of interest and store features and label
people = []
features = []
labels = []
dir = r"D:\IP\language\4. python\OpenCV\train"
for i in os.listdir(dir):
    people.append(i)               # names of subfolders in train

haar_cascade = cv.CascadeClassifier("haar_face.xml")

def create_train():
    for person in people:
        path = os.path.join(dir, person)    # train/ben
        label = people.index(person)
        
        for img in os.listdir(path):
            img_path = os.path.join(path, img)    # train/ben/img1
            img_array = cv.imread(img_path)
            gray = cv.cvtColor(img_array, cv.COLOR_BGR2GRAY)
            
            faces_rect = haar_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=4)
            
            for (x,y,w,h) in faces_rect:
                faces_roi = gray[y:y+h, x:x+w]          # roi: region of interest
                features.append(faces_roi)
                labels.append(label)
                
create_train()

features = np.array(features, dtype="object")
labels = np.array(labels)

face_recognizer = cv.face.LBPHFaceRecognizer_create()

face_recognizer.train(features, labels)
face_recognizer.save('face_trained.yml')
np.save('features.npy', features)
np.save('labels.npy', labels)
import cv2
import time
import mediapipe as mp
import HandDetectorClass as hdc
import numpy as np
import math
import os

finger_images = []
images = os.listdir(rf"fingers")     # list of all images
for img in images:
    im = cv2.imread(os.path.join("fingers",img))
    if im is not None:
        finger_images.append(im)

cap = cv2.VideoCapture(0)
detector = hdc.handDetector(detectionCon=0.7)
while True:
    success, img = cap.read()
    img = detector.findHands(img)
    lmList = detector.findPosition(img, draw=False)
    if lmList:
        fingers=[]
        
        # for thumb finger
        if lmList[detector.tipIds[0]][1] < lmList[detector.tipIds[0] - 1][1]:
            fingers.append(1)
        else:
            fingers.append(0)
            
        # for rest
        for i in range(1,5):
            if lmList[detector.tipIds[i]][2] < lmList[detector.tipIds[i] - 2][2]:   # higher tip means lower y value. -2 for clarity
                fingers.append(1)
            else:
                fingers.append(0)
        total_fingers = sum(fingers)
        
        if total_fingers == 0:
            finger_image = finger_images[5]
            finger_image_resized = cv2.resize(finger_image, (200, 200))
            img[10 : 10 + finger_image_resized.shape[0], 10 : 10 + finger_image_resized.shape[1]] = finger_image_resized
        else:
            finger_image = finger_images[total_fingers-1]
            finger_image_resized = cv2.resize(finger_image, (100, 100))
            img[10 : 10 + finger_image_resized.shape[0], 10 : 10 + finger_image_resized.shape[1]] = finger_image_resized
        cv2.putText(img, f"{total_fingers}", (40, 450), cv2.FONT_HERSHEY_COMPLEX, 1, (0,0,255), 3)
    
    cv2.imshow("Image", img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

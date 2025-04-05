import cv2 as cv
import mediapipe as mp
import time
import os
import HandDetectorClass as hdc
import numpy as np

brushThickness = 25
eraserThickness = 100
detector = hdc.handDetector(detectionCon=0.65, maxHands=1)
cap = cv.VideoCapture(0)

imgCanvas = np.zeros((720, 1280, 3), np.uint8)
while True:
    success, img = cap.read()
    img = detector.findHands(img)
    lmList = detector.findPosition(img, draw=False)
    cv.imshow("Image", img)
    
    x1, y1 = lmList[8][1:]
    x2, y2 = lmList[12][1:]
    
    if cv.waitKey(1) & 0xFF == ord('q'):
        break
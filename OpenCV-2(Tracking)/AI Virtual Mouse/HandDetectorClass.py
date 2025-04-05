import cv2 as cv
import mediapipe as mp
import time
import math

class handDetector():
    def __init__(self, mode=False, maxHands=2, detectionCon=0.5, trackCon=0.5):
        self.mode = mode
        self.maxHands = maxHands
        self.detectionCon = detectionCon
        self.trackCon = trackCon
        
        self.ptime = 0                           # for drawing landmarks and connections
        self.mpHands = mp.solutions.hands
        self.hands = self.mpHands.Hands(static_image_mode=self.mode, max_num_hands=self.maxHands,
                                        min_detection_confidence=self.detectionCon, min_tracking_confidence=self.trackCon)
        self.mpDraw = mp.solutions.drawing_utils
        self.tipIds = [4, 8, 12, 16, 20]

    def findHands(self, img, draw=True):
        imgRGB = cv.cvtColor(img, cv.COLOR_BGR2RGB)
        self.results = self.hands.process(imgRGB)    # save processed rgb image. self.results=object
        if self.results.multi_hand_landmarks:      # list of landmarks of each hand: landmark has x,y,z coordinates
            for handLms in self.results.multi_hand_landmarks:
                if draw:
                    self.mpDraw.draw_landmarks(img, handLms, self.mpHands.HAND_CONNECTIONS)
        return img

    def findPosition(self, img, draw=True):
        self.lmList = []                            # list of lists(id, x, y) of landmarks
        if self.results.multi_hand_landmarks:
            for handLms in self.results.multi_hand_landmarks:  # handLms=list of ojects
                for id, lm in enumerate(handLms.landmark):
                    h, w, c = img.shape
                    cx, cy = int(lm.x * w), int(lm.y * h) # lm contains normalized x,y,z coord. convert to pixel coordinates
                    self.lmList.append([id, cx, cy])
                    if draw:
                        cv.circle(img, (cx, cy), 5, (23, 160, 92), cv.FILLED)
        return self.lmList
    
    def findDistance(self, p1, p2, img, draw=True, r=8, t=3):
        x1, y1 = self.lmList[p1][1:]
        x2, y2 = self.lmList[p2][1:]
        
        if draw:
            cv.line(img, (x1,y1), (x2,y2), (255,0,255), t)
            cv.circle(img, (x1,y1), r, (255,0,255), cv.FILLED)
            cv.circle(img, (x2,y2), r, (255,0,255), cv.FILLED)
        length = math.hypot(x2-x1, y2-y1)
        return length, img, [x1,y1,x2,y2]
    
    def fingersUp(self):
        fingers = []
        if self.lmList[self.tipIds[0]][1] > self.lmList[self.tipIds[0] - 1][1]:
            fingers.append(1)
        else:
            fingers.append(0)
        
        for id in range(1,5):
            if self.lmList[self.tipIds[id]][2] < self.lmList[self.tipIds[id] - 2][2]:
                fingers.append(1)
            else:
                fingers.append(0)

        return fingers
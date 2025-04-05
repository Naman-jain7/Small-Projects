import cv2
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
        imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        self.results = self.hands.process(imgRGB)    # save processed rgb image. self.results=object
        if self.results.multi_hand_landmarks:      # list of landmarks of each hand: landmark has x,y,z coordinates
            for handLms in self.results.multi_hand_landmarks:
                if draw:
                    self.mpDraw.draw_landmarks(img, handLms, self.mpHands.HAND_CONNECTIONS)
        return img

    def findPosition(self, img, draw=True):
        lmList = []                            # list of lists(id, x, y) of landmarks
        if self.results.multi_hand_landmarks:
            for handLms in self.results.multi_hand_landmarks:  # handLms=list of ojects
                for id, lm in enumerate(handLms.landmark):
                    h, w, c = img.shape
                    cx, cy = int(lm.x * w), int(lm.y * h) # lm contains normalized x,y,z coord. convert to pixel coordinates
                    lmList.append([id, cx, cy])
                    if draw:
                        cv2.circle(img, (cx, cy), 5, (23, 160, 92), cv2.FILLED)
        return lmList
    
    def findFPS(self):
        ctime = time.time()
        if (ctime - self.ptime) > 0:
            fps = 1 / (ctime - self.ptime)
        else:
            fps = 0
        self.ptime = ctime
        return fps
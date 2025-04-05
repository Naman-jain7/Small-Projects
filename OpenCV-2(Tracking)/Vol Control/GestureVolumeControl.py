import cv2
import time
import mediapipe as mp
import numpy as np
import math
import HandDetectorClass as hdc
from ctypes import cast, POINTER
from comtypes import CLSCTX_ALL
from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume

cap = cv2.VideoCapture(0)
detector = hdc.handDetector(detectionCon=0.7)

devices = AudioUtilities.GetSpeakers()
interface = devices.Activate(IAudioEndpointVolume._iid_, CLSCTX_ALL, None)
volume = cast(interface, POINTER(IAudioEndpointVolume))
volRange = volume.GetVolumeRange()
minVol, maxVol = volRange[0], volRange[1]
vol = 0

while True:
    success, img = cap.read()
    img = detector.findHands(img)
    lmList = detector.findPosition(img, draw=False)
    
    if lmList:
        x1, y1 = lmList[4][1], lmList[4][2]
        x2, y2 = lmList[20][1], lmList[20][2]
        # cx, cy = (x1 + x2) // 2, (y1 + y2) // 2          # center of line joining two fingers
        cv2.circle(img, (x1, y1), 6, (0, 0, 255), cv2.FILLED)
        cv2.circle(img, (x2, y2), 6, (0, 0, 255), cv2.FILLED)
        # cv2.circle(img, (cx, cy), 10, (255, 0, 255), cv2.FILLED)
        cv2.line(img, (x1, y1), (x2, y2), (0, 0 , 255), 3)
        
        length = math.hypot(x2 - x1, y2 - y1)
        vol = np.interp(length, [50, 200], [minVol, maxVol])    # when val is 50, vol should be minimum
        volBar = np.interp(length, [50, 200], [400, 150])       # when vol is 0, height is 400.
        volPercent = np.interp(length, [50, 200], [0, 100])
        volume.SetMasterVolumeLevel(vol,None)
        cv2.rectangle(img, (50, 150), (85, 400), (255,0,0), 3)
        cv2.rectangle(img, (50, int(volBar)), (85, 400), (255,0,0), cv2.FILLED)
        cv2.putText(img, f"{int(volPercent)} %", (40, 450), cv2.FONT_HERSHEY_COMPLEX, 1, (255,0,0), 3)
        
    fps = detector.findFPS()
    cv2.putText(img, f'FPS: {int(fps)}', (10, 70), cv2.FONT_HERSHEY_PLAIN, 3, (255, 0, 255), 3)
    cv2.imshow("Image", img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
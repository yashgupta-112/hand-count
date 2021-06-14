import cv2
import mediapipe
import os
import time
import handtrackingmodule as htm

wCam ,hCam = 640 , 480

cap = cv2.VideoCapture(1)
cap.set(3,wCam)
cap.set(4,hCam)

detector = htm.handDetector(detectionCon = 0.75)
tipIds = [4,8,12,16,20]
while True:
    success , img = cap.read()
    img = detector.findHands(img)
    lmList =detector.findPosition(img,draw=False)
    if len(lmList) != 0:
        fingers = []
        if lmList[tipIds[0]][1] < lmList[tipIds[0]-1][1]:
                fingers.append(1)
        else:
            fingers.append(0)
    
        for id in range(1,5):
            if lmList[tipIds[id]][2] < lmList[tipIds[id]-2][2]:
                fingers.append(1)
            else:
                fingers.append(0)
        totalCount = fingers.count(1)
        print(totalCount)
        
    
    cv2.imshow("Img",img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
          break
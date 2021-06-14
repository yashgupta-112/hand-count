import cv2
import mediapipe
import os
import handtrackingmodule as htm
import handcountModule as hc
wCam ,hCam = 640 , 480

cap = cv2.VideoCapture(1)
cap.set(3,wCam)
cap.set(4,hCam)
detector = htm.handDetector(detectionCon = 0.5)
county = hc.Handcount()
tipIds = [4,8,12,16,20]
while True:
    success , img = cap.read()
    
    img = detector.findHands(img)
    lmList =detector.findPosition(img,draw=False)
    if len(lmList)!= 0:
        co = county.countFinger(lmList,tipIds)
        cv2.putText(img,f'Count : {int(co)}',(20,70),cv2.FONT_HERSHEY_SCRIPT_COMPLEX,2,(255,60,180),3)
                    
    cv2.imshow("Img",img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
          break
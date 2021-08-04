import cv2
import time
import os
import HandTrackingModule as htm
import serial

wCam, hCam = 640, 480

cap = cv2.VideoCapture(0)
cap.set(3, wCam)
cap.set(4, hCam)
pTime = 0

detector = htm.handDetector(detectionCon=0.75)

tipIds = [4, 8, 12, 16, 20]

while True:
    success, img = cap.read()

    img = detector.findHands(img)
    lmList = detector.findPosition(img, draw=False)
    # print(lmList)

    if len(lmList) != 0:
        fingers = []

        # thumb
        if lmList[tipIds[0]][1] > lmList[tipIds[0] - 1][1]:
            fingers.append(1)
        else:
            fingers.append(0)

        # fingers
        for id in range(1, 5):
            if lmList[tipIds[id]][2] < lmList[tipIds[id] - 2][2]:
                fingers.append(1)
            else:
                fingers.append(0)
        totalfingers = fingers.count(1)
        print(100 + totalfingers)
        print(totalfingers)

        cv2.rectangle(img, (20, 20), (170, 400 - 235), (0, 255, 0), cv2.FILLED, )
        cv2.putText(img, str(totalfingers), (45, 145), cv2.FONT_HERSHEY_PLAIN, 10, (255, 0, 0), 20)

    cTime = time.time()
    fps = 1 / (cTime - pTime)
    pTime = cTime

    cv2.putText(img, f'FPS: {int(fps)}', (400, 50), cv2.FONT_HERSHEY_PLAIN, 3, (0, 255, 0), 3)

    cv2.imshow("Feed", img)
    cv2.waitKey(1)
# ser1.close()

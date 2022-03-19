import cv2, time, mediapipe as mp
import HandTracking_module as htm

pTime = 0
cTime = 0
cap = cv2.VideoCapture(0)
detector = htm.HandDetector()

while True:
    success, img = cap.read()
    img = detector.findHands(img)
    lmList = detector.findPos(img)
    if len(lmList) != 0:
        print(lmList[4])

    cTime = time.time()
    fps = 1 / (cTime - pTime)
    pTime = cTime

    cv2.putText(
        img, str(int(fps)), (10, 40), cv2.FONT_HERSHEY_PLAIN, 2, (0, 100, 255), 2
    )

    cv2.imshow("Image", img)
    cv2.waitKey(1)

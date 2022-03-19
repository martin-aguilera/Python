import cv2, time, pyautogui
import numpy as np, HandTracking_module as htm

cap = cv2.VideoCapture(0)
wCam, hCam = 1280, 720
frameR = 150
smoothening = 1

pTime = 0
plocX, plocY = 0, 0
clocX, clocY = 0, 0

cap.set(3, wCam)
cap.set(4, hCam)
detector = htm.HandDetector(maxHands=1)
wScr, hScr = pyautogui.size()
# print(wScr, hScr)

while True:
    success, img = cap.read()
    img = cv2.flip(img, 1)
    img = detector.findHands(img)
    lmList, bbox = detector.findPos(img)
    cv2.rectangle(
        img, (frameR, frameR), (wCam - frameR, hCam - frameR), (255, 0, 255), 2
    )

    if len(lmList) != 0:
        x1, y1 = lmList[8][1:]
        x2, y2 = lmList[12][1:]
        fingers = detector.fingersUp()

        # print(fingers)
        x3 = np.interp(x1, (frameR, wCam - frameR), (0, wScr))
        y3 = np.interp(y1, (frameR, hCam - frameR), (0, hScr))
        clocX = plocX + (x3 - plocX) / smoothening
        clocY = plocY + (y3 - plocY) / smoothening

        # fingers[1] = Index finger (the mouse)
        if (
            fingers[1] == 1
            and fingers[0] == 0
            and fingers[2] == 0
            and fingers[3] == 0
            and fingers[4] == 0
        ):
            pyautogui.moveTo(clocX, clocY)
            cv2.circle(img, (x1, y1), 15, (255, 0, 255), cv2.FILLED)
            plocX, plocY = clocX, clocY

        # fingers[2] = Middle finger (index + middle = left click)
        elif (
            fingers[1] == 1
            and fingers[2] == 1
            and fingers[0] == 0
            and fingers[3] == 0
            and fingers[4] == 0
        ):
            length, img, lineInfo = detector.findDistance(8, 12, img)
            # print(length)
            if length < 80:
                cv2.circle(img, (lineInfo[4], lineInfo[5]), 15, (0, 255, 0), cv2.FILLED)
                pyautogui.leftClick()

        # fingers[4] = Pinky finger (index + pinky = right click)
        elif (
            fingers[4] == 1
            and fingers[1] == 1
            and fingers[0] == 0
            and fingers[2] == 0
            and fingers[3] == 0
        ):
            length, img, lineInfo = detector.findDistance(8, 20, img)
            if length < 90:
                cv2.circle(img, (lineInfo[4], lineInfo[5]), 15, (0, 255, 0), cv2.FILLED)
                pyautogui.rightClick()

    # cTime = time.time()
    # fps = 1/(cTime-pTime)
    # pTime = cTime
    # cv2.putText(img, str(int(fps)), (10,50), cv2.FONT_HERSHEY_PLAIN, 2, (255,0,0), 2)
    cv2.imshow("Image", img)
    cv2.waitKey(1)

# widthScr, heightScr = pyautogui.size() # Returns two integers, the width and height of the screen. (The primary monitor, in multi-monitor setups.)
# x2, x3 = pyautogui.position() # Returns two integers, the x and y of the mouse cursor's current position.
# pyautogui.moveTo(100, 150) # Move the mouse to the x, y coordinates 100, 150.
# pyautogui.click() # Click the mouse at its current location.
# pyautogui.click(200, 220) # Click the mouse at the x, y coordinates 200, 220.
# pyautogui.move(None, 10)  # Move mouse 10 pixels down, that is, move the mouse relative to its current position.
# pyautogui.doubleClick() # Double click the mouse at the
# pyautogui.moveTo(500, 500, duration=2, tween=#pyautogui.easeInOutQuad) # Use tweening/easing function to move mouse over 2 seconds.
# pyautogui.write('Hello world!', interval=0.25)  # Type with quarter-second pause in between each key.
# pyautogui.press('esc') # Simulate pressing the Escape key.
# pyautogui.keyDown('shift')
# pyautogui.write(['left', 'left', 'left', 'left', 'left', 'left'])
# pyautogui.keyUp('shift')
# pyautogui.hotkey('ctrl', 'c')

import cvzone.SerialModule
from cvzone.HandTrackingModule import HandDetector
import cv2

cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)
detector = HandDetector(maxHands=1, detectionCon=0.7)
mySerial = cvzone.SerialModule.SerialObject("COM7",9600,1)
while True:
# Get image frame
    success, img = cap.read()
# Find the hand and its landmarks
    img = detector.findHands(img) # with draw
#hands = detector.findHands(img, draw=False) # without draw

    lmList, bbox =detector.findPosition(img)
    if lmList:
        fingers = detector.fingersUp()
        print(fingers)
        mySerial.sendData(fingers)
    cv2.imshow("Image", img)

    if cv2.waitKey(1) == ord('q'):
        break
        cap.release()
        cv2.destroyAllWindows()
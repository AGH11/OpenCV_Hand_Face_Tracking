import cv2 as cv
import numpy as np
from cvzone.HandTrackingModule import HandDetector

# Initialize the camera capture
cap = cv.VideoCapture(0)

# Initialize the hand detector with specified parameters
detector = HandDetector(detectionCon=0.5, maxHands=2)

while True:
    # Read a frame from the camera
    rec, frame = cap.read()

    # Detect hands in the frame
    hands, frame = detector.findHands(frame)

    if hands:
        # Get the first detected hand and its landmark list
        hand1 = hands[0]
        lmlist1 = hand1['lmList']

        # Calculate the distance between two landmarks (4th and 8th in this case)
        length, info, frame = detector.findDistance(lmlist1[4][:-1], lmlist1[8][:-1], frame)
        print(length)
        
    # Show the frame with detected hands
    cv.imshow('frame', frame)

    # Check for the 'ESC' key (27) to exit the loop
    keyexit = cv.waitKey(5) & 0xFF
    if keyexit == 27:
        break

# Release the camera and close all OpenCV windows
cv.destroyAllWindows()
cap.release()

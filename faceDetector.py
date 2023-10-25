import numpy as np
import cv2 as cv
from cvzone.FaceDetectionModule import FaceDetector
from cvzone.FaceMeshModule import FaceMeshDetector

# Initialize the camera capture
cap = cv.VideoCapture(0)

# Initialize the face detector
detector = FaceDetector()

# Initialize the face mesh detector with a maximum of one face
meshdetector = FaceMeshDetector(maxFaces=1)

while True:
    # Read a frame from the camera
    rec, frame = cap.read()

    # Detect faces in the frame
    frame, bbox = detector.findFaces(frame)

    # Detect face mesh in the frame
    frame, faces = meshdetector.findFaceMesh(frame)

    if bbox:
        center = bbox[0]['center']
        # Uncomment the line below to draw a filled circle at the center of the detected face
        # cv.circle(frame, center, 5, (255, 0, 255), cv.FILLED)

    # Show the frame with detected faces and face mesh
    cv.imshow('frame', frame)

    # Check for the 'ESC' key (27) to exit the loop
    keyexit = cv.waitKey(5) & 0xFF
    if keyexit == 27:
        break

# Release the camera and close all OpenCV windows
cv.destroyAllWindows()
cap.release()

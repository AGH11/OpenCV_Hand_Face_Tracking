### HandGesture.py
This code is designed for hand gesture recognition using the OpenCV library. It captures video from the camera and uses the "cvzone" library for hand tracking. It identifies and tracks hands in the video feed and calculates the distance between specific landmarks on the hand, in this case, landmarks on the thumb and index finger. It then prints the distance to the console. The code continues running until the 'ESC' key is pressed, at which point it releases the camera and closes all OpenCV windows.

### faceDetector.py
This code is for face detection and face mesh tracking using OpenCV. It captures video from the camera and employs two separate modules from the "cvzone" library. The first module detects faces in the video feed, and if a face is found, it calculates the center of the detected face and can draw a filled circle at that center. The second module is responsible for detecting the face mesh. The code continues running until the 'ESC' key is pressed, after which it releases the camera and closes all OpenCV windows.

## 🌐 Sources
1. [OpenCV Python Tutorials](https://docs.opencv.org/master/d9/df8/tutorial_root.html)
2. [cvzone - Official Documentation](https://github.com/cvzone/cvzone)

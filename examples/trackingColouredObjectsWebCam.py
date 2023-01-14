#only shows blue objects from webcam
import cv2 as cv
import numpy as np
cap = cv.VideoCapture(0)
while cap.isOpened():
    # Take each frame
    _, frame = cap.read()
    # Convert BGR to HSV
    windowX = 1280
    windowY = 800
    hsv = cv.cvtColor(frame, cv.COLOR_BGR2HSV)
    # define range of blue color in HSV
    lower_blue = np.array([100,50,100])
    upper_blue = np.array([140,255,255])
    # Threshold the HSV image to get only blue colors
    mask = cv.inRange(hsv, lower_blue, upper_blue)
    # Bitwise-AND mask and original image
    frame = cv.bitwise_and(frame,frame, mask= mask)
    cv.namedWindow("Resized_frame", cv.WINDOW_NORMAL)
    cv.resizeWindow("Resized_frame", windowX, windowY)
    cv.imshow("Resized_frame",frame)
    k = cv.waitKey(5) & 0xFF
    if k == 27:
        break
cv.destroyAllWindows()
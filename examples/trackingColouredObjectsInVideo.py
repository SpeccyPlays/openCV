#shows white, yellow, and cyan objects in video
import cv2 as cv
import numpy as np
cap = cv.VideoCapture(r'C:\Users\ben\Documents\GitHub\openCV\examples\chuckie1.mp4')
#cap = cv.VideoCapture(0)
while cap.isOpened():
    # Take each frame
    _, frame = cap.read()
    # Convert BGR to HSV
    windowX = 400
    windowY = 300
    hsv = cv.cvtColor(frame, cv.COLOR_BGR2HSV)
    # define range of blue color in HSV
    lower_cyan = np.array([80,245,50])
    upper_cyan = np.array([100,255,255])
    lower_gold = np.array([20,50,50])
    upper_gold = np.array([40,255,255])
    lower_white = np.array([0,0,100])
    upper_white = np.array([10,0,255])
    # Threshold the HSV image to get only blue colors
    blue = cv.inRange(hsv, lower_cyan, upper_cyan)
    yellow = cv.inRange(hsv, lower_gold, upper_gold)
    white = cv.inRange(hsv, lower_white, upper_white)
    mask = cv.bitwise_or(cv.bitwise_or(blue, yellow), white)
    # Bitwise-AND mask and original image
    frame = cv.bitwise_and(frame,frame, mask= mask)
    cv.namedWindow("Resized_frame", cv.WINDOW_NORMAL)
    cv.resizeWindow("Resized_frame", windowX, windowY)
    cv.imshow("Resized_frame",frame)
    k = cv.waitKey(5) & 0xFF
    if k == 27:
        break
cv.destroyAllWindows()
#only shows blue objects from webcam
#take a background image first
#Take frame from webcam
#Make a mask of anything blue from webcam frame
#exclude this mask from background
#exclude everything that isn't blue from webcam frame
#combine background and new webcam frame
import cv2 as cv
import numpy as np
import pyautogui
cap = cv.VideoCapture(0)
pyautogui.alert(text='Take an empty background image', title='Take background photo', button='OK')
i, background_img = cap.read()
while cap.isOpened():
    # Take each frame
    _, frame = cap.read()
    # Convert BGR to HSV
    windowX = 1280
    windowY = 800
    hsv = cv.cvtColor(frame, cv.COLOR_BGR2HSV)
    # define range of blue color in HSV
    lower_blue = np.array([100,50,50])
    upper_blue = np.array([150,255,255])
    # Threshold the HSV image to get only blue colors
    mask = cv.inRange(hsv, lower_blue, upper_blue)
    # Invert mask for background image
    inverted_mask = cv.bitwise_not(mask)
    new_background_img = cv.bitwise_and(background_img, background_img, mask= inverted_mask)
    # Bitwise-AND mask and original image
    frame = cv.bitwise_and(frame,frame, mask= mask)
    #This next bit will everything masked out from background and masked in from frame from camera
    frame = cv.bitwise_or(new_background_img, frame)
    cv.namedWindow("Resized_frame", cv.WINDOW_NORMAL)
    cv.resizeWindow("Resized_frame", windowX, windowY)
    cv.imshow("Resized_frame",frame)
    k = cv.waitKey(5) & 0xFF
    if k == 27:
        break
cv.destroyAllWindows()
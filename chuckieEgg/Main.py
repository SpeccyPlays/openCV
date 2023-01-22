## Main
import pyautogui
import cv2 as cv
import numpy as np
import time
from windowcapture import WindowCapture
from pyautogui_functions import contestantsReady
from opencv_functions import *
from path_finding import *
#Colours for bounding squares (reminder it's BGR colours used for openCV)
yellow = (0, 255, 255)
blue = (255, 0, 0)
white = (255, 255, 255)
pink = (153, 51, 255)
green = (0, 255, 0)
#initialise windowcapture class
wincap = WindowCapture('Fuse')
cv.namedWindow("Resized_frame", cv.WINDOW_NORMAL)
wincap.set_foreground_window()
frame = wincap.get_screenshot()
frame_height, frame_width = frame.shape[:2]
cv.resizeWindow("Resized_frame", frame_width, frame_height)
while(1):
    frame = wincap.get_screenshot()
    for i in range(0, frame_width, 16):
        frame = cv.line(frame, (i, 0), (i, frame_height), blue)
    for i in range(0, frame_height, 16):
        frame = cv.line(frame, (0, i), (frame_width, i), blue)
    cv.imshow("Resized_frame",frame)
    k = cv.waitKey(5) & 0xFF
    if k == 27:
        break
cv.destroyAllWindows()
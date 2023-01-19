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
cv.resizeWindow("Resized_frame", 400, 300)
while(1):
    #img = pyautogui.screenshot(region=gameWindow)
    #frame = np.array(img)
    #frame = cv.cvtColor(frame, cv.COLOR_RGB2BGR)
    frame = wincap.get_screenshot()

    cv.imshow("Resized_frame",frame)
    k = cv.waitKey(5) & 0xFF
    if k == 27:
        break
cv.destroyAllWindows()
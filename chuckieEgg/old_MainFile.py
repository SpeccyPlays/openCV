### Main file ###
## Currently detecting all main elements of game and displaying in seperate window
## This is to help check my code. Visualisation window can be removed in future
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
#start game and return tuple containing location of game window
gameWindow = contestantsReady()
wincap = WindowCapture('Fuse')
#OpenCV is better at finding objects compared to pyautoGUI so these lines not included
#egg_locations = locate_multiple_objects('egg.PNG', gameWindow)
#playerLocation = locate_one_object('player.PNG', gameWindow)

#set up our display window so it doesn't overlap with Fuse window
#x, y, width, height = gameWindow
#monitor_window_x = int(width/4)
#monitor_window_y = int(height/4)
#cv.namedWindow("Resized_frame", cv.WINDOW_NORMAL)
#cv.resizeWindow("Resized_frame", monitor_window_x, monitor_window_y)
#cv.moveWindow("Resized_frame", x + width, y)
static_items_check = False
while(1):
    #img = pyautogui.screenshot(region=gameWindow)
    #frame = np.array(img)
    #frame = cv.cvtColor(frame, cv.COLOR_RGB2BGR)
    frame = wincap.get_screenshot()
    #OpenCV is better at finding objects compared to pyautoGUI
    frame, egg_locations = locate_multiple_objects_cv('egg.PNG', frame, white)
    frame, chickenl_locations = locate_multiple_objects_cv('chickenl.PNG', frame, blue)
    frame, chuckenr_locations = locate_multiple_objects_cv('chickenr.PNG', frame, blue)
    frame, player_location = locate_one_object_cv('player.PNG', frame, yellow)
    if not static_items_check:
        #only need to check static items once
        frame, whocares = locate_multiple_objects_cv('ladder.PNG', frame, pink)
        frame, whocares = locate_multiple_objects_cv('brick.PNG', frame, green)
        static_items_check = True
    frame, location = find_closest_item(frame, egg_locations, player_location, white)
    print('Closest egg is ',  location)
    # Convert BGR to HSV - only used if we want to isolate colours and display them
#   hsv = cv.cvtColor(frame, cv.COLOR_BGR2HSV)
    # define range of blue color in HSV
#   lower_cyan = np.array([80,245,50])
#    upper_cyan = np.array([100,255,255])
#    lower_gold = np.array([20,50,50])
#    upper_gold = np.array([40,255,255])
#    lower_white = np.array([0,0,100])
#    upper_white = np.array([10,0,255])
    # Threshold the HSV image to get only blue colors
#    blue = cv.inRange(hsv, lower_cyan, upper_cyan)
#    yellow = cv.inRange(hsv, lower_gold, upper_gold)
#    white = cv.inRange(hsv, lower_white, upper_white)
#    mask = cv.bitwise_or(cv.bitwise_or(blue, yellow), white)
    # Bitwise-AND mask and original image
#    frame = cv.bitwise_and(frame,frame, mask= mask)
    cv.imshow("Resized_frame",frame)
    k = cv.waitKey(5) & 0xFF
    if k == 27:
        break
cv.destroyAllWindows()
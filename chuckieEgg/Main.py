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
#setup opencv monitor window sizes
cv.namedWindow("Resized_frame", cv.WINDOW_NORMAL)
wincap.set_foreground_window()
frame = wincap.get_screenshot()
frame_height, frame_width = frame.shape[:2]
cv.resizeWindow("Resized_frame", frame_width, frame_height)
#set up so we can store locations of objects in an array for path finding later
tile_size = 16
tiles_wide = int(frame_width/tile_size)
tiles_high = int(frame_height/tile_size)
object_locations_array = [[0]*tiles_wide]*tiles_high
#print('This many tiles wide : ', tiles_wide, ' This many tiles high : ', tiles_high)
while(1):
    frame = wincap.get_screenshot()
    #draw a grid to show 8x8 tile layout
    for i in range(0, frame_width, tile_size):
        frame = cv.line(frame, (i, 0), (i, frame_height), blue)
    for i in range(0, frame_height, tile_size):
        frame = cv.line(frame, (0, i), (frame_width, i), blue)
    cv.imshow("Resized_frame",frame)
    k = cv.waitKey(5) & 0xFF
    if k == 27:
        break
cv.destroyAllWindows()
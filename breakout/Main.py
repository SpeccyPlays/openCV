## Main
import pyautogui
import cv2 as cv
import numpy as np
import time
from windowcapture import WindowCapture
from opencv_functions import *
import win32gui, win32ui, win32con
pyautogui.PAUSE = 0.1
pyautogui.FAILSAFE = True
#Colours for bounding squares (reminder it's BGR colours used for openCV)
yellow = (0, 255, 255)
blue = (255, 0, 0)
white = (255, 255, 255)
pink = (153, 51, 255)
green = (0, 255, 0)
#initialise windowcapture class
wincap = WindowCapture('Fuse')
cv.namedWindow("Resized_frame", cv.WINDOW_NORMAL)
cv.resizeWindow("Resized_frame", 200, 100)
key_left = 'c'
key_right = 'm'
wincap.set_foreground_window()
while(1):
    frame = wincap.get_screenshot()
    frame, ball_loc = locate_one_object_cv('ball2.PNG', frame, pink)
    frame, paddle_loc = locate_one_object_cv('paddle2.PNG', frame, green)
    cv.imshow("Resized_frame",frame)
    ball_x, ball_y = ball_loc
    paddle_x, paddle_y = paddle_loc
    #print ('Ball location : ', ball_x, ',', ball_y)
    #print ('Paddle location : ', paddle_x, ',', paddle_y)
    if int(paddle_x) < int(ball_x):
        pyautogui.keyUp(key_left)
        pyautogui.keyDown(key_right)
    if int(paddle_x) > int(ball_x):
        pyautogui.keyUp(key_right)
        pyautogui.keyDown(key_left)  
    k = cv.waitKey(5) & 0xFF
    if k == 27:#ESC key to break
        break
cv.destroyAllWindows()
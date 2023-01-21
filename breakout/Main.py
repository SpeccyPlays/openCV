## Main
import pyautogui
import cv2 as cv
import numpy as np
from windowcapture import WindowCapture
from opencv_functions import *
import win32gui, win32ui, win32con
pyautogui.PAUSE = 0.02
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
cv.resizeWindow("Resized_frame", 300, 200)
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
    #Change the plus and minus value - lower means more twitchy but can get to the ball quick enough
    if int(ball_x) > (int(paddle_x) + 2):
        pyautogui.keyUp(key_left)
        pyautogui.keyDown(key_right)
    if int(ball_x) < (int(paddle_x) - 2):
        pyautogui.keyUp(key_right)
        pyautogui.keyDown(key_left)  
    k = cv.waitKey(5) & 0xFF
    if k == 27:#ESC key to break
        break
cv.destroyAllWindows()
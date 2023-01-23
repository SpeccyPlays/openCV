## Main
import pyautogui
import cv2 as cv
import numpy as np
from windowcapture import WindowCapture
from opencv_functions import *
import win32gui, win32ui, win32con
pyautogui.PAUSE = 0.01
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
#game keys
key_left = 'c'
key_right = 'm'
#use these for how much difference in the paddle movements
min_offset = 2
max_offset = 4
wincap.set_foreground_window()
while(1):
    frame = wincap.get_screenshot()
    frame, ball_loc = locate_one_object_cv('ball2.PNG', frame, pink)
    frame, paddle_loc = locate_one_object_cv('paddle2.PNG', frame, green)
    cv.imshow("Resized_frame",frame)
    ball_x, ball_y = ball_loc
    paddle_x, paddle_y = paddle_loc
    ball_x = int(ball_x) # we're going to be using this a lot so better to only convert to int once
    paddle_x = int(paddle_x)
    #if it's far from the paddle, hold the key down. If it's closer, a quick nudge across
    if ball_x > (paddle_x + max_offset):
        pyautogui.keyUp(key_left)#otherwise it's pressing both direction keys at once
        pyautogui.keyDown(key_right)
    elif ball_x > (paddle_x + min_offset) and (ball_x < paddle_x + max_offset):
        pyautogui.keyUp(key_left)
        pyautogui.keyDown(key_right)
        pyautogui.keyUp(key_right)
    if ball_x < (paddle_x - max_offset):
        pyautogui.keyUp(key_right)
        pyautogui.keyDown(key_left)
    elif  ball_x < (paddle_x + min_offset) and (ball_x > paddle_x - max_offset):
        pyautogui.keyUp(key_right)
        pyautogui.keyDown(key_left)
        pyautogui.keyUp(key_left)
    k = cv.waitKey(5) & 0xFF
    if k == 27:#ESC key to break
        break
cv.destroyAllWindows()
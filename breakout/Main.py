## Main
import pyautogui
import cv2 as cv
import numpy as np
import math as math
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
current_key = ''
#use these for how much difference in the paddle movements
min_offset = 1
max_offset = 5
height_offset = 60
wincap.set_foreground_window()
old_ball_loc = 0, 0
predicted_ball_x = 0
predicted_ball_y = 0
while(1):
    frame = wincap.get_screenshot()
    frame, ball_loc = locate_one_object_cv('ball2.PNG', frame, white)
    frame, paddle_loc = locate_one_object_cv('paddle2.PNG', frame, green)
    ball_x, ball_y = ball_loc
    paddle_x, paddle_y = paddle_loc
    ball_x = int(ball_x)
    paddle_x = int(paddle_x)
    
    old_ball_x, old_ball_y = old_ball_loc
    x_diff = (ball_x - old_ball_x) * 2
    y_diff = (ball_y - old_ball_y) * 2
    predicted_ball_x = ball_x + x_diff
    predicted_ball_y = ball_y + y_diff
    #draw a box around the prediction
    top_left = (predicted_ball_x, predicted_ball_y)
    bottom_right = (predicted_ball_x + 8,  predicted_ball_y + 8)
    frame = cv.rectangle(frame, top_left, bottom_right, pink, 2)
    cv.imshow("Resized_frame",frame)
    if predicted_ball_x > (paddle_x + min_offset):
        if current_key != key_right:
        #otherwise it's pressing both direction keys at once
            pyautogui.keyUp(key_left)
            pyautogui.keyDown(key_right)
            current_key = key_right
            print('change right')
    elif predicted_ball_x < (paddle_x - min_offset) :
        if current_key != key_left:
            pyautogui.keyUp(key_right)
            pyautogui.keyDown(key_left)
            print('change left')
            current_key = key_left
    print(current_key, ' Predicted x ', predicted_ball_x, 'Paddle x : ', paddle_x)
    old_ball_loc = ball_x, ball_y
    k = cv.waitKey(5) & 0xFF
    
    if k == 27:#ESC key to break
        break
pyautogui.keyUp(key_right)
pyautogui.keyUp(key_left)
cv.destroyAllWindows()
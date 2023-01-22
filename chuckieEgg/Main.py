## Main
import pyautogui
import cv2 as cv
import numpy as np
import time
from windowcapture import WindowCapture
from pyautogui_functions import *#contestantsReady
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
frame_height, frame_width = frame.shape[:2]#doesn't include last item which is alpha channel
cv.resizeWindow("Resized_frame", frame_width, frame_height)
#set up so we can store locations of objects in an array for path finding later
tile_size = 16
tiles_wide = int(frame_width/tile_size)
tiles_high = int(frame_height/tile_size)
object_locations_array = [[0 for i in range(tiles_wide)] for j in range(tiles_high)] #why are you like this python
#object_locations_array = [[0]*tiles_wide]*tiles_high
level_read = False
frame, egg_locations = locate_multiple_objects_cv('egg.PNG', frame, yellow)
#Below will stay in the loop until eggs show - means the level has started
#we'll need to fill our location array next
while not egg_locations:
    frame = wincap.get_screenshot()
    frame, egg_locations = locate_multiple_objects_cv('egg.PNG', frame, white)
    cv.imshow("Resized_frame",frame)
    if check_should_exit():
        break
object_locations_array = put_objects_in_array(object_locations_array, egg_locations, tile_size, 1)
while(1):
    frame = wincap.get_screenshot()
    if not level_read:
        #we only need to read these items once as they won't change
        frame, brick_locations = locate_multiple_objects_cv('brick.PNG', frame, green)
        frame, ladder_locations = locate_multiple_objects_cv('ladder.PNG', frame, pink)
        object_locations_array = put_objects_in_array(object_locations_array, brick_locations, tile_size, 2)
        object_locations_array = put_objects_in_array(object_locations_array, ladder_locations, tile_size, 3)
        for i in object_locations_array:
            print(i)
        print('Level read')
        level_read = True
    frame, egg_locations = locate_multiple_objects_cv('egg.PNG', frame, white)
    frame, player_location = locate_multiple_objects_cv('player.PNG', frame, yellow)
    #draw a grid to show tile layout
    for i in range(0, frame_width, tile_size):
        frame = cv.line(frame, (i, 0), (i, frame_height), blue)
    for i in range(0, frame_height, tile_size):
        frame = cv.line(frame, (0, i), (frame_width, i), blue)
    cv.imshow("Resized_frame",frame)
    if check_should_exit():
        break
    print(object_locations_array)

cv.destroyAllWindows()
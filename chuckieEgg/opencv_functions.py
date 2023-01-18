import cv2 as cv
import numpy as np
def locate_one_object_cv(filename, img):
    #copied straight off the docs page
    img_gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
    template = cv.imread(filename,0)
    w, h = template.shape[::-1]
    res = cv.matchTemplate(img_gray,template,cv.TM_CCOEFF)
    min_val, max_val, min_loc, max_loc = cv.minMaxLoc(res)
    top_left = max_loc
    bottom_right = (top_left[0] + w, top_left[1] + h)
    cv.rectangle(img,top_left, bottom_right, 255, 2)
    return img

def locate_multiple_objects_cv(filename, img):
    #copied off the docs page with minor edits
    img_gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
    template = cv.imread(filename, 0)
    w, h = template.shape[::-1]
    res = cv.matchTemplate(img_gray,template,cv.TM_CCOEFF_NORMED)
    threshold = 0.8
    loc = np.where( res >= threshold)
    for pt in zip(*loc[::-1]):
        cv.rectangle(img, pt, (pt[0] + w, pt[1] + h), (0,0,255), 2)
    return img

def loop_list_and_draw_rectangles(img, the_list):
    for item in the_list:
        draw_rectangles(img, item)

def draw_rectangles(img, item_to_draw):
    top_left_x, top_left_y, width, height = item_to_draw
    cv.rectangle(img,(top_left_x, top_left_y),(top_left_x + width, top_left_y + height),(255,255,255),3)
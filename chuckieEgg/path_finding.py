#This is the wrong way round
#it should go through all items, calculate how far it is from the player
#then use the weighting to find the nearest item
import cv2 as cv
def find_closest_item(img, list_of_items, start_location, colour):
    closest_item = (0,0)
    start_x, start_y = start_location
    for item in list_of_items:
        item_x, item_y = item
        if item_y > start_y and item_y < start_y + 25:
            closest_item = item
    if closest_item > (0, 0):
        img = cv.line(img, (start_x, start_y), closest_item, colour, 3)
    return img, closest_item
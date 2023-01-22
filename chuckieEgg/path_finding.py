#This is the wrong way round
#it should go through all items, calculate how far it is from the player
#then use the weighting to find the nearest item
import cv2 as cv

def put_objects_in_array(the_array, the_list, tile_size, number_for_array):
    #Pass a list of x, y tuples and add them in the array
    for object in the_list:
        x, y = object
        x = int(x/tile_size)
        y = int(y/tile_size)
        the_array[y][x] = number_for_array
    return the_array

def put_objects_in_array(the_array, the_list, tile_size):
    #Pass a list of x, y tuples and remove them in the array
    for object in the_list:
        x, y = object
        x = int(x/tile_size)
        y = int(y/tile_size)
        the_array[y][x] = 0
    return the_array

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
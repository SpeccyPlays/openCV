#This is the wrong way round
#it should go through all items, calculate how far it is from the player
#then use the weighting to find the nearest item
import cv2 as cv
def put_objects_in_array(the_array, the_list, tile_size, number_for_array):
    for object in the_list:
        x, y = object
        # as the location is top left corner have a small offset to make sure array location is clean
        offset = int(tile_size/4)#maybe
        x = int(x/tile_size)
        y = int(y/tile_size)
        print('object : ', object, 'Array : ', x, ',', y)
        the_array[y][x] = number_for_array
    for i in the_array:
        print(i)
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
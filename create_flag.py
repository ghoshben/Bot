import json


def get_rectangle_coordinates(* ,top_y, bottom_y, left_x, right_x, colour):
    """Gets the coordinates of the rectangle to create a flag."""
    coords = []
    for y in range(top_y, bottom_y+1):
        for x in range(left_x, right_x+1):
            coords.append([x, y, colour])
    return coords

saffron = get_rectangle_coordinates(top_y = 299,bottom_y= 315,left_x= 238,right_x= 541,colour= 3)
white = get_rectangle_coordinates(top_y= 316,bottom_y= 329,left_x= 238,right_x= 541,colour= 31)
# remove pixels in chakra area for now
white = list(filter(lambda v: v[0]>392 or v[0]<376, white))
green = get_rectangle_coordinates(top_y= 330,bottom_y= 342,left_x= 238,right_x= 541,colour= 6)

flag = saffron + white + green

with open("orders.json", "w") as f:
    json.dump(flag, f, indent=4)

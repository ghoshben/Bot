import json


def get_rectangle_coordinates(top_y, bottom_y, left_x, right_x, colour):
    """Gets the coordinates of the rectangle to create a flag."""
    coords = []
    for y in range(top_y, bottom_y+1):
        for x in range(left_x, right_x+1):
            coords.append([x, y, colour])
    return coords

saffron = get_rectangle_coordinates(299, 315, 238, 541, 3)
white = get_rectangle_coordinates(316, 239, 238, 541, 31)
green = get_rectangle_coordinates(330, 342, 238, 541, 6)

flag = saffron + white + green

with open("orders.json", "w") as f:
    json.dump(flag, f, indent=4)

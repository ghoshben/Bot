import json
import math
import os 

from PIL import Image

# map of colors for pixels you can place
color_map = {
    "#FF4500": 2,  # bright red
    "#FFA800": 3,  # orange
    "#FFD635": 4,  # yellow
    "#00A368": 6,  # darker green
    "#7EED56": 8,  # lighter green
    "#2450A4": 12,  # darkest blue
    "#3690EA": 13,  # medium normal blue
    "#51E9F4": 14,  # cyan
    "#811E9F": 18,  # darkest purple
    "#B44AC0": 19,  # normal purple
    "#FF99AA": 23,  # pink
    "#9C6926": 25,  # brown
    "#000000": 27,  # black
    "#898D90": 29,  # grey
    "#D4D7D9": 30,  # light grey
    "#FFFFFF": 31,  # white
}

rgb_colors_array = [(255, 69, 0), (255, 168, 0), (255, 214, 53), (0, 163, 104), (126, 237, 86), (36, 80, 164), (54, 144, 234), (81, 233, 244), (129, 30, 159), (180, 74, 192), (255, 153, 170), (156, 105, 38), (0, 0, 0), (137, 141, 144), (212, 215, 217), (255, 255, 255)]

def rgb_to_hex(rgb):
    return ('#%02x%02x%02x' % rgb).upper()

def closest_color(target_rgb):
    global rgb_colors_array
    
    r, g, b = target_rgb
    a = target_rgb[3] if len(target_rgb) > 3 else 255 

    if a < 255 or (r,g,b) == (69,42,0):
        return (69,42,0)
    
    color_diffs = []
    for color in rgb_colors_array:
        cr, cg, cb = color
        color_diff = math.sqrt((r - cr) ** 2 + (g - cg) ** 2 + (b - cb) ** 2)
        color_diffs.append((color_diff, color))
        
    return min(color_diffs)[1]


def test_coords(coords):
    global reverse_map

    image_path = os.path.join(os.path.abspath(os.getcwd()), 'image.jpg')
    im = Image.open(image_path)
    pix = im.load()
    
    for r, c, cc in coords:
        pix[r, c] = reverse_map[cc][0]
    
    new_image_path = os.path.join(os.path.abspath(os.getcwd()), 'new_image.png')
    im.save(new_image_path)

start_x = 0
start_y = 0

image_path = os.path.join(os.path.abspath(os.getcwd()), 'image.jpg')
im = Image.open(image_path)

pix = im.load()
w, h = im.size

coords = []
reverse_map = {}
for y in range(start_y, start_y+h):
    for x in range(start_x, start_x+w):
        target_rgb = pix[x, y];
        new_rgb = closest_color(target_rgb)
        new_hex = rgb_to_hex(new_rgb)
        color_code = color_map[new_hex]
        coords.append([x, y, color_code])
        reverse_map[color_code] = [new_rgb, new_hex]

test_coords(coords)


with open("image_to_orders.json", "w") as f:
    json.dump(coords, f, indent=4)

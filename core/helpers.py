from colorthief import ColorThief
from PIL import Image
from webcolors import rgb_to_hex


def get_attrs_from_img(image):
    with Image.open(image) as img:
        width, height = img.size
    color_thief = ColorThief(image)
    hex_color = rgb_to_hex(color_thief.get_color(quality=1))
    return {
        'color': hex_color,
        'height': height,
        'width': width
    }

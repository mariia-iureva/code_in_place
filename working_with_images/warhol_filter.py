"""
This program generates the Warhol effect based on the original image.
"""

from simpleimage import SimpleImage
import random

N_ROWS = 2
N_COLS = 3
PATCH_SIZE = 222
WIDTH = N_COLS * PATCH_SIZE
HEIGHT = N_ROWS * PATCH_SIZE
PATCH_NAME = 'images/simba-sq.jpg'

def make_recolored_patch(red_scale, green_scale, blue_scale):
    '''
    Implement this function to make a patch for the Warhol Filter.
    It loads the patch image and recolors it.
    :param red_scale: A number to multiply each pixel's red component by
    :param green_scale: A number to multiply each pixel's green component by
    :param blue_scale: A number to multiply each pixel's blue component by
    Returns the newly generated patch.
    '''
    patch = SimpleImage(PATCH_NAME)
    # TODO: your code here
    for pixel in patch:
        pixel.red = pixel.red * red_scale
        pixel.green = pixel.green * green_scale
        pixel.blue = pixel.blue * blue_scale
    return patch

def put_patch(final_image, start_x, start_y, patch):
    # width = final_image.width
    # height = final_image.height
    for y in range(PATCH_SIZE):
        for x in range(PATCH_SIZE):
            pixel = patch.get_pixel(x, y)
            final_image.set_pixel(x + start_x, y + start_y, pixel)
            # final_image.set_pixel(x + 222, y, pixel)
            # final_image.set_pixel(x + 222 + 222, y, pixel)
    return final_image

def set_scale():
    scale = random.uniform(0.0, 2.0)
    return scale


def main():
    final_image = SimpleImage.blank(WIDTH, HEIGHT)

    # TODO: your code here
    # This is an example which should generate a pinkish patch

    start_y = 0
    for i in range(N_ROWS): #2
        start_x = 0
        for i in range(N_COLS): #3
            red_scale = set_scale()
            green_scale = set_scale()
            blue_scale = set_scale()
            patch = make_recolored_patch(red_scale, green_scale, blue_scale)
            final_image = put_patch(final_image, start_x, start_y, patch)
            start_x += PATCH_SIZE
        start_y += PATCH_SIZE
    
    final_image.show()

if __name__ == '__main__':
    main()

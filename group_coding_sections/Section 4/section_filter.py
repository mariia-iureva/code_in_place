"""
This program loads an image and applies the narok filter
to it by setting "bright" pixels to grayscale values.
"""

from simpleimage import SimpleImage
# name: MAGIC_NUMBER, type: int, value: 153 (constant)
MAGIC_NUMBER = 153

def main():
    # name: image, type: SimpleImage, value: SimpleImage suitcase
    image = SimpleImage('images/simba-sq.jpg')

    # name: px, type: Pixel, value: The First Pixel (will change)
    for px in image:
        # name: red, type: int, value: The amount of red in the pixel
        red = px.red;
        # name: red, type: int, value: The amount of green in the pixel
        green = px.green;
        # name: red, type: int, value: The amount of green in the pixel
        blue = px.blue;

        # name: average, type: int, value: The average of red, green blue
        average = (red + green + blue) // 3 # //
        # name: isTooBright, type: boolean, value: Is this pixel too bright
        isTooBright = average > MAGIC_NUMBER
        if isTooBright:
            turn_grey(px, average)
    # Apply the filter
    # TODO: your code here

    image.show()

def turn_grey(px2, average):
    px2.red = average
    px2.green = average
    px2.blue = average

if __name__ == '__main__':
    main()

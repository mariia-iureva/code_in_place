from simpleimage import SimpleImage

def main():
    image = SimpleImage('images/karel.png')
    trimmed_img = trim_crop_image(image, 30)
    trimmed_img.show()

def trim_crop_image(original_img, trim_size):
    width = original_img.width# - trim_size * 2
    height = original_img.height# - trim_size * 2
    cropped_image = SimpleImage.blank(width, height)
    # count pixels, left 30th, top 30th, right 30th, bottom 30th
    # name: y, type: int, value: 0 (counting up)
    for y in range(original_img.height): 
        for x in range(original_img.width):  
            original_pixel = original_img.get_pixel(x, y)

            is_outside_boundary = outside_boundary(x, y, trim_size, original_img.width, original_img.height)
            
            if not is_outside_boundary:
                # copy pixel from original_img to cropped_img
                cropped_image_pixel = cropped_image.get_pixel(x, y)
                cropped_image_pixel.red = original_pixel.red
                cropped_image_pixel.green = original_pixel.green
                cropped_image_pixel.blue = original_pixel.blue

    # return the new cropped image
    return cropped_image
    # TODO: your code here

# should I get rid of this pixel?
# max_x is the initial width of the uncropped image
# max_y is the initial height of the uncropped image
def outside_boundary(pixel_x, pixel_y, side_amount, max_x, max_y):
    if pixel_x < 30:
        return True
    
    if pixel_x > max_x - 30:
        return True

    if pixel_y < 30:
        return True

    if pixel_y > max_y - 30:
        return True

    return False


if __name__ == '__main__':
    main()

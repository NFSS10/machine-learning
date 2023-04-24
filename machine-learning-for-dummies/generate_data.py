import os
import png
import itertools
import random


RED = [255, 0, 0]
GREEN = [0, 255, 0]
BLUE = [0, 0, 255]


def main():
    # size of the images to be generated
    width = 8
    height = 8

    # create output folders for the images
    red_output_folder = "./red/"
    blue_output_folder = "./blue/"
    os.makedirs(red_output_folder, exist_ok=True)
    os.makedirs(blue_output_folder, exist_ok=True)

    # create images with clear red and blue ranges
    create_red_range(width, height, red_output_folder)
    create_blue_range(width, height, blue_output_folder)

    # create images with a more mixed red and blue ranges
    create_redish_range(width, height, red_output_folder)
    create_blueish_range(width, height, blue_output_folder)


# ---------------------------------------------------------------------


# Builds a image with the specified size and fill it with the provided
# pixel color
def create_filled_png(width, height, pixel):
    image = []
    for y in range(height):
        # creates row of pixels
        row = [pixel for _ in range(width)]

        # flatten list
        row = list(itertools.chain(*row))

        image.append(row)

    return png.from_array(image, "RGB")


# Creates red images with the red channel ranging from 10 to 255 in steps
# of 10
def create_red_range(width, height, output_folder):
    # from 10 to 255 in steps of 10
    for i in range(10, 255, 10):
        pixel = [i, 0, 0]

        print(f"creating {width}x{height} image with pixel: {pixel}")
        image_png = create_filled_png(width, height, pixel)
        image_png.save(f"{output_folder}{pixel}.png")

    # creates the red truth image filled with [255, 0, 0] color
    image_png = create_filled_png(width, height, RED)
    image_png.save(f"{output_folder}red_truth.png")


# Creates red images with the blue channel ranging from 10 to 255 in steps
# of 10
def create_blue_range(width, height, output_folder):
    # from 10 to 255 in steps of 10
    for i in range(10, 255, 10):
        pixel = [0, 0, i]

        print(f"creating {width}x{height} image with pixel: {pixel}")
        image_png = create_filled_png(width, height, pixel)
        image_png.save(f"{output_folder}{pixel}.png")

    # creates the blue truth image filled with [0, 0, 255] color
    image_png = create_filled_png(width, height, BLUE)
    image_png.save(f"{output_folder}blue_truth.png")


# Creates red images with some random values for the green and blue channels
def create_redish_range(width, height, output_folder, num_images=100):
    for i in range(num_images):
        value = random.randint(50, 255)
        green_rand = random.uniform(0, 0.25)
        blue_rand = random.uniform(0, 0.5)

        red = value
        green = int(value * green_rand)
        blue = int(value * blue_rand)

        pixel = [red, green, blue]
        print(f"creating {width}x{height} image with pixel: {pixel}")
        image_png = create_filled_png(width, height, pixel)
        image_png.save(f"{output_folder}{pixel}.png")


# Creates blue images with some random values for the red and green channels
def create_blueish_range(width, height, output_folder, num_images=100):
    for i in range(num_images):
        value = random.randint(50, 255)
        red_rand = random.uniform(0, 0.5)
        green_rand = random.uniform(0, 0.25)

        red = int(value * red_rand)
        green = int(value * green_rand)
        blue = value

        pixel = [red, green, blue]
        print(f"creating {width}x{height} image with pixel: {pixel}")
        image_png = create_filled_png(width, height, pixel)
        image_png.save(f"{output_folder}{pixel}.png")


if __name__ == "__main__":
    main()

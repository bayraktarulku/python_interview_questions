import colorsys
import random

import matplotlib.pyplot as plt
import numpy as np
from IPython.display import display
from PIL import Image, ImageChops, ImageDraw


def setup():
    global image_size, padding
    image_size = 512
    padding = 32


image1 = Image.new("RGB", size=(256, 256), color=(255, 0, 0))
image2 = Image.new("RGB", size=(256, 256), color=(0, 255, 0))
image3 = Image.new("RGB", size=(256, 256), color=(0, 0, 255))
draw1 = ImageDraw.Draw(image1)
line1 = ((0, 0), (256, 256))
draw1.line(line1, width=20)

draw2 = ImageDraw.Draw(image2)
line2 = ((256, 0), (0, 256))
draw2.line(line2, width=20)

draw3 = ImageDraw.Draw(image3)
line3 = ((0, 0), (256, 256))
draw3.line(line3, width=20)


def generate_point(num_points):
    points = []
    for i in range(num_points):
        points.append(
            (
                random.randint(0 + padding, image_size - padding),
                random.randint(0 + padding, image_size - padding),
            )
        )
    return points


def random_color():
    h = random.random()  # Parlak/canlı renkler
    s = 1
    v = 1
    float_rgb = colorsys.hsv_to_rgb(h, s, v)
    rgb = [int(s * 255) for s in float_rgb]
    return tuple(rgb)


def interpolate(start_color, end_color, factor: float):
    recip = 1 - factor
    return (
        int(start_color[0] * recip + end_color[0] * factor),
        int(start_color[1] * recip + end_color[1] * factor),
        int(start_color[2] * recip + end_color[2] * factor),
    )


def generate_art(path):
    print("Yeahh!! Generating art!")

    setup()
    image_bg = (0, 0, 0)
    image = Image.new("RGB", size=(image_size, image_size), color=image_bg)

    draw = ImageDraw.Draw(image)
    points = generate_point(10)

    start_color = random_color()
    end_color = random_color()

    for i in range(len(points)):

        overlay_image = Image.new("RGB", size=(image_size, image_size), color=image_bg)
        overlay_draw = ImageDraw.Draw(overlay_image)

        if i == (len(points) - 1):
            p1 = points[i]
            p2 = points[0]
        else:
            p1 = points[i]
            p2 = points[i + 1]
        factor = i / (len(points) - 1)
        line_color = interpolate(start_color, end_color, factor)
        line = (p1, p2)
        overlay_draw.line(line, fill=line_color, width=i + 1)
        image = ImageChops.add(image, overlay_image)

    image.resize((image_size, image_size), resample=Image.ANTIALIAS)
    image.save(path)


for i in range(1):
    generate_art(f"image_{i}.png")

fig = plt.figure(figsize=(20, 20))
columns = 4
rows = 3
for i in range(0, 1):
    img = np.array(Image.open(f"image_{i}.png"))
    fig.add_subplot(rows, columns, i + 1)
    plt.imshow(img)
    plt.axis("off")
    plt.show()
plt.tight_layout()

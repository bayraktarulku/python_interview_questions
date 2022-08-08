import turtle
from turtle import *

COLORS = {
    0: "white",
    1: "red",
    2: "blue",
    3: "green",
    4: "black",
}

PIXELS = [
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 4, 4, 4, 4, 4, 4, 4, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 4, 4, 4, 4, 4, 4, 0, 4, 4, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 4, 4, 4, 4, 4, 4, 0, 0, 4, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 4, 4, 4, 4, 4, 4, 0, 0, 4, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 4, 4, 4, 4, 4, 4, 0, 0, 4, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 4, 4, 4, 4, 4, 4, 0, 0, 4, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 4, 4, 4, 4, 0, 0, 0, 4, 4, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 4, 4, 4, 4, 0, 0, 0, 0, 4, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 4, 4, 4, 4, 0, 0, 0, 4, 4, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 4, 4, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 4, 4, 4, 4, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 4, 4, 4, 4, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 4, 4, 4, 4, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 4, 0, 0, 4, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
]

WIDTH, HEIGHT = len(PIXELS[0]), len(PIXELS)

scn = turtle.Screen()
pen = turtle.Turtle()


def pixel():
    for i in range(4):
        pen.forward(5)
        pen.left(90)
    pen.forward(5)


if __name__ == "__main__":
    scn.setup(1000, 1500)
    pen.speed(0)
    pen.hideturtle()
    for i in range(WIDTH):
        pen.up()
        pen.setpos(0, 5 * i)
        pen.color("gray")
        pen.down()
        row = PIXELS[i]
        for j in range(HEIGHT):
            col = COLORS[row[j]]
            pen.fillcolor(col)
            pen.begin_fill()
            pixel()
            pen.end_fill()

    print("done - press any key to exit")
    turtle.onkeypress(exit)
    turtle.listen()
    turtle.done()

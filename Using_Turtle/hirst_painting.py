import turtle as t
import random

tim = t.Turtle()
t.colormode(255)
my_screen = t.Screen()
colors = [(233, 222, 92), (211, 158, 105), (116, 177, 210), (226, 57, 131), (181, 78, 33), (210, 135, 174),
          (41, 103, 161), (12, 21, 62), (184, 46, 111), (186, 164, 23), (43, 182, 112), (122, 187, 155), (25, 32, 158),
          (173, 16, 67), (234, 164, 199), (229, 75, 43)]


def horizontal():
    for _ in range(10):
        tim.speed("fastest")
        tim.pendown()
        tim.dot(20, random.choice(colors))
        tim.penup()
        tim.forward(50)


def next_row(x, y):
    tim.penup()
    tim.setpos(x, y)


def draw():
    steps = 0
    x = -200
    y = -200
    tim.hideturtle()
    tim.penup()
    tim.setpos(x, y)

    while steps < 10:
        horizontal()
        steps += 1
        y += 50
        next_row(x, y)
    my_screen.exitonclick()


draw()


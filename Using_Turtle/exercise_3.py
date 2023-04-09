from turtle import Turtle
import random

tim = Turtle()
angle = 0
colors = ["red", "orange", "lime", "deep pink", "royal blue", "orange red", "sea green", "black", "dark slate gray", "teal", "green", "firebrick", "indigo", "hot pink"]
tim.pensize(3)

def draw():
    for number_of_sides in range(3,11):
        angle = 360 / number_of_sides
        index = random.randint(0,len(colors))
        pen_colors = colors[index]
        for _ in range(number_of_sides):
            tim.pencolor(pen_colors)
            tim.forward(100)
            tim.right(angle)

draw()
my_screen.exitonclick()
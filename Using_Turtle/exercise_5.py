import turtle as t
import random

tim = t.Turtle()
my_screen = t.Screen()
t.colormode(255)
tim.speed("fastest")

def color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    return (r, g, b)

def draw(size_of_gap):
    number_of_circles = round(360 / size_of_gap)
    for _ in range(number_of_circles):
        tim.pencolor(color())
        tim.circle(100)
        size_of_gap += 5
        tim.setheading(size_of_gap)

draw(5)
my_screen.exitonclick()
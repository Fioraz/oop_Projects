import turtle as t
import random

tim = t.Turtle()
t.colormode(255)
is_on = True
tim.pensize(10)
tim.speed("fastest")
directions = [0, 90, 180, 270]

def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    return (r, g, b)

def random_walk():
    while is_on:
        tim.pencolor(random_color())
        tim.forward(50)
        tim.setheading(random.choice(directions))
        
random_walk()
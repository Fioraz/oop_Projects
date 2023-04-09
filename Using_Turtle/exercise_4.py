from turtle import Turtle
import random

tim = Turtle()
is_on = True
tim.pensize(10)
tim.speed("fast")
directions = [0, 90, 180, 270]
colors = ["red", "orange", "lime", "deep pink", "royal blue", "orange red", "sea green", "black", "dark slate gray", "teal", "green", "firebrick", "indigo", "hot pink"]

def random_walk():
    while is_on:
        tim.pencolor(random.choice(colors))
        tim.forward(50)
        tim.setheading(random.choice(directions))
        
random_walk()
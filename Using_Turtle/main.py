from turtle import Turtle, Screen

timmy = Turtle()
print(timmy)
timmy.shape("turtle")
timmy.color("black","slateblue1")

for _ in range(4):
    timmy.forward(100)
    timmy.left(90)

my_screen = Screen()
print(my_screen.canvheight)
my_screen.exitonclick()

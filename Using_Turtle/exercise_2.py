import turtle

tim = turtle.Turtle()
my_screen = turtle.Screen()
my_screen.bgcolor("#809980")

for _ in range(15):
    tim.forward(10)
    tim.penup()
    tim.forward(10)
    tim.pendown()

print(my_screen.canvheight)
my_screen.exitonclick()



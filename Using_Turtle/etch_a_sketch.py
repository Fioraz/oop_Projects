import turtle as t

tim = t.Turtle()
screen = t.Screen()


def move_forward():
    tim.forward(10)


def move_backward():
    tim.backward(10)


def rotate_anticlock():
    tim.left(10)


def rotate_clock():
    tim.right(10)


def clear():
    tim.clear()
    tim.penup()
    tim.home()


screen.listen()
screen.onkey(move_forward, "w")
screen.onkey(move_backward, "s")
screen.onkey(rotate_anticlock, "a")
screen.onkey(rotate_clock, "d")
screen.onkey(clear, "c")
screen.exitonclick()

from turtle import Turtle, Screen

screen = Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput("Turtle Race", "Who will win the race? Enter a colour.")
colors = ["purple", "blue", "green", "yellow", "orange", "red"]
y = -100

for turtle_index in range(6):
    tim = Turtle(shape="turtle")
    tim.color(colors[turtle_index])
    tim.setpos(-240, y)
    y += 50


screen.exitonclick()

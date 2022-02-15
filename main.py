from turtle import Screen, Turtle

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My Snake Game")

start_position = [(0,0),(-20, 0),(-40,0)]

for position in start_position:
    tim = Turtle(shape = "square")
    tim.color("white")
    tim.goto(position)










screen.exitonclick()
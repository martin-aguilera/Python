from turtle import (
    bgcolor,
    speed,
    hideturtle,
    color,
    circle,
    right,
    forward,
    exitonclick,
)

bgcolor("black")
speed(50)
hideturtle()
for i in range(120):
    color("cyan")
    circle(i)
    color("green")
    circle(i * 0.8)
    color("lime")
    circle(i * 1.5)
    right(3)
    forward(3)
exitonclick()

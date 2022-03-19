from turtle import bgcolor, pensize, speed, hideturtle, color, circle, left, exitonclick

color_list = ["red", "magenta", "blue", "cyan", "green", "yellow", "white"]
bgcolor("black")
pensize(2)
speed(0)
hideturtle()
for i in range(6):
    for colours in color_list:
        color(colours)
        circle(100)
        left(10)
exitonclick()

from turtle import forward, title, speed, color, bgcolor, left, exitonclick

title("wtf")
speed(11)
color("cyan")
bgcolor("black")
a = 170
while a > -210:
    left(a)
    forward(a * 2)
    a -= 1
exitonclick()

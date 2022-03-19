import turtle

s = turtle.Screen()
t = turtle.Turtle()
s.bgcolor("black")
t.pencolor("red")
t.speed(0)
for i in range(150):
    t.circle(190 - i, 90)
    t.lt(90)
    t.circle(190 - i, 90)
    t.lt(18)
turtle.exitonclick()

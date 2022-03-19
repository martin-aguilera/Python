import turtle

s = turtle.Screen()
t = turtle.Turtle()
s.bgcolor("black")
t.width(2)
t.speed(15)
col = ("white", "cyan", "lime")
for i in range(300):
    t.pencolor(col[i % 3])
    t.forward(i * 4)
    t.right(121)
turtle.exitonclick()

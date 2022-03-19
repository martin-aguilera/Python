import turtle
import time


# Ventana
wn = turtle.Screen()
wn.title("Pong")
wn.bgcolor("black")
wn.setup(width=800, height=600)
wn.tracer(0)

####################################

# Marcador
marcadorA = 0
marcadorB = 0

####################################

# Jugador A
jugadorA = turtle.Turtle()
jugadorA.speed(0)
jugadorA.shape("square")
jugadorA.color("white")
jugadorA.penup()
jugadorA.goto(-350, 0)
jugadorA.shapesize(stretch_wid=5, stretch_len=1)

####################################

# Jugador B
jugadorB = turtle.Turtle()
jugadorB.speed(0)
jugadorB.shape("square")
jugadorB.color("white")
jugadorB.penup()
jugadorB.goto(350, 0)
jugadorB.shapesize(stretch_wid=5, stretch_len=1)

####################################

# Pelota
pelota = turtle.Turtle()
pelota.speed(0)
pelota.shape("circle")
pelota.color("white")
pelota.penup()
pelota.goto(0, 0)
pelota.dx = 0.5
pelota.dy = 0.5

####################################

# Linea de divición
divicion = turtle.Turtle()
divicion.color("white")
divicion.goto(0, 400)
divicion.goto(0, -400)

####################################

# Pen
pen = turtle.Turtle()
pen.speed(0)
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
pen.write("Player A: 0		Player B: 0", align="center", font=("Courier", 24, "normal"))

####################################

# Funciones
# A
def jugadorA_up():
    y = jugadorA.ycor()
    y += 25
    jugadorA.sety(y)


def jugadorA_down():
    y = jugadorA.ycor()
    y -= 25
    jugadorA.sety(y)


# B
def jugadorB_up():
    y = jugadorB.ycor()
    y += 25
    jugadorB.sety(y)


def jugadorB_down():
    y = jugadorB.ycor()
    y -= 25
    jugadorB.sety(y)


####################################

# Teclado
wn.listen()
wn.onkeypress(jugadorA_up, "w")
wn.onkeypress(jugadorA_down, "s")
wn.onkeypress(jugadorB_up, "Up")
wn.onkeypress(jugadorB_down, "Down")
########################################################################
########################################################################
########################################################################
########################################################################
########################################################################
while True:
    wn.update()

    pelota.setx(pelota.xcor() + pelota.dx)
    pelota.sety(pelota.ycor() + pelota.dy)

    # Bordes
    if pelota.ycor() > 290:
        pelota.dy *= -1
    if pelota.ycor() < -290:
        pelota.dy *= -1

    # Bordes Izquierda/Derecha
    if pelota.xcor() > 390:
        pelota.goto(0, 0)
        pelota.dx *= -1
        marcadorA += 1
        pen.clear()
        pen.write(
            "Player A: {}		Player B: {}".format(marcadorA, marcadorB),
            align="center",
            font=("Courier", 24, "normal"),
        )

    if pelota.xcor() < -390:
        pelota.goto(0, 0)
        pelota.dx *= -1
        marcadorB += 1
        pen.clear()
        pen.write(
            "Player A: {}		Player B: {}".format(marcadorA, marcadorB),
            align="center",
            font=("Courier", 24, "normal"),
        )

    if (pelota.xcor() > 340 and pelota.xcor() < 350) and (
        pelota.ycor() < jugadorB.ycor() + 50 and pelota.ycor() > jugadorB.ycor() - 50
    ):
        pelota.dx *= -1

    if (pelota.xcor() < -340 and pelota.xcor() > -350) and (
        pelota.ycor() < jugadorA.ycor() + 50 and pelota.ycor() > jugadorA.ycor() - 50
    ):
        pelota.dx *= -1

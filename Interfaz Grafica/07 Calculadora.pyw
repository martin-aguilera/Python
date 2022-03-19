from tkinter import *

root = Tk()
root.resizable(1, 1)
root.iconbitmap("assets/wea.ico")

miFrame = Frame(root)
miFrame.pack()
# miFrame.config(bg='Black')

operacion = ""
reset_pantalla = False
resultado = 0

# -------------PANTALLA---------------------------------------------
numScreen = StringVar()
screen = Entry(miFrame, textvariable=numScreen)
screen.grid(row=1, column=1, padx=5, pady=5, columnspan=4)
screen.config(background="black", fg="white", justify="right")

# -------------PULSACIONES-TECLADO----------------------------------
def numeroPulsado(num):
    global operacion
    global reset_pantalla
    if reset_pantalla != False:
        numScreen.set(num)
        reset_pantalla = False
    else:
        numScreen.set(numScreen.get() + num)


def suma(num):
    global operacion
    global resultado
    global reset_pantalla
    resultado += float(num)
    operacion = "suma"
    reset_pantalla = True
    numScreen.set(resultado)


num1 = 0
contador_resta = 0


def resta(num):
    global operacion
    global resultado
    global num1
    global contador_resta
    global reset_pantalla
    if contador_resta == 0:
        num1 = float(num)
        resultado = num1
    else:
        if contador_resta == 1:
            resultado = num1 - float(num)
        else:
            resultado = float(resultado) - float(num)
        numScreen.set(resultado)
        resultado = numScreen.get()
    contador_resta = contador_resta + 1
    operacion = "resta"
    reset_pantalla = True


contador_multi = 0


def multiplica(num):
    global operacion
    global resultado
    global num1
    global contador_multi
    global reset_pantalla
    if contador_multi == 0:
        num1 = float(num)
        resultado = num1
    else:
        if contador_multi == 1:
            resultado = num1 * float(num)
        else:
            resultado = float(resultado) * float(num)
        numScreen.set(resultado)
        resultado = numScreen.get()
    contador_multi = contador_multi + 1
    operacion = "multiplicacion"
    reset_pantalla = True


contador_divi = 0


def divide(num):
    global operacion
    global resultado
    global num1
    global contador_divi
    global reset_pantalla
    if contador_divi == 0:
        num1 = float(num)
        resultado = num1
    else:
        if contador_divi == 1:
            resultado = num1 / float(num)
        else:
            resultado = float(resultado) / float(num)
        numScreen.set(resultado)
        resultado = numScreen.get()
    contador_divi = contador_divi + 1
    operacion = "division"
    reset_pantalla = True


def El_resultado():
    global resultado
    global operacion
    global contador_resta
    global contador_multi
    global contador_divi
    if operacion == "suma":
        numScreen.set(resultado + float(numScreen.get()))
        resultado = 0
    elif operacion == "resta":
        numScreen.set(float(resultado) - float(numScreen.get()))
        resultado = 0
        contador_resta = 0
    elif operacion == "multiplicacion":
        numScreen.set(float(resultado) * float(numScreen.get()))
        resultado = 0
        contador_multi = 0
    elif operacion == "division":
        numScreen.set(float(resultado) / float(numScreen.get()))
        resultado = 0
        contador_divi = 0


def Borrado():
    global resultado
    numScreen.set(" ")


# -----------FILA-1-------------------------------------------------
boton7 = Button(miFrame, text="7", width=3, command=lambda: numeroPulsado("7"))
boton7.grid(row=2, column=1)
boton7.config(background="gray")

boton8 = Button(miFrame, text="8", width=3, command=lambda: numeroPulsado("8"))
boton8.grid(row=2, column=2)
boton8.config(background="gray")

boton9 = Button(miFrame, text="9", width=3, command=lambda: numeroPulsado("9"))
boton9.grid(row=2, column=3)
boton9.config(background="gray")

botonDiv = Button(miFrame, text="/", width=3, command=lambda: divide(numScreen.get()))
botonDiv.grid(row=2, column=4)
botonDiv.config(background="orange")

# -----------FILA-2-------------------------------------------------
boton4 = Button(miFrame, text="4", width=3, command=lambda: numeroPulsado("4"))
boton4.grid(row=3, column=1)
boton4.config(background="gray")

boton5 = Button(miFrame, text="5", width=3, command=lambda: numeroPulsado("5"))
boton5.grid(row=3, column=2)
boton5.config(background="gray")

boton6 = Button(miFrame, text="6", width=3, command=lambda: numeroPulsado("6"))
boton6.grid(row=3, column=3)
boton6.config(background="gray")

botonMul = Button(
    miFrame, text="x", width=3, command=lambda: multiplica(numScreen.get())
)
botonMul.grid(row=3, column=4)
botonMul.config(background="orange")

# -----------FILA-3-------------------------------------------------
boton1 = Button(miFrame, text="1", width=3, command=lambda: numeroPulsado("1"))
boton1.grid(row=4, column=1)
boton1.config(background="gray")

boton2 = Button(miFrame, text="2", width=3, command=lambda: numeroPulsado("2"))
boton2.grid(row=4, column=2)
boton2.config(background="gray")

boton3 = Button(miFrame, text="3", width=3, command=lambda: numeroPulsado("3"))
boton3.grid(row=4, column=3)
boton3.config(background="gray")

botonRes = Button(miFrame, text="-", width=3, command=lambda: resta(numScreen.get()))
botonRes.grid(row=4, column=4)
botonRes.config(background="orange")

# -----------FILA-4-------------------------------------------------
boton0 = Button(miFrame, text="0", width=3, command=lambda: numeroPulsado("0"))
boton0.grid(row=5, column=1)
boton0.config(background="gray")

botonDot = Button(miFrame, text=".", width=3, command=lambda: numeroPulsado("."))
botonDot.grid(row=5, column=2)
botonDot.config(background="gray")

botonCls = Button(miFrame, text="cls", width=3, command=lambda: Borrado())
botonCls.grid(row=5, column=3)
botonCls.config(background="orange")

botonSum = Button(miFrame, text="+", width=3, command=lambda: suma(numScreen.get()))
botonSum.grid(row=5, column=4)
botonSum.config(background="orange")

# -----------FILA-5-------------------------------------------------

botonEqu = Button(miFrame, text="=", width=3, command=lambda: El_resultado())
botonEqu.grid(row=6, column=3, columnspan=4, sticky="nsew")
botonEqu.config(background="orange")

# botonBack = Button(miFrame, text='del', width=3)
# botonBack.grid(row=6, column=1)

root.mainloop()

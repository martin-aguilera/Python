from tkinter import *
import os

os.system("cls")

root = Tk()
varOpcion = IntVar()

miFrame = Frame(root, width=400, height=400)
miFrame.pack()


def Imprimir():
    os.system("cls")
    if varOpcion.get() == 1:
        etiqueta_2.config(text="Haz elegido Femenino")
    elif varOpcion.get() == 2:
        etiqueta_2.config(text="Haz elegido Masculino")
    else:
        etiqueta_2.config(text="~ERROR: 404")


etiqueta = Label(miFrame, text="Tu Genero:")
etiqueta.grid(row=0, column=0)

etiqueta_2 = Label(miFrame)
etiqueta_2.grid(row=4, column=0)

Fem = Radiobutton(
    miFrame, text="Femenino", variable=varOpcion, value=1, command=Imprimir
)
Fem.grid(row=1, column=0)

Mal = Radiobutton(
    miFrame, text="Masculino", variable=varOpcion, value=2, command=Imprimir
)
Mal.grid(row=2, column=0)

Err = Radiobutton(
    miFrame, text="Otro(s)", variable=varOpcion, value=3, command=Imprimir
)
Err.grid(row=3, column=0)

root.mainloop()

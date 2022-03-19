from tkinter import *

root = Tk()
root.title("wea")
root.resizable(0, 0)

miFrame = Frame(root, width=300, height=200)
miFrame.pack()

minombre = StringVar()
miapellido = StringVar()
micontraseña = StringVar()

The_input_name = Entry(miFrame, textvariable=minombre)
The_input_name.grid(row=0, column=1, padx=10, pady=5)
Label_name = Label(miFrame, text="Nombre:")
Label_name.grid(row=0, column=0, padx=10, pady=5)

The_input_lastname = Entry(miFrame, textvariable=miapellido)
The_input_lastname.grid(row=1, column=1, padx=10, pady=5)
Label_lastname = Label(miFrame, text="Apellido:")
Label_lastname.grid(row=1, column=0, padx=10, pady=5)

Input_pass = Entry(miFrame)
Input_pass.grid(row=2, column=1, padx=10, pady=5)
Input_pass.config(show="*")
Label_pass = Label(miFrame, text="Contraseña:")
Label_pass.grid(row=2, column=0, padx=10, pady=5)

Text_comments = Text(miFrame, width=16, height=5)
Text_comments.grid(row=3, column=1, padx=10, pady=10)
ScrollVert = Scrollbar(miFrame, command=Text_comments.yview)
ScrollVert.grid(row=3, column=2, sticky="nsew")
Text_comments.config(yscrollcommand=ScrollVert.set)
Label_comments = Label(miFrame, text="Comentarios:")
Label_comments.grid(row=3, column=0, padx=10, pady=10)


def codigoBoton():
    minombre.set("Martín")
    miapellido.set("Aguilera")


boton_1 = Button(root, text="Enviar", command=codigoBoton)
boton_1.pack()

root.mainloop()

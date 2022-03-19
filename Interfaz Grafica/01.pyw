from tkinter import *
import tkinter

raiz = Tk()  # Se crea una interfaz (la raiz de la interfaz grafica)
raiz.title("PICO PAL KE LEE")  # Establece el titulo de la interfaz
raiz.resizable(
    True, True
)  # Permite o niega al usuario el poder cambiar el tamaño de la interfaz
# raiz.geometry('350x500')               # Define el tamaño de la interfaz
raiz.iconbitmap("assets/icon.ico")  # Pon tu propio icono en la interfaz
raiz.config(bg="lime")  # Establece un color de fondo a la interfaz
raiz.config(bd=35)
raiz.config(relief="groove")

cubo = Frame()  # Creacion de un frame (aun no esta en la interfaz)
cubo.pack()  # Enpaquetado del frame en la raiz (existe en la interfaz, pero sin forma o color)
cubo.config(bg="red")  # Da color al frame (aun no se ve porque no tiene forma)
cubo.config(width=20, height=20)
cubo.config(bd=10)
cubo.config(relief="groove")
cubo.config(cursor="hand2")

raiz.mainloop()

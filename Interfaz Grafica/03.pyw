from tkinter import *

root = Tk()
root.title("wea")
root.resizable(0, 0)

miFrame = Frame(root, width=300, height=200)
miFrame.pack()

The_input_name = Entry(miFrame)
The_input_name.grid(row=0, column=1, padx=10, pady=5)
Label_name = Label(miFrame, text="Nombre:")
Label_name.grid(row=0, column=0, padx=10, pady=5)

The_input_lastname = Entry(miFrame)
The_input_lastname.grid(row=1, column=1, padx=10, pady=5)
Label_lastname = Label(miFrame, text="Apellido:")
Label_lastname.grid(row=1, column=0, padx=10, pady=5)
root.mainloop()

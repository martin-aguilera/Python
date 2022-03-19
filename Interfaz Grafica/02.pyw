from tkinter import *

root = Tk()

miFrame = Frame(root, width=600, height=600)
miFrame.pack()
# Label(miFrame, text='pico pal ke lee').place(x=15, y=10)

miImagen = PhotoImage(file="assets/gif.gif")
Label(miFrame, image=miImagen).place(x=100, y=100)

root.mainloop()

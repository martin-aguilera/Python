from tkinter import *

root = Tk()
root.title("wea")

miFrame = Frame(root, width=300, height=200)
miFrame.pack()

Text_comments = Text(miFrame, width=16, height=5)
Text_comments.grid(row=0, column=1, padx=10, pady=10)

Label_comments = Label(miFrame, text="Comentarios:")
Label_comments.grid(row=0, column=0, padx=10, pady=10)

ScrollVert = Scrollbar(miFrame, command=Text_comments.yview)
ScrollVert.grid(row=0, column=2, sticky="nsew")

Text_comments.config(yscrollcommand=ScrollVert.set)

root.mainloop()

import subprocess, tkinter.messagebox as msgbox
from tkinter import *

notepad = ["notepad", "Notepad", "NOTEPAD"]
steam = ["steam", "Steam", "STEAM"]
calculator = ["calculator", "Calculator", "CALCULATOR"]
opera = ["opera", "Opera", "OPERA"]
osu = ["osu", "Osu", "OSU", "osu!", "Osu!", "OSU!"]
mega = [
    "mega",
    "Mega",
    "MEGA",
    "megasync",
    "Megasync",
    "MEGAsync",
    "megaSync",
    "MegaSync",
    "MEGASync",
    "MEGASYNC",
]


def Open():

    #   Change the program path to yours in case your path is different
    if nameValue.get() in notepad:
        subprocess.Popen("C:\\WINDOWS\\system32\\notepad.exe")

    # elif nameValue.get() in steam:
    # subprocess.Popen('C:\\Program Files (x86)\\Steam\\steam.exe')

    elif nameValue.get() in calculator:
        subprocess.Popen("C:\\WINDOWS\\system32\\calc.exe")

    elif nameValue.get() in opera:
        subprocess.Popen(
            "C:\\Users\\e x a i d e n\\AppData\\Local\\Programs\\Opera GX\\launcher.exe"
        )

    # elif nameValue.get() in osu:
    # subprocess.Popen('C:\\Users\\e x a i d e n\\Desktop\\Desktop 2\\Archivos\\osu!\\osu!.exe')

    elif nameValue.get() in mega:
        subprocess.Popen(
            "C:\\Users\\e x a i d e n\\AppData\\Local\\MEGAsync\\MEGAsync.exe"
        )

    else:
        print("\nTry Again")


root = Tk()
root.geometry("600x300")
root.title("Wea")

nameValue = StringVar()

Label(root, text="Open your Software", font="comicsansms 19 bold", pady=10).pack()
f1 = Frame(root, pady=30)
Label(f1, text="Enter Software name ", font="comicsansms 13 bold").pack()
nameEntry = Entry(
    f1, textvariable=nameValue, width=30, font="comicsansms 15 bold", relief=SUNKEN
)
nameEntry.pack()
f1.pack()
f2 = Frame(root)
Button(f2, text="Submit", command=Open).pack()
f2.pack()
root.mainloop()

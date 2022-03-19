from tkinter import *
from tkinter import filedialog
from os import system
from mutagen.mp3 import MP3
import pygame, time

system("cls")
root = Tk()
root.title("Trash Player")
root.iconbitmap("assets/icon.ico")
root.geometry("400x325")
root.resizable(0, 0)
root.config(bg="black")
pygame.mixer.init()


def add_song():
    songs = filedialog.askopenfilenames(
        initialdir="C:/Users/e x a i d e n/Music/",
        title="Choose A Song",
        filetypes=(("mp3 Files", "*.mp3"),),
    )
    for song in songs:
        song = song.replace("C:/Users/e x a i d e n/Music/", "")
        song = song.replace(".mp3", "")
        song_box.insert(END, song)


global paused
paused = False


def pause(is_paused):
    global paused
    paused = is_paused
    if paused:
        pygame.mixer.music.unpause()
        paused = False
    else:
        pygame.mixer.music.pause()
        paused = True


def play_time():
    current_time = pygame.mixer.music.get_pos() / 1000
    converted_current_time = time.strftime("%M:%S", time.gmtime(current_time))
    song = song_box.get(ACTIVE)
    song = f"C:/Users/e x a i d e n/Music/{song}.mp3"
    song_mut = MP3(song)
    song_length = song_mut.info.length
    converted_song_length = time.strftime("%M:%S", time.gmtime(song_length))
    status_bar.config(text=f"{converted_current_time} / {converted_song_length}")
    status_bar.after(1000, play_time)


def play():
    song = song_box.get(ACTIVE)
    song = f"C:/Users/e x a i d e n/Music/{song}.mp3"
    pygame.mixer.music.load(song)
    pygame.mixer.music.play(loops=0)
    play_time()


def back():
    next_one = song_box.curselection()
    next_one = next_one[0] - 1
    song = song_box.get(next_one)
    song = f"C:/Users/e x a i d e n/Music/{song}.mp3"
    pygame.mixer.music.load(song)
    pygame.mixer.music.play(loops=0)
    song_box.selection_clear(0, END)
    song_box.activate(next_one)
    song_box.selection_set(next_one, last=None)


def forward():
    next_one = song_box.curselection()
    next_one = next_one[0] + 1
    song = song_box.get(next_one)
    song = f"C:/Users/e x a i d e n/Music/{song}.mp3"
    pygame.mixer.music.load(song)
    pygame.mixer.music.play(loops=0)
    song_box.selection_clear(0, END)
    song_box.activate(next_one)
    song_box.selection_set(next_one, last=None)


def stop():
    pygame.mixer.music.stop()
    song_box.selection_clear(ACTIVE)
    status_bar.config(text="")


def remove_selected():
    song_box.delete(ANCHOR)
    pygame.mixer.music.stop()


def remove_all():
    song_box.delete(0, END)
    pygame.mixer.music.stop()


song_box = Listbox(
    root,
    bg="black",
    fg="green",
    width=60,
    selectbackground="green",
    selectforeground="black",
)
song_box.pack(pady=20)

pause_btn_img = PhotoImage(file="assets/pause2.png")
play_btn_img = PhotoImage(file="assets/play2.png")
back_btn_img = PhotoImage(file="assets/left2.png")
forward_btn_img = PhotoImage(file="assets/right2.png")
stop_btn_img = PhotoImage(file="assets/stop2.png")

control_frame = Frame(root, bg="black")
control_frame.pack()

pause_btn = Button(
    control_frame,
    image=pause_btn_img,
    borderwidth=0,
    bg="black",
    command=lambda: pause(paused),
)
play_btn = Button(
    control_frame, image=play_btn_img, borderwidth=0, bg="black", command=play
)
back_btn = Button(
    control_frame, image=back_btn_img, borderwidth=0, bg="black", command=back
)
forward_btn = Button(
    control_frame, image=forward_btn_img, borderwidth=0, bg="black", command=forward
)
stop_btn = Button(
    control_frame, image=stop_btn_img, borderwidth=0, bg="black", command=stop
)

pause_btn.grid(row=0, column=0, padx=5)
play_btn.grid(row=0, column=1, padx=5)
back_btn.grid(row=0, column=2, padx=5)
forward_btn.grid(row=0, column=3, padx=5)
stop_btn.grid(row=0, column=4, padx=5)

my_menu = Menu(root)
root.config(menu=my_menu)

add_song_menu = Menu(my_menu)
my_menu.add_command(label="Add Songs", command=add_song)

remove_song_menu = Menu(my_menu)
my_menu.add_cascade(label="Remove Songs", menu=remove_song_menu)
remove_song_menu.add_command(label="Remove Selected", command=remove_selected)
remove_song_menu.add_command(label="Remove All", command=remove_all)

"""root = Tk()
root.title('Wea Music Player')
root.iconbitmap('assets/icon.ico')
root.geometry('400x325')
root.resizable(0,0)
root.config(bg='black')"""

status_bar = Label(root, text="", bd=1, relief=GROOVE, anchor=E, bg="black", fg="green")
status_bar.pack(fill=X, side=BOTTOM, ipady=2)

root.mainloop()

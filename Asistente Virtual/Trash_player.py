from tkinter import (
    Tk,
    Listbox,
    PhotoImage,
    Frame,
    Button,
    Menu,
    Label,
    GROOVE,
    X,
    BOTTOM,
    END,
    filedialog,
    ACTIVE,
    E,
    ANCHOR,
)
from os import system
from mutagen.mp3 import MP3
import pygame, time

system("cls")


class Main:
    def __init__(self):
        pygame.mixer.init()
        self.root = Tk()
        self.root.title("Trash Player")
        self.root.iconbitmap("assets/icon.ico")
        self.root.geometry("400x325")
        self.root.resizable(0, 0)
        self.root.config(bg="black")
        self.song_box = Listbox(
            self.root,
            bg="black",
            fg="green",
            width=60,
            selectbackground="green",
            selectforeground="black",
        )
        self.song_box.pack(pady=20)

        self.pause_btn_img = PhotoImage(file="assets/pause2.png")
        self.play_btn_img = PhotoImage(file="assets/play2.png")
        self.back_btn_img = PhotoImage(file="assets/left2.png")
        self.forward_btn_img = PhotoImage(file="assets/right2.png")
        self.stop_btn_img = PhotoImage(file="assets/stop2.png")

        self.control_frame = Frame(self.root, bg="black")
        self.control_frame.pack()

        self.pause_btn = Button(
            self.control_frame,
            image=self.pause_btn_img,
            borderwidth=0,
            bg="black",
            command=lambda: self.pause(paused),
        )
        self.play_btn = Button(
            self.control_frame,
            image=self.play_btn_img,
            borderwidth=0,
            bg="black",
            command=self.play,
        )
        self.back_btn = Button(
            self.control_frame,
            image=self.back_btn_img,
            borderwidth=0,
            bg="black",
            command=self.back,
        )
        self.forward_btn = Button(
            self.control_frame,
            image=self.forward_btn_img,
            borderwidth=0,
            bg="black",
            command=self.forward,
        )
        self.stop_btn = Button(
            self.control_frame,
            image=self.stop_btn_img,
            borderwidth=0,
            bg="black",
            command=self.stop,
        )

        self.pause_btn.grid(row=0, column=0, padx=5)
        self.play_btn.grid(row=0, column=1, padx=5)
        self.back_btn.grid(row=0, column=2, padx=5)
        self.forward_btn.grid(row=0, column=3, padx=5)
        self.stop_btn.grid(row=0, column=4, padx=5)

        self.my_menu = Menu(self.root)
        self.root.config(menu=self.my_menu)

        self.add_song_menu = Menu(self.my_menu)
        self.my_menu.add_command(label="Add Songs", command=self.add_song)

        self.remove_song_menu = Menu(self.my_menu)
        self.my_menu.add_cascade(label="Remove Songs", menu=self.remove_song_menu)
        self.remove_song_menu.add_command(
            label="Remove Selected", command=self.remove_selected
        )
        self.remove_song_menu.add_command(label="Remove All", command=self.remove_all)

        self.status_bar = Label(
            self.root, text="", bd=1, relief=GROOVE, anchor=E, bg="black", fg="green"
        )
        self.status_bar.pack(fill=X, side=BOTTOM, ipady=2)

        self.root.mainloop()

    def add_song(self):
        songs = filedialog.askopenfilenames(
            initialdir="C:/Users/e x a i d e n/Music/",
            title="Choose A Song",
            filetypes=(("mp3 Files", "*.mp3"),),
        )
        for song in songs:
            song = song.replace("C:/Users/e x a i d e n/Music/", "")
            song = song.replace(".mp3", "")
            self.song_box.insert(END, song)

    global paused
    paused = False

    def pause(self, is_paused):
        global paused
        paused = is_paused
        if paused:
            pygame.mixer.music.unpause()
            paused = False
        else:
            pygame.mixer.music.pause()
            paused = True

    def play_time(self):
        self.current_time = pygame.mixer.music.get_pos() / 1000
        self.converted_current_time = time.strftime(
            "%M:%S", time.gmtime(self.current_time)
        )
        song = self.song_box.get(ACTIVE)
        song = f"C:/Users/e x a i d e n/Music/{song}.mp3"
        self.song_mut = MP3(song)
        song_length = self.song_mut.info.length
        self.converted_song_length = time.strftime("%M:%S", time.gmtime(song_length))
        self.status_bar.config(
            text=f"{self.converted_current_time} / {self.converted_song_length}"
        )
        self.status_bar.after(1000, self.play_time)

    def play(self):
        song = self.song_box.get(ACTIVE)
        song = f"C:/Users/e x a i d e n/Music/{song}.mp3"
        pygame.mixer.music.load(song)
        pygame.mixer.music.play(loops=0)
        self.play_time()

    def back(self):
        next_one = self.song_box.curselection()
        next_one = next_one[0] - 1
        song = self.song_box.get(next_one)
        song = f"C:/Users/e x a i d e n/Music/{song}.mp3"
        pygame.mixer.music.load(song)
        pygame.mixer.music.play(loops=0)
        self.song_box.selection_clear(0, END)
        self.song_box.activate(next_one)
        self.song_box.selection_set(next_one, last=None)

    def forward(self):
        next_one = self.song_box.curselection()
        next_one = next_one[0] + 1
        song = self.song_box.get(next_one)
        song = f"C:/Users/e x a i d e n/Music/{song}.mp3"
        pygame.mixer.music.load(song)
        pygame.mixer.music.play(loops=0)
        self.song_box.selection_clear(0, END)
        self.song_box.activate(next_one)
        self.song_box.selection_set(next_one, last=None)

    def stop(self):
        pygame.mixer.music.stop()
        self.song_box.selection_clear(ACTIVE)
        self.status_bar.config(text="")

    def remove_selected(self):
        self.song_box.delete(ANCHOR)
        pygame.mixer.music.stop()

    def remove_all(self):
        self.song_box.delete(0, END)
        pygame.mixer.music.stop()


if __name__ == "__main__":
    Main()

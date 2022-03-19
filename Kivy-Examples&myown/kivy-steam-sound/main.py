from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button
from kivy.lang import Builder
import pygame

pygame.mixer.init()


KV = """
GridLayout
    display: entry
    rows: 1
    padding: 10
    spacing: 10
    BoxLayout:
        spacing: 10
        Button:
            id: entry
            text: "Steam Sound"
            on_press: app.sound()
            font_size: 70
"""


class MyApp(App):
    def build(self):
        pygame.mixer.music.load("steam.wav")
        return Builder.load_string(KV)

    def sound(self):
        pygame.mixer.music.play()


MyApp().run()

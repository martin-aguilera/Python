from kivy.app import App
from kivy.lang import Builder
from kivy.uix.gridlayout import GridLayout

KV = """
GridLayout
    display: entry
    rows: 3
    padding: 10
    spacing: 10
    BoxLayout:
        TextInput:
            id: entry
            font_size: 20

"""


class MyApp(App):
    def build(self):
        return Builder.load_string(KV)


MyApp().run()

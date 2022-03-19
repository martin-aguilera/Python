from kivy.app import App
from kivy.lang import Builder
from kivy.uix.gridlayout import GridLayout
from python_percentage import get_percentage as percent
from math import sin, asin, cos, acos, tan, atan, sqrt, log, hypot, exp
from math import pi as π, radians as rad, fabs as abs

KV = """
GridLayout
    display: entry
    rows: 6
    padding: 10
    spacing: 10
    BoxLayout:
        TextInput:
            id: entry
            font_size: 25
    BoxLayout:
        spacing: 10
        Button:
            text: "rad"
            on_press: entry.text += self.text + "("
            font_size: 22
        Button:
            text: "sin"
            on_press: entry.text += self.text + "("
            font_size: 22
        Button:
            text: "sin⁻¹"
            on_press: entry.text += "asin("
            font_size: 22
        Button:
            text: "%"
            on_press: entry.text += "percent("
            font_size: 22
        Button:
            text: "("
            on_press: entry.text += self.text
            font_size: 22
        Button:
            text: ")"
            on_press: entry.text += self.text
            font_size: 22
        Button:
            text: "Del"
            on_press: entry.text = ""
            font_size: 22
    BoxLayout:
        spacing: 10
        Button:
            text: "abs"
            on_press: entry.text += self.text + "("
            font_size: 22
        Button:
            text: "cos"
            on_press: entry.text += self.text + "("
            font_size: 22
        Button:
            text: "cos⁻¹"
            on_press: entry.text += "acos("
            font_size: 22
        Button:
            background_normal: ""
            background_color: (1, 116/255, 0)
            text: "7"
            on_press: entry.text += self.text
            font_size: 22
        Button:
            background_normal: ""
            background_color: (1, 116/255, 0)
            text: "8"
            on_press: entry.text += self.text
            font_size: 22
        Button:
            background_normal: ""
            background_color: (1, 116/255, 0)
            text: "9"
            on_press: entry.text += self.text
            font_size: 22
        Button:
            text: "+"
            on_press: entry.text += self.text
            font_size: 22
    BoxLayout:
        spacing: 10
        Button:
            text: "hypot"
            on_press: entry.text += self.text + "("
            font_size: 22
        Button:
            text: "tan"
            on_press: entry.text += self.text + "("
            font_size: 22
        Button:
            text: "tan⁻¹"
            on_press: entry.text += "atan("
            font_size: 22
        Button:
            background_normal: ""
            background_color: (1, 116/255, 0)
            text: "4"
            on_press: entry.text += self.text
            font_size: 22
        Button:
            background_normal: ""
            background_color: (1, 116/255, 0)
            text: "5"
            on_press: entry.text += self.text
            font_size: 22
        Button:
            background_normal: ""
            background_color: (1, 116/255, 0)
            text: "6"
            on_press: entry.text += self.text
            font_size: 22
        Button:
            text: "-"
            on_press: entry.text += self.text
            font_size: 22
    BoxLayout:
        spacing: 10
        Button:
            text: "exp"
            on_press: entry.text += self.text + "("
            font_size: 22
        Button:
            text: "π"
            on_press: entry.text += self.text
            font_size: 22
        Button:
            text: "log"
            on_press: entry.text += self.text + "("
            font_size: 22
        Button:
            background_normal: ""
            background_color: (1, 116/255, 0)
            text: "1"
            on_press: entry.text += self.text
            font_size: 22
        Button:
            background_normal: ""
            background_color: (1, 116/255, 0)
            text: "2"
            on_press: entry.text += self.text
            font_size: 22
        Button:
            background_normal: ""
            background_color: (1, 116/255, 0)
            text: "3"
            on_press: entry.text += self.text
            font_size: 22
        Button:
            text: "*"
            on_press: entry.text += self.text
            font_size: 22
    BoxLayout:
        spacing: 10
        Button:
            text: "round"
            on_press: entry.text += self.text + "("
            font_size: 22
        Button:
            text: "√"
            on_press: entry.text += "sqrt("
            font_size: 22
        Button:
            text: ","
            on_press: entry.text += self.text
            font_size: 22
        Button:
            text: "."
            on_press: entry.text += self.text
            font_size: 22
        Button:
            background_normal: ""
            background_color: (1, 116/255.0, 0)
            text: "0"
            on_press: entry.text += self.text
            font_size: 25
        Button:
            text: "="
            on_press: app.calc(entry.text)
            font_size: 22
        Button:
            text: "/"
            on_press: entry.text += self.text
            font_size: 22
"""


class MyApp(App):
    def build(self):
        return Builder.load_string(KV)  # Lee el string KV y construye la interfaz.

    def calc(self, form):  # Se hace la logica para el funcionamiento de la calculadora.
        try:
            self.root.display.text = str(eval(form))
        except SyntaxError:
            self.root.display.text = "SyntaxError, Dumbass."
        except TypeError:
            self.root.display.text = "TypeError, Dumbass."
        except NameError:
            self.root.display.text = "NameError, Wtf are you doing?"
        except ValueError:
            self.root.display.text = "ValueError, Try another number, dumbass."


MyApp().run()

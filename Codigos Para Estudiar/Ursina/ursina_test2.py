from math import modf
from ursina import *
from ursina import texture


class Test_cube(Entity):
    def __init__(self):
        super().__init__(
            model="cube",
            color=color.white,
            texture="white_cube",
            rotation=Vec3(45, 45, 45),
        )


class Test_button(Button):
    def __init__(self):
        super().__init__(
            parent=scene,
            model="cube",
            texture="brick",
            color=color.blue,
            highlight_color=color.red,
            pressed_color=color.lime,
        )

    def input(self, key):
        if self.hovered:
            if key == "left mouse down":
                print("click")


app = Ursina()

test_cube = Test_button()

app.run()

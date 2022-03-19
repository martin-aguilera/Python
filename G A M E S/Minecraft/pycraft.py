from ursina import (
    Ursina,
    load_texture,
    Audio,
    window,
    held_keys,
    Button,
    scene,
    color,
    random,
    mouse,
    destroy,
    Entity,
    camera,
    Vec2,
    Vec3,
)
from ursina.prefabs.first_person_controller import FirstPersonController

app = Ursina()
grass_texture = load_texture("assets/textures/grass_block.png")
stone_texture = load_texture("assets/textures/stone_block.png")
brick_texture = load_texture("assets/textures/brick_block.png")
dirt_texture = load_texture("assets/textures/dirt_block.png")
sky_texture = load_texture("assets/textures/skybox.png")
arm_texture = load_texture("assets/textures/arm_texture.png")
grass_icon = load_texture("assets/icons/grass.png")
stone_icon = load_texture("assets/icons/stone.png")
brick_icon = load_texture("assets/icons/brick.png")
dirt_icon = load_texture("assets/icons/dirt.png")
punch_sound = Audio("assets/audio/punch_sound", loop=False, autoplay=False)
music = Audio("assets/audio/1.mp3", loop=True, autoplay=True)
block_pick = 1
music.play()

window.fps_counter.enabled = False
window.exit_button.visible = False


def update():
    global block_pick

    if held_keys["left mouse"] or held_keys["right mouse"]:
        hand.active()
    else:
        hand.passive()

    if held_keys["1"]:
        block_pick = 1
    if held_keys["2"]:
        block_pick = 2
    if held_keys["3"]:
        block_pick = 3
    if held_keys["4"]:
        block_pick = 4

    if block_pick == 1:
        Object_icon(texture=grass_icon)
    elif block_pick == 2:
        Object_icon(texture=stone_icon)
    elif block_pick == 3:
        Object_icon(texture=brick_icon)
    elif block_pick == 4:
        Object_icon(texture=dirt_icon)


class Voxel(Button):
    def __init__(self, position=(0, 0, 0), texture=grass_texture):
        super().__init__(
            parent=scene,
            position=position,
            model="assets/textures/block",
            origin_y=0.5,
            texture=texture,
            color=color.color(0, 0, random.uniform(0.9, 1)),
            scale=0.5,
        )

    def input(self, key):
        if self.hovered:
            if key == "left mouse down":
                punch_sound.play()
                if block_pick == 1:
                    Voxel(position=self.position + mouse.normal, texture=grass_texture)
                if block_pick == 2:
                    Voxel(position=self.position + mouse.normal, texture=stone_texture)
                if block_pick == 3:
                    Voxel(position=self.position + mouse.normal, texture=brick_texture)
                if block_pick == 4:
                    Voxel(position=self.position + mouse.normal, texture=dirt_texture)

            if key == "right mouse down":
                punch_sound.play()
                destroy(self)


class Sky(Entity):
    def __init__(self):
        super().__init__(
            parent=scene,
            model="sphere",
            texture=sky_texture,
            scale=150,
            double_sided=True,
        )


class Hand(Entity):
    def __init__(self):
        super().__init__(
            parent=camera.ui,
            model="assets/textures/arm",
            texture=arm_texture,
            scale=0.2,
            rotation=Vec3(150, -10, 0),
            position=Vec2(0.4, -0.6),
        )

    def active(self):
        self.position = Vec2(0.3, -0.5)

    def passive(self):
        self.position = Vec2(0.4, -0.6)


class Selection_bar(Entity):
    def __init__(self):
        super().__init__(
            parent=camera.ui,
            model="quad",
            color=color.gray,
            scale=(0.1, 0.1),
            position=Vec2(-0.8, 0.42),
        )


class Object_icon(Entity):
    def __init__(self, texture=grass_icon):
        super().__init__(
            parent=camera.ui,
            model="quad",
            texture=texture,
            scale=(0.08, 0.08),
            position=Vec2(-0.8, 0.42),
        )


bar = Selection_bar()
icon = Object_icon()
for z in range(20):
    for x in range(20):
        Voxel(position=(x, 0, z))
player = FirstPersonController()
sky = Sky()
hand = Hand()
app.run()

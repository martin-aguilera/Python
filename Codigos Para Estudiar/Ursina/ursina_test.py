from ursina import *


def update():
    if held_keys["a"]:
        pika.x -= 4.1 * time.dt
    elif held_keys["d"]:
        pika.x += 4.1 * time.dt
    if held_keys["w"]:
        pika.y += 4.1 * time.dt
    elif held_keys["s"]:
        pika.y -= 4.1 * time.dt


app = Ursina()


# test_square = Entity(model = 'quad', color = color.red, scale = (1, 1), position = (1, 1))
pika_texture = load_texture("pika.png")
pika = Entity(model="quad", texture=pika_texture, scale=(2, 2))


app.run()

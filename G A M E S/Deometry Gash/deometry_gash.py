from ursina import Ursina, Entity, camera, color, time, curve, duplicate, invoke

app = Ursina()

background = Entity(model="quad", texture="assets/bg.jpg", scale=55, z=10, y=15)

camera.orthographic = True
camera.fov = 17

player = Entity(model="quad", collider="box", texture="assets/cube1.png", x=-8)

ground = Entity(
    model="cube",
    color=color.lime,
    y=-1,
    origin_y=0.5,
    scale=(200, 15, 1),
    collider="box",
    texture="white_cube",
)

diam = []
plates = []


def new_obstacle(val):
    new1 = Entity(
        model="diamond",
        color=color.violet,
        y=-0.5,
        texture="white_cube",
        x=val,
        collider="mesh",
    )
    new2 = duplicate(new1, y=0.35, x=val + 1, scale=0.8)
    diam.extend((new1, new2))
    if val % 60 > 40:
        for i in range(5):
            e = Entity(
                model="cube",
                y=i - 0.5,
                x=val + 5 + i * 7,
                scale_x=3,
                collider="box",
                color=color.lime,
                texture="white_cube",
            )
            plates.append(e)
    invoke(new_obstacle, val=val + 10, delay=1)


new_obstacle(30)


def update():
    for ob in diam:
        ob.x -= 10 * time.dt
    for ob in plates:
        ob.x -= 10 * time.dt
    if not player.intersects().hit:
        player.y -= 7 * time.dt
    player.y = max(-0.5, player.y)
    t = player.intersects()
    if t.hit:
        for en in t.entities:
            if en.color == color.violet:
                quit()


def input(key):
    if key == "space":
        if player.intersects().hit:
            player.animate_y(player.y + 3, duration=0.2, curve=curve.out_sine)
            player.animate_rotation_z(
                player.rotation_z + 180, duration=0.6, curve=curve.linear
            )
            dust = Entity(
                model="circle", scale=-3, color=color.smoke, position=player.position
            )
            dust.animate_scale(2, duration=0.3, curve=curve.linear)
            dust.fade_out(duration=0.3)


app.run()

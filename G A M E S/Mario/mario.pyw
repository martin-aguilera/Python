import arcade, os
from pygame import mixer

mixer.init()
os.system("cls")

# Constantes
SCREEN_WIDTH = 1250
SCREEN_HEIGHT = 700
SCREEN_TITLE = "Super Mario CTM"

# Constantes para escalar los sprites
CHARACTER_SCALING = 0.17
GROUND_SCALING = 0.17
CYLINDER_SCALING = 0.20
FLOWER_SCALING = 1
ENEMIES_SCALING = 0.17
COIN_SCALING = 0.07
RUPEE_SCALING = 0.03
CLOUD_SCALING = 0.6
BUSH_SCALING = 0.3

LEFT_VIEWPORT_MARGIN = 200
RIGHT_VIEWPORT_MARGIN = 250
BOTTOM_VIEWPORT_MARGIN = 250
TOP_VIEWPORT_MARGIN = 250

# Valocidad del jugador
PLAYER_MOVEMENT_SPEED = 5
GRAVITY = 1
PLAYER_JUMP_SPEED = 20

# char = ["pikachu00", "charizard00"]
# choice = random.choice(char)

jump_sound = mixer.Sound("assets/sound/small_jump.ogg")
jump_bump = mixer.Sound("assets/sound/bump.ogg")
coin_sound = mixer.Sound("assets/sound/coin.ogg")
mixer.music.load("assets/music/main_theme.ogg")
mixer.music.set_volume(1.7)
mixer.music.play(loops=-1)


'''class InstructionView(arcade.View):

    def __init__(self):
        super().__init__()
        self.texture = arcade.load_texture("assets/cover.png")
        # Restablecer la ventana gráfica, necesaria si tenemos un juego de desplazamiento y necesitamos
        # para restablecer la ventana gráfica al inicio para que podamos ver lo que dibujamos.
        arcade.set_viewport(0, SCREEN_WIDTH - 1, 0, SCREEN_HEIGHT - 1)

    def on_draw(self):
        """ Dibuja esta vista """
        arcade.start_render()
        self.texture.draw_sized(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2, SCREEN_WIDTH, SCREEN_HEIGHT)

    def on_mouse_press(self, _x, _y, _button, _modifiers):
        """ Si el usuario presiona el botón del mouse, inicia el juego. """
        game_view = MyGame()
        game_view.setup()
        self.window.show_view(game_view)'''


class Collectable(arcade.Sprite):
    def __init__(self, filename, scale):
        super().__init__(filename, scale)
        self.changed = False


class Mygame(arcade.Window):
    def __init__(self):
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
        arcade.set_background_color(arcade.csscolor.CORNFLOWER_BLUE)
        self.text_angle = 0
        self.time_elapsed = 0.0

        self.wall_list = None
        self.player_list = None
        self.background_list = None
        self.background_list_2 = None
        self.enemy_list = None
        self.coin_list = None
        self.rupee_list = None
        # Variable del sprite jugador#
        self.player_sprite = None
        self.view_bottom = 0
        self.view_left = 0

    def setup(self):
        self.player_list = arcade.SpriteList()
        self.wall_list = arcade.SpriteList()
        self.coin_list = arcade.SpriteList()
        self.rupee_list = arcade.SpriteList()
        self.background_list = arcade.SpriteList()
        self.background_list_2 = arcade.SpriteList()

        ### PLAYER ###
        image_source = "assets/characters/pikachu00.png"  # .format(choice)
        self.player_sprite = arcade.Sprite(image_source, CHARACTER_SCALING)
        self.player_sprite.center_x = 64
        self.player_sprite.center_y = 93
        self.player_list.append(self.player_sprite)

        self.view_bottom = 0
        self.view_left = 0
        self.score = 0

        ### COINS ###
        for i in range(1120, 1135, 30):
            # Create the coin instance
            coin = Collectable("assets/objects/Coin1.png", COIN_SCALING)
            coin.center_x = i
            coin.center_y = 270
            self.coin_list.append(coin)
        for i in range(1405, 1510, 30):
            # Create the coin instance
            coin = Collectable("assets/objects/Coin1.png", COIN_SCALING)
            coin.center_x = i
            coin.center_y = 396
            self.coin_list.append(coin)
        for i in range(1655, 1675, 30):
            # Create the coin instance
            coin = Collectable("assets/objects/Coin1.png", COIN_SCALING)
            coin.center_x = i
            coin.center_y = 250
            self.coin_list.append(coin)
        for i in range(1755, 1935, 30):
            # Create the coin instance
            coin = Collectable("assets/objects/Coin1.png", COIN_SCALING)
            coin.center_x = i
            coin.center_y = 520
            self.coin_list.append(coin)
        for i in range(1755, 1935, 30):
            # Create the coin instance
            coin = Collectable("assets/objects/Coin1.png", COIN_SCALING)
            coin.center_x = i
            coin.center_y = 555
            self.coin_list.append(coin)
        for i in range(1755, 1935, 30):
            # Create the coin instance
            coin = Collectable("assets/objects/Coin1.png", COIN_SCALING)
            coin.center_x = i
            coin.center_y = 590
            self.coin_list.append(coin)
        for i in range(1755, 1935, 30):
            # Create the coin instance
            coin = Collectable("assets/objects/Coin1.png", COIN_SCALING)
            coin.center_x = i
            coin.center_y = 626
            self.coin_list.append(coin)
        # RUPEE
        for r in range(2135, 2155, 30):
            # Create the coin instance
            rupee = Collectable("assets/objects/rupee.png", RUPEE_SCALING)
            rupee.center_x = r
            rupee.center_y = 600
            self.rupee_list.append(rupee)

        ###ENEMIES###

        # CREAR EL PISO
        for x in range(-600, 1600, 55):
            wall = arcade.Sprite(
                "assets/ground n walls/brickblock01.png", GROUND_SCALING
            )
            wall.center_x = x
            wall.center_y = -20
            self.wall_list.append(wall)
        for x in range(1770, 4000, 55):
            wall = arcade.Sprite(
                "assets/ground n walls/brickblock01.png", GROUND_SCALING
            )
            wall.center_x = x
            wall.center_y = -20
            self.wall_list.append(wall)
        for x in range(4720, 8000, 55):
            wall = arcade.Sprite(
                "assets/ground n walls/brickblock01.png", GROUND_SCALING
            )
            wall.center_x = x
            wall.center_y = -20
            self.wall_list.append(wall)
        for x in range(-600, 1600, 55):
            wall = arcade.Sprite("assets/ground n walls/ground.png", GROUND_SCALING)
            wall.center_x = x
            wall.center_y = 32
            self.wall_list.append(wall)
        for x in range(1770, 4000, 55):
            wall = arcade.Sprite("assets/ground n walls/ground.png", GROUND_SCALING)
            wall.center_x = x
            wall.center_y = 32
            self.wall_list.append(wall)
        for x in range(4720, 8000, 55):
            wall = arcade.Sprite("assets/ground n walls/ground.png", GROUND_SCALING)
            wall.center_x = x
            wall.center_y = 32
            self.wall_list.append(wall)
        for x in range(4220, 4500, 250):
            wall = arcade.Sprite(
                "assets/ground n walls/mysteryblockused.png", GROUND_SCALING
            )
            wall.center_x = x
            wall.center_y = 90
            self.wall_list.append(wall)

        # Bloques misticos
        for bm in range(695, 795, 55):
            wall = arcade.Sprite(
                "assets/ground n walls/mysterybloc.png", GROUND_SCALING
            )
            wall.center_x = bm
            wall.center_y = 230
            self.wall_list.append(wall)
        for bm in range(2300, 2400, 55):
            wall = arcade.Sprite(
                "assets/ground n walls/mysterybloc.png", GROUND_SCALING
            )
            wall.center_x = bm
            wall.center_y = 230
            self.wall_list.append(wall)

        # Parte de a bajo de los Hongos
        coord_mush_bottom_list = [
            [1120, 123],
            [1450, 123],
            [1450, 250],
            [1830, 123],
            [1830, 250],
            [1830, 373],
        ]

        for coord in coord_mush_bottom_list:
            wall = arcade.Sprite(
                "assets/ground n walls/mushroomstick.png", CYLINDER_SCALING
            )
            wall.position = coord
            self.background_list.append(wall)

        # Parte de arriba de los Hongos
        coord_mush_top_list = [[1120, 218], [1450, 345], [1830, 468]]
        for coordinate in coord_mush_top_list:
            wall = arcade.Sprite(
                "assets/ground n walls/mushroomplatform.png", CYLINDER_SCALING
            )
            wall.position = coordinate
            self.wall_list.append(wall)

        # Pipes
        coord_pipe04_list = [
            [-100, 202],
            [-200, 202],
            [-300, 202],
            [7400, 202],
            [7500, 202],
            [7600, 202],
            [7700, 202],
            [7800, 202],
            [7900, 202],
            [8000, 202],
        ]
        for coordinate in coord_pipe04_list:
            # Add a crate on the ground
            wall = arcade.Sprite(
                "assets/ground n walls/Pipes/New/new_pipe04.png", CYLINDER_SCALING
            )
            wall.position = coordinate
            self.wall_list.append(wall)

        coord_pipe02_list = [[2100, 130], [2550, 130]]
        for coordinate in coord_pipe02_list:
            # Add a crate on the ground
            wall = arcade.Sprite(
                "assets/ground n walls/Pipes/New/new_pipe02.png", CYLINDER_SCALING
            )
            wall.position = coordinate
            self.wall_list.append(wall)

        # COLINAS
        for hl in range(200, 1500, 650):
            # Add Flowers
            hill = arcade.Sprite("assets/objects/bg_hill.png", ENEMIES_SCALING)
            hill.center_x = hl
            hill.center_y = 100
            self.background_list_2.append(hill)
        for hl in range(1900, 4000, 760):
            hill = arcade.Sprite("assets/objects/bg_hill.png", ENEMIES_SCALING)
            hill.center_x = hl
            hill.center_y = 100
            self.background_list_2.append(hill)
        for hl in range(5100, 8000, 760):
            hill = arcade.Sprite("assets/objects/bg_hill.png", ENEMIES_SCALING)
            hill.center_x = hl
            hill.center_y = 100
            self.background_list_2.append(hill)

        # Arbustos
        for bsh in range(500, 1500, 650):
            # Add Flowers
            bush = arcade.Sprite("assets/objects/bg_bush.png", BUSH_SCALING)
            bush.center_x = bsh
            bush.center_y = 90
            self.background_list_2.append(bush)
        for bsh in range(2250, 4000, 760):
            bush = arcade.Sprite("assets/objects/bg_bush.png", BUSH_SCALING)
            bush.center_x = bsh
            bush.center_y = 90
            self.background_list_2.append(bush)
        for bsh in range(4800, 8000, 760):
            bush = arcade.Sprite("assets/objects/bg_bush.png", BUSH_SCALING)
            bush.center_x = bsh
            bush.center_y = 90
            self.background_list_2.append(bush)

        # FLORES
        for fl in range(50, 1560, 150):
            # Add Flowers
            flower = arcade.Sprite("assets/objects/flowers.png", FLOWER_SCALING)
            flower.center_x = fl
            flower.center_y = 72
            self.background_list.append(flower)
        for fl in range(1770, 4000, 150):
            # Add Flowers
            flower = arcade.Sprite("assets/objects/flowers.png", FLOWER_SCALING)
            flower.center_x = fl
            flower.center_y = 72
            self.background_list.append(flower)
        for fl in range(4800, 8000, 150):
            # Add Flowers
            flower = arcade.Sprite("assets/objects/flowers.png", FLOWER_SCALING)
            flower.center_x = fl
            flower.center_y = 72
            self.background_list.append(flower)

        # NUBES
        for cl in range(250, 8000, 650):
            # Add Flowers
            cloud = arcade.Sprite("assets/objects/bg_cloud.png", CLOUD_SCALING)
            cloud.center_x = cl
            cloud.center_y = 550
            self.background_list.append(cloud)

        ### CASTILLO ###
        coord_castle = [7160, 239]
        castle = arcade.Sprite("assets/objects/castle01.png", BUSH_SCALING)
        castle.position = coord_castle
        self.background_list.append(castle)

        # Motor de fisica
        self.physics_engine = arcade.PhysicsEnginePlatformer(
            self.player_sprite, self.wall_list, GRAVITY
        )

    def on_key_press(self, key, modifiers):
        if key == arcade.key.UP:
            if self.physics_engine.can_jump():
                jump_sound.play()
                jump = self.player_sprite.change_y = PLAYER_JUMP_SPEED

        elif key == arcade.key.LEFT:
            go_left = self.player_sprite.change_x = -PLAYER_MOVEMENT_SPEED

        elif key == arcade.key.RIGHT:
            go_right = self.player_sprite.change_x = PLAYER_MOVEMENT_SPEED

    def on_key_release(self, key, modifiers):
        if key == arcade.key.LEFT:
            go_left = self.player_sprite.change_x = 0

        elif key == arcade.key.RIGHT:
            go_right = self.player_sprite.change_x = 0

    def on_draw(self):
        print(self.score)

        arcade.start_render()
        self.background_list_2.draw()
        self.wall_list.draw()
        self.background_list.draw()
        self.coin_list.draw()
        self.rupee_list.draw()
        self.player_list.draw()

    def on_update(self, delta_time):
        self.text_angle += 1
        self.time_elapsed += delta_time

        hit_list = arcade.check_for_collision_with_list(
            self.player_sprite, self.coin_list
        )
        for coin in hit_list:
            # Have we collected this?
            if not coin.changed:
                coin.kill()
                coin_sound.play()
                coin.changed = True
                self.score += 1

        hit_list1 = arcade.check_for_collision_with_list(
            self.player_sprite, self.rupee_list
        )
        for coin in hit_list1:
            # Have we collected this?
            if not coin.changed:
                coin.kill()
                coin_sound.play()
                coin.changed = True
                self.score += 10

        changed = False

        # Desplazarse a la iquierda
        left_boundary = self.view_left + LEFT_VIEWPORT_MARGIN
        if self.player_sprite.left < left_boundary:
            self.view_left -= left_boundary - self.player_sprite.left
            changed = True

            # Desplazarse a la derecha
        right_boundary = self.view_left + SCREEN_WIDTH - RIGHT_VIEWPORT_MARGIN - 350
        if self.player_sprite.right > right_boundary:
            self.view_left += self.player_sprite.right - right_boundary
            changed = True

        if changed:
            # Solo desplazamiento en enteros. De lo contrario, terminamos con píxeles que
            # no se alineen en la pantalla
            self.view_bottom = int(self.view_bottom)
            self.view_left = int(self.view_left)

            # Hacer el seguimiento
        arcade.set_viewport(
            self.view_left,
            SCREEN_WIDTH + self.view_left,
            self.view_bottom,
            SCREEN_HEIGHT + self.view_bottom,
        )

        self.physics_engine.update()


def main():
    window = Mygame()
    # 	start_view = InstructionView()
    window.setup()
    arcade.run()


if __name__ == "__main__":
    main()

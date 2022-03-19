import pygame, sys, random
from random import choice

pygame.init()
pygame.font.init()

# Constantes																				  		  #
ANCHO = 900  #
ALTO = 600  #

NEGRO = (000, 000, 000)  #
AZUL = (000, 000, 255)  #
VERDE = (000, 255, 000)  #
CELESTE = (000, 255, 255)  #
ROJO = (255, 000, 000)  #
MORADO = (255, 000, 255)  #
AMARILLO = (255, 255, 000)  #
BLANCO = (255, 255, 255)  #
NARANJA = (255, 125, 000)  #
ROSADO = (255, 000, 125)  #
LIMA = (185, 255, 000)  #

colores = [
    AZUL,
    VERDE,
    CELESTE,
    ROJO,
    MORADO,  #
    AMARILLO,
    BLANCO,
    NARANJA,
    ROSADO,
    LIMA,
]  #

the_backgrounds = ["assets/1.png", "assets/2.jpg", "assets/3.png", "assets/4.png"]  #

score_value = 0  #
high_score_value = 0  #

font = pygame.font.SysFont("comicsansms", 40)  #
score = font.render(("Score: " + str(score_value)), True, BLANCO)  #
high_score = font.render(("High Score: " + str(high_score_value)), True, BLANCO)  #

colores_aleatorio = choice(colores)  #
background_aleatorio = choice(the_backgrounds)  #

# Jugador
jugador_size_x = 150
jugador_size_y = 20
jugador_pos = [ANCHO / 2, ALTO - jugador_size_y * 2]
# Velocidad de movimiento
speed_x = 0
speed_y = 0
# Frutas
fruit_size = 25  #
fruit_pos = [random.randint(10, ANCHO - fruit_size), 0]  #

# Ventana del juego																	  			  #
ventana = pygame.display.set_mode((ANCHO, ALTO))  #
background = pygame.image.load(background_aleatorio).convert()  #

game_over = False  #
clock = pygame.time.Clock()  #

# Funciones																	  					  #
def detectar_colision(jugador_pos, fruit_pos):  #
    jx = jugador_pos[0]  #
    jy = jugador_pos[1]  #
    ex = fruit_pos[0]  #
    ey = fruit_pos[1]  #

    if (ex >= jx and ex < (jx + jugador_size_x)) or (
        jx >= ex and jx < (ex + fruit_size)
    ):  #
        if (ey >= jy and ey < (jy + jugador_size_y)) or (
            jy >= ey and jy < (ey + fruit_size)
        ):  #
            return True  #
    return False  #


while not game_over:  #
    for event in pygame.event.get():  #
        if event.type == pygame.QUIT:
            sys.exit()

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                speed_x = -10
            if event.key == pygame.K_RIGHT:
                speed_x = 10

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                speed_x = 0
            if event.key == pygame.K_RIGHT:
                speed_x = 0

    ventana.blit(background, [0, 0])

    jugador_pos[0] += speed_x

    if fruit_pos[1] >= 0 and fruit_pos[1] < ALTO:  #
        fruit_pos[1] += 10  #
    else:  #
        fruit_pos[0] = random.randint(0, ANCHO - fruit_size)  #
        fruit_pos[1] = 0  #
        colores_aleatorio = choice(colores)  #

    # Coliciones													  	  							  #
    if detectar_colision(jugador_pos, fruit_pos):  #
        score_value = score_value + 2.5  #
        if score_value > high_score_value:  #
            high_score_value = score_value  #
            score = font.render(("Score: " + str(int(score_value))), True, BLANCO)  #
            high_score = font.render(
                ("High Score: " + str(int(high_score_value))), True, BLANCO
            )

    # Dibujar frutas
    pygame.draw.circle(
        ventana, colores_aleatorio, (fruit_pos[0], fruit_pos[1]), fruit_size
    )

    # Dibujar jugador
    pygame.draw.rect(
        ventana,
        ROJO,
        (jugador_pos[0], jugador_pos[1], jugador_size_x, jugador_size_y),
        4,
    )

    ventana.blit(score, (ANCHO / 7.5 - score.get_rect().width / 2, ALTO / 5 - 100))  #
    ventana.blit(
        high_score, (ANCHO / 1.25 - high_score.get_rect().width / 2, ALTO / 5 - 100)
    )  # 																							  #
    clock.tick(60)  #
    pygame.display.update()  #

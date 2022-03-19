import pygame, sys, random  #
from random import choice  #

pygame.init()
pygame.font.init()

# Constantes																				  		  #
ANCHO = 900  #
ALTO = 600
# Jugador
jugador_size_x = 150
jugador_size_y = 20
jugador_pos = [400, 560]

# Velocidad de movimiento
speed_x = 0
speed_y = 0
# Frutas
fruit_size = 25
fruit_pos = [random.randint(fruit_size, ANCHO - fruit_size), 0]

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

score_value = 0  # 																			  #

font = pygame.font.SysFont("comicsansms", 40)  #
score = font.render(("Score: " + str(score_value)), True, BLANCO)

colores_aleatorio = choice(colores)
background_aleatorio = choice(the_backgrounds)

# Ventana del juego																	  			  #
ventana = pygame.display.set_mode((ANCHO, ALTO))  #
background = pygame.image.load(background_aleatorio).convert()  #

game_over = False  #
clock = pygame.time.Clock()

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
        colores_aleatorio = choice(colores)

    # Dibujar frutas
    fruit = pygame.draw.circle(
        ventana, colores_aleatorio, (fruit_pos[0], fruit_pos[1]), fruit_size
    )
    # Dibujar jugador
    player = pygame.draw.rect(
        ventana,
        ROJO,
        (jugador_pos[0], jugador_pos[1], jugador_size_x, jugador_size_y),
        4,
    )
    # pygame.draw.line(ventana, BLANCO, (400, 570), (550,570),25)

    # coliciones
    if fruit.colliderect(player):
        score_value += 10 / 7
        score = font.render(("Score: " + str(int(score_value))), True, BLANCO)
        fruit.remove(fruit)

    ventana.blit(score, (ANCHO / 7.5 - score.get_rect().width / 2, ALTO / 5 - 100))
    clock.tick(60)  #
    pygame.display.update()

import pygame, sys

pygame.init()
pygame.font.init()

# Colores
black = (000, 000, 000)
white = (255, 255, 255)
screen_size = (800, 600)
player_width = 15
player_height = 90

screen = pygame.display.set_mode(screen_size)
clock = pygame.time.Clock()

score_p1 = 0
score_p2 = 0
font = pygame.font.SysFont("comicsansms", 40)
score_1 = font.render(("Player A:  " + str(score_p1)), True, white)
score_2 = font.render(("Player B:  " + str(score_p2)), True, white)

# Coordenadas y Valocidad del jugador 1
player1_x_coord = 50
player1_y_coord = 255
player1_y_speed = 0

# Coordenadas y Valocidad del jugador 2
player2_x_coord = 750 - player_width
player2_y_coord = 255
player2_y_speed = 0

# Coordenadas de la pelota
ball_x = 400
ball_y = 300
ball_speed_x = 3
ball_speed_y = 3

game_over = False

while not game_over:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True
        if event.type == pygame.KEYDOWN:
            # jugador 1
            if event.key == pygame.K_w:
                player1_y_speed = -3
            if event.key == pygame.K_s:
                player1_y_speed = 3
            # Jugador 2
            if event.key == pygame.K_UP:
                player2_y_speed = -3
            if event.key == pygame.K_DOWN:
                player2_y_speed = 3

        if event.type == pygame.KEYUP:
            # jugador 1
            if event.key == pygame.K_w:
                player1_y_speed = 0
            if event.key == pygame.K_s:
                player1_y_speed = 0
            # Jugador 2
            if event.key == pygame.K_UP:
                player2_y_speed = 0
            if event.key == pygame.K_DOWN:
                player2_y_speed = 0

    if ball_y > 590 or ball_y < 10:
        ball_speed_y *= -1

    # Revisa si la pelota sale del lado derecho
    if ball_x > 800:
        score_p1 = score_p1 + 1
        ball_x = 400
        ball_y = 300
        # Si sale de la pantalla, invierte direccion
        ball_speed_x *= -1
        ball_speed_y *= -1
        score_1 = font.render(("Player A:  " + str(score_p1)), True, white)

    # Revisa si la pelota sale del lado izquierdo
    if ball_x < 0:
        score_p2 = score_p2 + 1
        ball_x = 400
        ball_y = 300
        # Si sale de la pantalla, invierte direccion
        ball_speed_x *= -1
        ball_speed_y *= -1
        score_2 = font.render(("Player B:  " + str(score_p2)), True, white)

    # Modifica las coord. para dar mov. a los jugadores/.
    player1_y_coord += player1_y_speed
    player2_y_coord += player2_y_speed
    # Movimiento Pelota
    ball_x += ball_speed_x
    ball_y += ball_speed_y

    screen.fill(black)
    # Zona de dibujo
    pygame.draw.line(screen, white, (400, 0), (400, 240), 1)
    pygame.draw.line(screen, white, (400, 360), (400, 600), 1)
    pygame.draw.circle(screen, white, [400, 300], 60, 1)
    pygame.draw.rect(screen, white, (0, 0, 800, 600), 5)

    player_1 = pygame.draw.rect(
        screen, white, (player1_x_coord, player1_y_coord, player_width, player_height)
    )
    player_2 = pygame.draw.rect(
        screen, white, (player2_x_coord, player2_y_coord, player_width, player_height)
    )
    ball = pygame.draw.circle(screen, white, (ball_x, ball_y), 10)

    # Coliciones
    if ball.colliderect(player_1) or ball.colliderect(player_2):
        ball_speed_x *= -1

    screen.blit(score_1, (70, 600 / 5 - 100))
    screen.blit(score_2, (500, 600 / 5 - 100))

    pygame.display.flip()
    clock.tick(60)
pygame.quit()

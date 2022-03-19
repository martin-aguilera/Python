from os import pardir
import pygame
from random import randrange as rnd

WIDTH, HEIGHT = 1200, 800
fps = 60

# paddle setting
paddle_w = 330
paddle_h = 35
paddle_speed = 15
paddle = pygame.Rect(
    WIDTH // 2 - paddle_w // 2, HEIGHT - paddle_h - 10, paddle_w, paddle_h
)

pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()

# background
img = pygame.image.load("1.jpg").convert()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
    screen.blit(img, (0, 0))

    # drawing world
    pygame.draw.rect(screen, pygame.Color("darkorange"), paddle)

    # control
    key = pygame.key.get_pressed()
    if key[pygame.K_LEFT] and paddle.left > 0:
        paddle.left -= paddle_speed
    if key[pygame.K_RIGHT] and paddle.right < WIDTH:
        paddle.right += paddle_speed

    if key[pygame.K_LEFT] and key[pygame.K_LSHIFT] and paddle.left > 0:
        paddle.left -= paddle_speed * 2
    if key[pygame.K_RIGHT] and key[pygame.K_LSHIFT] and paddle.right < WIDTH:
        paddle.right += paddle_speed * 2

    pygame.display.flip()
    clock.tick(fps)

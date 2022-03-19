import pygame, sys, time, random
from pygame.locals import *
pygame.init()
pygame.font.init()

width  =   500
height =   500

black  =  (000,000,000)
green  =  (000,255,000)
red    =  (255,000,000)
white  =  (255,255,255)

screen =   pygame.display.set_mode((width,height))
fps    =   pygame.time.Clock()

def food_spawn():
    food_pos     =   [random.randint(0, 49)*10, random.randint(0, 49)*10]
    return food_pos

def main():
    snake_pos    =   [100,50]
    snake_body   =   [[100,50], [90,50], [80,50]]
    direction    =   'RIGHT'
    change       =   direction
    food_pos     =   food_spawn()

    score_value       =   0
    high_score_value  =   0

    font = pygame.font.SysFont("comicsansms", 22)
    score = font.render(("Score: " + str(score_value)), True, white)
    high_score = font.render(("High Score: " + str(high_score_value)), True, white)

    run = True
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    change = 'RIGHT'
                if event.key == pygame.K_LEFT:
                    change = 'LEFT'
                if event.key == pygame.K_UP:
                    change = 'UP'
                if event.key == pygame.K_DOWN:
                    change = 'DOWN'

        if change == 'RIGHT' and direction != 'LEFT':
            direction = 'RIGHT'
        if change == 'LEFT' and direction != 'RIGHT':
            direction = 'LEFT'
        if change == 'UP' and direction != 'DOWN':
            direction = 'UP'
        if change == 'DOWN' and direction != 'UP':
            direction = 'DOWN'
        
        if direction == 'RIGHT':
            snake_pos[0] += 10
        if direction == 'LEFT':
            snake_pos[0] -= 10
        if direction == 'UP':
            snake_pos[1] -= 10
        if direction == 'DOWN':
            snake_pos[1] += 10
        
        snake_body.insert(0, list(snake_pos))
        if snake_pos == food_pos:
            food_pos = food_spawn()
            score_value += 1
            if score_value > high_score_value:
                high_score_value = score_value
                score = font.render(("Score: " + str(int(score_value))), True, white)
                high_score = font.render(("High Score: " + str(int(high_score_value))), True, white)
        else:
            snake_body.pop()

        screen.fill(black)

        for pos in snake_body:
            pygame.draw.rect(screen, green, pygame.Rect(pos[0],pos[1], 10,10))
        pygame.draw.rect(screen, red, pygame.Rect(food_pos[0],food_pos[1], 10,10))

        if snake_pos[0] >= 500 or snake_pos[0] <= 0:
            snake_pos = [100,50]
            snake_body.pop()
            run = False
        if snake_pos[1] >= 500 or snake_pos[1] <= 0:
            snake_pos = [100,50]
            snake_body.pop()
            run = False
        if snake_pos in snake_body[1:]:
            snake_pos = [100,50]
            snake_body.pop()
            run = False

        screen.blit(score, (width/7.5 - score.get_rect( ).width/2, height/5 - 100))
        #screen.blit(high_score, (width/1.25 - high_score.get_rect( ).width/2, height/5 - 100))	

        pygame.display.flip()
        fps.tick(10)

main()
pygame.quit()
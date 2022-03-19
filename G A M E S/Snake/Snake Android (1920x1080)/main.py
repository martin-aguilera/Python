import pygame, random
from enum import Enum
from collections import namedtuple

pygame.init()
font = pygame.font.SysFont("arial", 60)


class Direction(Enum):
    RIGHT = 1
    LEFT = 2
    UP = 3
    DOWN = 4


Point = namedtuple("Point", "x, y")

# rgb colors

BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN1 = (0, 180, 0)
GREEN2 = (0, 255, 0)
GRAY = (20, 20, 20)
WHITE = (255, 255, 255)

BLOCK_SIZE = 20
SPEED = 15

player_rect = pygame.Rect(0, 0, 64, 64)
up_rect = pygame.Rect(300, 100, 50, 50)
down_rect = pygame.Rect(300, 180, 50, 50)


class SnakeGame:
    def __init__(self, w=1080, h=1920):
        self.w = w
        self.h = h
        # init display
        self.high_score = 0
        self.display = pygame.display.set_mode((self.w, self.h))
        pygame.display.set_caption("Snake")
        # pygame.FULLSCREEN
        self.clock = pygame.time.Clock()
        self.reset()

        # init game state

    def reset(self):
        self.direction = Direction.RIGHT
        self.head = Point(self.w / 2, self.h / 2)
        self.snake = [
            self.head,
            Point(self.head.x - BLOCK_SIZE, self.head.y),
            Point(self.head.x - (2 * BLOCK_SIZE), self.head.y),
        ]
        self.score = 0
        self.food = None
        self._place_food()

    def _place_food(self):
        x = random.randint(0, (self.w - BLOCK_SIZE) // BLOCK_SIZE) * BLOCK_SIZE
        y = random.randint(0, (self.h - BLOCK_SIZE) // BLOCK_SIZE) * BLOCK_SIZE
        self.food = Point(x, y)
        if self.food in self.snake:
            self._place_food()

    def play_step(self):
        # 1. collect user input
        for event in pygame.event.get():
            pos = pygame.mouse.get_pos()
            print(pos)
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if pos[0] > 180 and pos[0] < 900 and pos[1] < 360:  ###
                    self.direction = Direction.UP
                elif pos[0] > 180 and pos[0] < 900 and pos[1] > 1550:  ###
                    self.direction = Direction.DOWN
                elif pos[0] < 360 and pos[1] > 588 and pos[1] < 1308:  ###
                    self.direction = Direction.LEFT
                elif pos[0] > 720 and pos[1] > 588 and pos[1] < 1308:
                    self.direction = Direction.RIGHT

        # 2. move
        self._move(self.direction)  # update the head
        self.snake.insert(0, self.head)

        # 3. check if game over
        game_over = False
        if self._is_collision():
            game_over = True
            return game_over, self.score

        # 4. place new food or just move
        if self.head == self.food:
            self.score += 1
            if self.score > self.high_score:
                self.high_score = self.score
            self._place_food()
        else:
            self.snake.pop()

        # 5. update ui and clock
        self._update_ui()
        self.clock.tick(SPEED)

        # 6. return game over and score
        return game_over, self.score

    def _is_collision(self, pt=None):
        if pt is None:
            pt = self.head
        # hits boundary
        if (
            pt.x > self.w - BLOCK_SIZE
            or pt.x < 0
            or pt.y > self.h - BLOCK_SIZE
            or pt.y < 0
        ):
            return True
        # hits itself
        if pt in self.snake[1:]:
            return True
        return False

    def _update_ui(self):
        self.display.fill(BLACK)
        pygame.draw.rect(self.display, GRAY, pygame.Rect(180, 0, 720, 360))  ##
        pygame.draw.rect(self.display, GRAY, pygame.Rect(0, 588, 360, 720))  ##
        pygame.draw.rect(self.display, GRAY, pygame.Rect(180, 1560, 720, 360))  ##
        pygame.draw.rect(self.display, GRAY, pygame.Rect(720, 588, 360, 720))  ##
        pygame.draw.rect(self.display, WHITE, pygame.Rect(0, 0, 1080, 1920), 10)
        # print(self.h - 270)

        for pt in self.snake:
            pygame.draw.rect(
                self.display, GREEN1, pygame.Rect(pt.x, pt.y, BLOCK_SIZE, BLOCK_SIZE)
            )
            pygame.draw.rect(
                self.display, GREEN2, pygame.Rect(pt.x + 4, pt.y + 4, 12, 12)
            )

        pygame.draw.rect(
            self.display,
            RED,
            pygame.Rect(self.food.x, self.food.y, BLOCK_SIZE, BLOCK_SIZE),
        )

        text1 = font.render("Score: " + str(self.score), True, WHITE)
        text2 = font.render("High Score: " + str(self.high_score), True, WHITE)
        self.display.blit(text1, [20, 20])
        self.display.blit(text2, [760, 20])
        pygame.display.flip()

    def _move(self, direction):
        x = self.head.x
        y = self.head.y
        if direction == Direction.RIGHT and direction != Direction.LEFT:
            x += BLOCK_SIZE
        elif direction == Direction.LEFT and direction != Direction.RIGHT:
            x -= BLOCK_SIZE
        elif direction == Direction.DOWN and direction != Direction.UP:
            y += BLOCK_SIZE
        elif direction == Direction.UP and direction != Direction.DOWN:
            y -= BLOCK_SIZE

        self.head = Point(x, y)


if __name__ == "__main__":
    game = SnakeGame()
    # game loop
    while True:
        game_over, score = game.play_step()
        if game_over == True:
            game.reset()
            game.play_step()

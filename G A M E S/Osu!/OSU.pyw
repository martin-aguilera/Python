import pygame, random, sys
from random import choice

screen_width = 1360
screen_height = 700
black = (000, 000, 000)
blue = (000, 000, 255)
green = (000, 255, 000)
cyan = (000, 255, 255)
red = (255, 000, 000)
purple = (255, 000, 255)
yellow = (255, 255, 000)
white = (255, 255, 255)
orange = (255, 125, 000)
pink = (255, 000, 125)
lime = (185, 255, 000)

the_fruits = ["fruit1.png", "fruit2.png", "fruit3.png", "fruit4.png"]
choice(the_fruits)


class Meteor(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load(f"assets/{choice(the_fruits)}").convert()
        self.image.set_colorkey(black)
        self.rect = self.image.get_rect()

    def update(self):
        self.rect.y += 2

        if self.rect.y > screen_height:
            self.rect.y = -100
            self.rect.x = random.randrange(screen_width - 50)
        if self.rect.x > screen_width:
            self.rect.y = -100
            self.rect.x = random.randrange(screen_width - 50)
        if self.rect.right > screen_width:
            self.rect.right = screen_height
        if self.rect.left < 0:
            self.rect.left = 0


class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("assets/player-edit.png").convert()
        self.image.set_colorkey(black)
        self.rect = self.image.get_rect()
        self.speed_x = 0

    def changespeed(self, x):
        self.speed_x += x

    def update(self):
        self.rect.x += self.speed_x
        self.rect.y = 590


class Game(object):
    def __init__(self):
        self.game_over = False
        self.score = 0

        self.meteor_list = pygame.sprite.Group()
        self.all_sprites_list = pygame.sprite.Group()

        for i in range(30):
            meteor = Meteor()
            meteor.rect.x = random.randrange(screen_width - 60)
            meteor.rect.y = random.randrange(screen_height)

            self.meteor_list.add(meteor)
            self.all_sprites_list.add(meteor)

        self.player = Player()
        self.all_sprites_list.add(self.player)

    def process_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return True

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    self.player.changespeed(-7)
                if event.key == pygame.K_RIGHT:
                    self.player.changespeed(7)

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT:
                    self.player.changespeed(7)
                if event.key == pygame.K_RIGHT:
                    self.player.changespeed(-7)

            if event.type == pygame.MOUSEBUTTONDOWN:
                if self.game_over:
                    self.__init__()

        return False

    def run_logic(self):

        if not self.game_over:
            self.all_sprites_list.update()
            meteor_hit_list = pygame.sprite.spritecollide(
                self.player, self.meteor_list, True
            )

            for meteor in meteor_hit_list:
                self.score += 1
                print(self.score)

            if len(self.meteor_list) == 0:
                self.game_over = True

    def display_frame(self, screen):
        screen.fill(black)

        if self.game_over:
            font = pygame.font.SysFont("serif", 25)
            text = font.render("Game Over, Click to continue", True, white)
            center_x = (screen_width // 2) - (text.get_width() // 2)
            center_y = (screen_height // 2) - (text.get_height() // 2)
            screen.blit(text, [center_x, center_y])

        if not self.game_over:
            self.all_sprites_list.draw(screen)
        pygame.display.flip()


def main():
    pygame.init()

    screen = pygame.display.set_mode([screen_width, screen_height])

    done = False
    clock = pygame.time.Clock()

    game = Game()

    while not done:
        done = game.process_events()
        game.run_logic()
        game.display_frame(screen)
        clock.tick(60)
    pygame.quit()


if __name__ == "__main__":
    main()

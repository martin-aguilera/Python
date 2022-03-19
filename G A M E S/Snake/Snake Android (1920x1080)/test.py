import pygame

pygame.init()

BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
CYAN = (0, 255, 255)
PURPLE = (255, 0, 255)
WHITE = (255, 255, 255)

screen = pygame.display.set_mode()
pygame.FULLSCREEN
wx, wy = screen.get_size()
print((wx, wy))

screen.fill(WHITE)


class Button:
    def __init__(self, color, x, y, width, height):
        self.color = color
        self.x = x
        self.y = y
        self.width = width
        self.height = height

    def draw(self, screen):
        pygame.draw.rect(screen, self.color, (self.x, self.y, self.width, self.height))

    def isOver(self, pos):
        # Pos is the mouse position or a tuple of (x,y) coordinates
        if pos[1] > 360:
            return True
        return False


def redrawWindow():
    screen.fill(WHITE)
    button1.draw(screen)
    button2.draw(screen)
    button3.draw(screen)
    button4.draw(screen)
    button5.draw(screen)


run = True
button1 = Button(GREEN, 640, 180, 180, 270)
button2 = Button(YELLOW, 0, 270, 270, 180)
button3 = Button(CYAN, 270, 450, 180, 270)
button4 = Button(PURPLE, 450, 270, 270, 180)
button5 = Button(BLACK, 270, 270, 180, 180)

while run:
    redrawWindow()
    pygame.display.update()
    for event in pygame.event.get():
        pos = pygame.mouse.get_pos()
        # print(pos)
        if event.type == pygame.QUIT:
            run = False
            pygame.quit()
            quit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            if button5.isOver(pos):
                button5.color = WHITE
            else:
                button5.color = BLACK

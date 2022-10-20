import pygame
from pygame.locals import *

pygame.init()

WIN_WIDTH = 500
WIN_HEIGHT = 500

WIN = pygame.display.set_mode((WIN_WIDTH, WIN_HEIGHT))
pygame.display.set_caption('Tic-tac-toe')


def draw_choose_player():
    bg = (255, 255, 200)
    gridO = (255, 0, 0)
    gridX = (0, 0, 255)
    WIN.fill(bg)

    pygame.draw.rect(WIN, (0, 0, 0), pygame.Rect(40, 150, 200, 200), 10)
    pygame.draw.line(WIN, gridX, (60, 170), (220, 330), 10)
    pygame.draw.line(WIN, gridX, (60, 330), (220, 170), 10)

    pygame.draw.rect(WIN, (0, 0, 0), pygame.Rect(260, 150, 200, 200), 10)
    pygame.draw.circle(WIN, gridO, (360, 250), 80, 10)


run = True
player_is_choosing = True
player_is_choosing_grid = True
grid = 0
while run:

    if player_is_choosing:
        draw_choose_player()
    elif player_is_choosing_grid:
        pass

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    pygame.display.update()

pygame.quit()

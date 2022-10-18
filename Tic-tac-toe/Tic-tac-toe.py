import pygame
from pygame.locals import *

pygame.init()

WIN_WIDTH = 500
WIN_HEIGHT = 500

WIN = pygame.display.set_mode((WIN_WIDTH, WIN_HEIGHT))
pygame.display.set_caption('Tic-tac-toe')


def draw_choose_player():
    bg = (255, 255, 255)
    gridX = (255, 0, 0)
    dridO = (0, 0, 255)
    WIN.fill(bg)


run = True
while run:
    draw_choose_player()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    pygame.display.update()

pygame.quit()

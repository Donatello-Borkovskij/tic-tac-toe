import pygame
from Grid import Grid
from pygame.locals import *

pygame.init()

screen_width = 500
screen_height = 500

screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('Tic-tac-toe')


def draw_choose_player():
    bg = (255, 255, 200)
    gridO = (255, 0, 0)
    gridX = (0, 0, 255)
    screen.fill(bg)

    pygame.draw.rect(screen, (0, 0, 0), pygame.Rect(40, 150, 200, 200), 10)
    pygame.draw.line(screen, gridX, (60, 170), (220, 330), 10)
    pygame.draw.line(screen, gridX, (60, 330), (220, 170), 10)

    pygame.draw.rect(screen, (0, 0, 0), pygame.Rect(260, 150, 200, 200), 10)
    pygame.draw.circle(screen, gridO, (360, 250), 80, 10)

def draw_grid_choice():
    pass


run = True
player_is_choosing = False
player_is_choosing_grid = False
grid = 0
while run:

    if player_is_choosing:
        draw_choose_player()
    elif player_is_choosing_grid:
        draw_grid_choice()
    else:
        table = Grid()
        table.draw_grid(screen, screen_width, screen_height, (50, 50, 50), (255, 255, 200))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    pygame.display.update()

pygame.quit()

import pygame


class Grid:
    line_width = 5
    markers = []

    def __init__(self, size):
        self.size = size

        for y in range(self.size):
            row = [0] * self.size
            self.markers.append(row)
        print(self.markers)

    #def __init__(self):
    #    self.size = 3

    def draw_grid(self, screen, screen_width, screen_height, grid, bg):
        screen.fill(bg)
        if self.size == 5:
            for x in range(1, self.size):
                pygame.draw.line(screen, grid, (0, x * 100), (screen_width, x * 100), self.line_width)
                pygame.draw.line(screen, grid, (x * 100, 0), (x * 100, screen_height), self.line_width)

        elif self.size == 4:
            for x in range(1, self.size):
                pygame.draw.line(screen, grid, (50, x * 100 + 50), (screen_width - 50, x * 100 + 50), self.line_width)
                pygame.draw.line(screen, grid, (x * 100 + 50, 50), (x * 100 + 50, screen_height - 50), self.line_width)

        elif self.size == 3:
            for x in range(1, self.size):
                pygame.draw.line(screen, grid, (100, x * 100 + 100), (screen_width - 100, x * 100 + 100)
                                 , self.line_width)
                pygame.draw.line(screen, grid, (x * 100 + 100, 100), (x * 100 + 100, screen_height - 100)
                                 , self.line_width)

#    def get_number_of_grids(self):

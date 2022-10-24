import pygame


class Grid:
    line_width = 5
    markers = []
    clicked = False

    def __init__(self, size, x, o, player):
        self.size = size
        self.x = x
        self.o = o
        self.player = player

        for y in range(self.size):
            row = [0] * self.size
            self.markers.append(row)
        print(self.markers)

    def draw_markers(self, screen):
        if self.size == 5:
            x_pos = 0

            for x in self.markers:
                y_pos = 0
                for y in x:
                    if y == 1:
                        screen.blit(self.x, (x_pos * 100, y_pos * 100))
                    if y == -1:
                        screen.blit(self.o, (x_pos * 100, y_pos * 100))
                    y_pos += 1
                x_pos += 1
        elif self.size == 4:
            x_pos = 0

            for x in self.markers:
                y_pos = 0
                for y in x:
                    if y == 1:
                        screen.blit(self.x, (x_pos * 100 + 50, y_pos * 100 + 50))
                    if y == -1:
                        screen.blit(self.o, (x_pos * 100 + 50, y_pos * 100 + 50))
                    y_pos += 1
                x_pos += 1



    def draw_grid(self, screen, screen_width, screen_height, grid, bg):
        # get mouse position
        pos = pygame.mouse.get_pos()
        screen.fill(bg)

        if self.size == 5:
            for x in range(1, self.size):
                pygame.draw.line(screen, grid, (0, x * 100), (screen_width, x * 100), self.line_width)
                pygame.draw.line(screen, grid, (x * 100, 0), (x * 100, screen_height), self.line_width)
                # check mouseover and clicked conditions
                if pygame.mouse.get_pressed()[0] == 1 and self.clicked == False:
                    self.clicked = True
                    if self.markers[pos[0] // 100][pos[1] // 100] == 0:
                        if self.player:
                            self.markers[pos[0] // 100][pos[1] // 100] = 1
                            self.player = False
                        else:
                            self.markers[pos[0] // 100][pos[1] // 100] = -1
                            self.player = True

                if pygame.mouse.get_pressed()[0] == 0:
                    self.clicked = False
                    #self.draw_markers(screen)

        elif self.size == 4:
            for x in range(1, self.size):
                pygame.draw.line(screen, grid, (50, x * 100 + 50), (screen_width - 50, x * 100 + 50), self.line_width)
                pygame.draw.line(screen, grid, (x * 100 + 50, 50), (x * 100 + 50, screen_height - 50), self.line_width)
                # check mouseover and clicked conditions
                if (pos[0] - 50) <= 500 and (pos[0] - 50) >= 0 and (pos[1] - 50) <= 500 and (pos[1] - 50) >= 0:
                    if pygame.mouse.get_pressed()[0] == 1 and self.clicked == False:
                        self.clicked = True
                        if self.markers[(pos[0] - 50) // 100][(pos[1] - 50) // 100] == 0:
                            if self.player:
                                self.markers[(pos[0] - 50) // 100][(pos[1] - 50) // 100] = 1
                                self.player = False
                            else:
                                self.markers[(pos[0] - 50) // 100][(pos[1] - 50) // 100] = -1
                                self.player = True

                    if pygame.mouse.get_pressed()[0] == 0:
                        self.clicked = False

        elif self.size == 3:
            for x in range(1, self.size):
                pygame.draw.line(screen, grid, (100, x * 100 + 100), (screen_width - 100, x * 100 + 100)
                                 , self.line_width)
                pygame.draw.line(screen, grid, (x * 100 + 100, 100), (x * 100 + 100, screen_height - 100)
                                 , self.line_width)


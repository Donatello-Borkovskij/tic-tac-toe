import pygame


class Grid:
    line_width = 5
    markers = []
    clicked = False
    game_over = False
    tie = False

    def __init__(self, size, x, o, player):
        self.size = size
        self.x = x
        self.o = o
        self.player = player

        for y in range(self.size):
            row = [0] * self.size
            self.markers.append(row)
        print(self.markers)

    # def get_game_over(self):
    #     return self.game_over

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

        elif self.size == 3:
            x_pos = 0

            for x in self.markers:
                y_pos = 0
                for y in x:
                    if y == 1:
                        screen.blit(self.x, (x_pos * 100 + 100, y_pos * 100 + 100))
                    if y == -1:
                        screen.blit(self.o, (x_pos * 100 + 100, y_pos * 100 + 100))
                    y_pos += 1
                x_pos += 1

    def draw_grid(self, screen, screen_width, screen_height, grid, bg):
        # get mouse position
        pos = pygame.mouse.get_pos()
        screen.fill(bg)

        if not self.game_over:
            if self.size == 5:
                for x in range(1, self.size):
                    pygame.draw.line(screen, grid, (0, x * 100), (screen_width, x * 100), self.line_width)
                    pygame.draw.line(screen, grid, (x * 100, 0), (x * 100, screen_height), self.line_width)
                    # check mouseover and clicked conditions
                    if pygame.mouse.get_pressed()[0] == 1 and self.clicked == False:
                        x = pos[0] // 100
                        y = pos[1] // 100
                        self.clicked = True
                        if self.markers[x][y] == 0:
                            if self.player:
                                self.markers[x][y] = 1
                                self.player = False
                            else:
                                self.markers[x][y] = -1
                                self.player = True
                            self.winner_winner_chicken_dinner(x, y)

                    if pygame.mouse.get_pressed()[0] == 0:
                        self.clicked = False

            elif self.size == 4:
                for x in range(1, self.size):
                    pygame.draw.line(screen, grid, (50, x * 100 + 50), (screen_width - 50, x * 100 + 50), self.line_width)
                    pygame.draw.line(screen, grid, (x * 100 + 50, 50), (x * 100 + 50, screen_height - 50), self.line_width)
                    # check mouseover and clicked conditions
                    try:
                        if pygame.mouse.get_pressed()[0] == 1 and self.clicked == False:
                            x = (pos[0] - 50) // 100
                            y = (pos[1] - 50) // 100
                            self.clicked = True
                            if self.markers[x][y] == 0:
                                if self.player:
                                    self.markers[x][y] = 1
                                    self.player = False
                                else:
                                    self.markers[x][y] = -1
                                    self.player = True
                                self.winner_winner_chicken_dinner(x, y)

                        if pygame.mouse.get_pressed()[0] == 0:
                            self.clicked = False
                    except IndexError:
                        print('oops')

            elif self.size == 3:
                for x in range(1, self.size):
                    pygame.draw.line(screen, grid, (100, x * 100 + 100), (screen_width - 100, x * 100 + 100)
                                     , self.line_width)
                    pygame.draw.line(screen, grid, (x * 100 + 100, 100), (x * 100 + 100, screen_height - 100)
                                     , self.line_width)
                    # check mouseover and clicked conditions
                    try:
                        if pygame.mouse.get_pressed()[0] == 1 and self.clicked == False:
                            x = (pos[0] - 100) // 100
                            y = (pos[1] - 100) // 100
                            self.clicked = True
                            if self.markers[x][y] == 0:
                                if self.player:
                                    self.markers[x][y] = 1
                                    self.player = False
                                else:
                                    self.markers[x][y] = -1
                                    self.player = True
                                self.winner_winner_chicken_dinner(x, y)

                        if pygame.mouse.get_pressed()[0] == 0:
                            self.clicked = False
                    except IndexError:
                        print('ooops')
        #else:


    def winner_winner_chicken_dinner(self, x, y):
        try:
            # check row
            if self.markers[x][y] \
                    + self.markers[x - 1][y] \
                    + self.markers[x + 1][y] == 3:
                self.winner = self.x
                self.game_over = True
            elif self.markers[x][y] \
                    + self.markers[x - 1][y] \
                    + self.markers[x + 1][y] == -3:
                self.winner = self.o
                self.game_over = True
            # check clumn
            elif self.markers[x][y] \
                    + self.markers[x][y - 1] \
                    + self.markers[x][y + 1] == 3:
                self.winner = self.x
                self.game_over = True
            elif self.markers[x][y] \
                    + self.markers[x][y - 1] \
                    + self.markers[x][y + 1] == -3:
                self.winner = self.o
                self.game_over = True
            # check diagonals (up left to bottom right)
            elif self.markers[x][y] \
                    + self.markers[x - 1][y - 1] \
                    + self.markers[x + 1][y + 1] == 3:
                self.winner = self.x
                self.game_over = True
            elif self.markers[x][y] \
                    + self.markers[x - 1][y - 1] \
                    + self.markers[x + 1][y + 1] == -3:
                self.winner = self.o
                self.game_over = True
            # check diagonals (bottom left to up right)
            elif self.markers[x][y] \
                     + self.markers[x + 1][y - 1] \
                     + self.markers[x - 1][y + 1] == 3:
                self.winner = self.x
                self.game_over = True
            elif self.markers[x][y] \
                    + self.markers[x + 1][y - 1] \
                    + self.markers[x - 1][y + 1] == -3:
                self.winner = self.o
                self.game_over = True
            else:
                if not self.game_over:
                    self.tie = True
                    for x in self.markers:
                        for y in x:
                            if y == 0:
                                self.tie = False
                                break
                    if self.tie:
                        self.game_over = True
            print("game over = {0}".format(self.game_over))

        except IndexError:
            print('ooops 2')

    #def draw_game_over(self):



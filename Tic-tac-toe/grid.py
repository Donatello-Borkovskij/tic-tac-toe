import pygame


class Grid:
    line_width = 5
    markers = []
    clicked = False
    game_over = False
    tie = False
    winner = 0
    size = 0

    def __init__(self, x, o, player):
        self.x = x
        self.o = o
        self.player = player

    def set_size(self, size):
        self.size = size

        for y in range(self.size):
            row = [0] * self.size
            self.markers.append(row)
        print(self.markers)

    def set_markers(self, markers):
        self.markers = markers

    def get_markers(self):
        return self.markers

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

    def draw_grid(self, screen, screen_width, screen_height, grid, bg, font):
        # get mouse position
        pos = pygame.mouse.get_pos()
        screen.fill(bg)

        if not self.game_over:
            if self.size == 5:
                for x in range(1, self.size):
                    pygame.draw.line(screen, grid, (0, x * 100), (screen_width, x * 100), self.line_width)
                    pygame.draw.line(screen, grid, (x * 100, 0), (x * 100, screen_height), self.line_width)
                    # check mouseover and clicked conditions
                    try:
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
                    except IndexError:
                        print('oops')

            elif self.size == 4:
                for x in range(1, self.size):
                    pygame.draw.line(screen, grid, (50, x * 100 + 50), (screen_width - 50, x * 100 + 50),
                                     self.line_width)
                    pygame.draw.line(screen, grid, (x * 100 + 50, 50), (x * 100 + 50, screen_height - 50),
                                     self.line_width)
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
            self.draw_markers(screen)
        else:
            self.draw_game_over(screen, screen_width, screen_height, font)

    def winner_winner_chicken_dinner(self, x, y):
        try:
            # check row
            if 0 < x < self.size - 1:
                if self.markers[x][y] \
                        + self.markers[x - 1][y] \
                        + self.markers[x + 1][y] == 3:
                    self.winner = self.x
                    self.game_over = True
                    print('1')
                    return
                elif 0 < x < self.size and self.markers[x][y] \
                        + self.markers[x - 1][y] \
                        + self.markers[x + 1][y] == -3:
                    self.winner = self.o
                    self.game_over = True
                    print('2')
                    return
            # check row 2 to left side
            if 1 < x:
                if self.markers[x][y] \
                        + self.markers[x - 1][y] \
                        + self.markers[x - 2][y] == 3:
                    self.winner = self.x
                    self.game_over = True
                    print('3')
                    return
                elif self.markers[x][y] \
                        + self.markers[x - 1][y] \
                        + self.markers[x - 2][y] == -3:
                    self.winner = self.o
                    self.game_over = True
                    print('4')
                    return
            # check row 2 to right side
            if x < self.size - 1:
                if self.markers[x][y] \
                        + self.markers[x + 1][y] \
                        + self.markers[x + 2][y] == 3:
                    self.winner = self.x
                    self.game_over = True
                    print('5')
                    return
                elif self.markers[x][y] \
                        + self.markers[x + 1][y] \
                        + self.markers[x + 2][y] == -3:
                    self.winner = self.o
                    self.game_over = True
                    print('6')
                    return
        except IndexError:
            print('ooops 2')
        try:
            # check column
            if 0 < y < self.size - 1:
                if self.markers[x][y] \
                        + self.markers[x][y - 1] \
                        + self.markers[x][y + 1] == 3:
                    self.winner = self.x
                    self.game_over = True
                    print('7')
                    return
                elif self.markers[x][y] \
                        + self.markers[x][y - 1] \
                        + self.markers[x][y + 1] == -3:
                    self.winner = self.o
                    self.game_over = True
                    print('8')
                    return
            # check column 2 down
            if y < self.size - 1:
                if self.markers[x][y] \
                        + self.markers[x][y + 1] \
                        + self.markers[x][y + 2] == 3:
                    self.winner = self.x
                    self.game_over = True
                    print('9')
                    return
                elif self.markers[x][y] \
                        + self.markers[x][y + 1] \
                        + self.markers[x][y + 2] == -3:
                    self.winner = self.o
                    self.game_over = True
                    print('10')
                    return
            # check column 2 up
            if 1 < y:
                if self.markers[x][y] \
                        + self.markers[x][y - 1] \
                        + self.markers[x][y - 2] == 3:
                    self.winner = self.x
                    self.game_over = True
                    print('11')
                    return
                elif self.markers[x][y] \
                        + self.markers[x][y - 1] \
                        + self.markers[x][y - 2] == -3:
                    self.winner = self.o
                    self.game_over = True
                    print('12')
                    return
        except IndexError:
            print('ooops 3')
        try:
            if 0 < x < self.size - 1 and 0 < y < self.size - 1:
                # check diagonals (up left to bottom right)
                if self.markers[x][y] \
                        + self.markers[x - 1][y - 1] \
                        + self.markers[x + 1][y + 1] == 3:
                    self.winner = self.x
                    self.game_over = True
                    print('13')
                    return
                elif self.markers[x][y] \
                        + self.markers[x - 1][y - 1] \
                        + self.markers[x + 1][y + 1] == -3:
                    self.winner = self.o
                    self.game_over = True
                    print('14')
                    return
                # check diagonals (bottom left to up right)
                elif self.markers[x][y] \
                        + self.markers[x - 1][y + 1] \
                        + self.markers[x + 1][y - 1] == 3:
                    self.winner = self.x
                    self.game_over = True
                    print('15')
                    return
                elif self.markers[x][y] \
                        + self.markers[x - 1][y + 1] \
                        + self.markers[x + 1][y - 1] == -3:
                    self.winner = self.o
                    self.game_over = True
                    print('16')
                    return
        except IndexError:
            print('ooops 4')
        try:
            # check diagonals 2 to one direction
            if 1 < x and 1 < y:
                # check diagonal to left up
                if self.markers[x][y] \
                        + self.markers[x - 1][y - 1] \
                        + self.markers[x - 2][y - 2] == 3:
                    self.winner = self.x
                    self.game_over = True
                    print('17')
                    return
                elif self.markers[x][y] \
                        + self.markers[x - 1][y - 1] \
                        + self.markers[x - 2][y - 2] == -3:
                    self.winner = self.o
                    self.game_over = True
                    print('18')
                    return
            if 1 < x and y < self.size - 1:
                # check diagonal 2 to left down
                if self.markers[x][y] \
                        + self.markers[x - 1][y + 1] \
                        + self.markers[x - 2][y + 2] == 3:
                    self.winner = self.x
                    self.game_over = True
                    print('19')
                    return
                elif self.markers[x][y] \
                        + self.markers[x - 1][y + 1] \
                        + self.markers[x - 2][y + 2] == -3:
                    self.winner = self.o
                    self.game_over = True
                    print('20')
                    return
            if x < self.size - 1 and 1 < y:
                # check diagonal 2 to right up
                if self.markers[x][y] \
                        + self.markers[x + 1][y - 1] \
                        + self.markers[x + 2][y - 2] == 3:
                    self.winner = self.x
                    self.game_over = True
                    print('21')
                    return
                elif self.markers[x][y] \
                        + self.markers[x + 1][y - 1] \
                        + self.markers[x + 2][y - 2] == -3:
                    self.winner = self.o
                    self.game_over = True
                    print('22')
                    return
            if x < self.size - 1 and y < self.size - 1:
                # check diagonal 2 to right down
                if self.markers[x][y] \
                        + self.markers[x + 1][y + 1] \
                        + self.markers[x + 2][y + 2] == 3:
                    self.winner = self.x
                    self.game_over = True
                    print('23')
                    return
                elif self.markers[x][y] \
                        + self.markers[x + 1][y + 1] \
                        + self.markers[x + 2][y + 2] == -3:
                    self.winner = self.o
                    self.game_over = True
                    print('24')
                    return
            else:
                if self.game_over == False:
                    self.tie = True
                    for row in self.markers:
                        for i in row:
                            if i == 0:
                                self.tie = False
                    # if it is a tie, then call game over and set winner to 0 (no one)
                    if self.tie == True:
                        self.game_over = True
                        self.winner = 0
        except IndexError:
            print('ooops 5')

        print(self.markers)
        print("x = {0}, y = {1}".format(x, y))
        print("game over = {0}".format(self.game_over))

    def draw_game_over(self, screen, screen_width, screen_height, font):
        if self.tie:
            end_img = font.render("It's a tie!", True, (0, 0, 0))
            screen.blit(end_img, (screen_width // 2 - 25, screen_height // 2 - 120))
        else:
            end_img = font.render("has won!", True, (0, 0, 0))
            quit_img = font.render("press 'q' to quit!", True, (0, 0, 0))
            #restart_img = font.render("press 'space' to restart", True, (0, 0, 0))
            screen.blit(self.winner, (screen_width // 2 - 125, screen_height // 2 - 150))
            screen.blit(end_img, (screen_width // 2, screen_height // 2 - 120))
            screen.blit(quit_img, (screen_width // 2 - 100, screen_height // 2))
            #screen.blit(restart_img, (screen_width // 2 - 150, screen_height // 2 + 100))

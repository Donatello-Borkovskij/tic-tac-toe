import unittest
import grid
import pygame

x_img = pygame.image.load('imgs/X.png')
o_img = pygame.image.load('imgs/O.png')


class TestGrid(unittest.TestCase):
    def test_grid_size(self):
        size_3 = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
        size_4 = [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]
        size_5 = [[0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0]]

        table = grid.Grid(x_img, o_img, True)
        table.set_size(3)
        self.assertEqual(table.get_markers(), size_3)
        table.set_size(4)
        self.assertEqual(table.get_markers(), size_4)
        table.set_size(5)
        self.assertEqual(table.get_markers(), size_5)

    def test_win(self):
        table = grid.Grid(x_img, o_img, True)
        table.set_size(3)

        # test rows for x
        table.set_markers([[1, 0, 0], [1, 0, 0], [1, 0, 0]])
        table.winner_winner_chicken_dinner(2, 0)
        self.assertEqual(table.get_winner(), x_img)
        self.assertEqual(table.game_over, True)

        table.set_markers([[0, 1, 0], [0, 1, 0], [0, 1, 0]])
        table.winner_winner_chicken_dinner(2, 1)
        self.assertEqual(table.get_winner(), x_img)
        self.assertEqual(table.game_over, True)

        table.set_markers([[0, 0, 1], [0, 0, 1], [0, 0, 1]])
        table.winner_winner_chicken_dinner(2, 2)
        self.assertEqual(table.get_winner(), x_img)
        self.assertEqual(table.game_over, True)
        # test columns for x
        table.set_markers([[1, 1, 1], [0, 0, 0], [0, 0, 0]])
        table.winner_winner_chicken_dinner(0, 0)
        self.assertEqual(table.get_winner(), x_img)
        self.assertEqual(table.game_over, True)

        table.set_markers([[0, 0, 0], [1, 1, 1], [0, 0, 0]])
        table.winner_winner_chicken_dinner(0, 0)
        self.assertEqual(table.get_winner(), x_img)
        self.assertEqual(table.game_over, True)

        table.set_markers([[0, 0, 0], [0, 0, 0], [1, 1, 1]])
        table.winner_winner_chicken_dinner(0, 0)
        self.assertEqual(table.get_winner(), x_img)
        self.assertEqual(table.game_over, True)
        # test diagonals for x
        table.set_markers([[1, 0, 0], [0, 1, 0], [0, 0, 1]])
        table.winner_winner_chicken_dinner(0, 0)
        self.assertEqual(table.get_winner(), x_img)
        self.assertEqual(table.game_over, True)

        table.set_markers([[0, 0, 1], [0, 1, 0], [1, 0, 0]])
        table.winner_winner_chicken_dinner(0, 0)
        self.assertEqual(table.get_winner(), x_img)
        self.assertEqual(table.game_over, True)

        ##########################################
        # test rows for o
        table.set_markers([[-1, 0, 0], [-1, 0, 0], [-1, 0, 0]])
        table.winner_winner_chicken_dinner(2, 0)
        self.assertEqual(table.get_winner(), o_img)
        self.assertEqual(table.game_over, True)

        table.set_markers([[0, -1, 0], [0, -1, 0], [0, -1, 0]])
        table.winner_winner_chicken_dinner(2, 1)
        self.assertEqual(table.get_winner(), o_img)
        self.assertEqual(table.game_over, True)

        table.set_markers([[0, 0, -1], [0, 0, -1], [0, 0, -1]])
        table.winner_winner_chicken_dinner(2, 2)
        self.assertEqual(table.get_winner(), o_img)
        self.assertEqual(table.game_over, True)
        # test columns for o
        table.set_markers([[-1, -1, -1], [0, 0, 0], [0, 0, 0]])
        table.winner_winner_chicken_dinner(0, 0)
        self.assertEqual(table.get_winner(), o_img)
        self.assertEqual(table.game_over, True)

        table.set_markers([[0, 0, 0], [-1, -1, -1], [0, 0, 0]])
        table.winner_winner_chicken_dinner(0, 0)
        self.assertEqual(table.get_winner(), o_img)
        self.assertEqual(table.game_over, True)

        table.set_markers([[0, 0, 0], [0, 0, 0], [-1, -1, -1]])
        table.winner_winner_chicken_dinner(0, 0)
        self.assertEqual(table.get_winner(), o_img)
        self.assertEqual(table.game_over, True)
        # test diagonals for o
        table.set_markers([[-1, 0, 0], [0, -1, 0], [0, 0, -1]])
        table.winner_winner_chicken_dinner(0, 0)
        self.assertEqual(table.get_winner(), o_img)
        self.assertEqual(table.game_over, True)

        table.set_markers([[0, 0, -1], [0, -1, 0], [-1, 0, 0]])
        table.winner_winner_chicken_dinner(0, 0)
        self.assertEqual(table.get_winner(), o_img)
        self.assertEqual(table.game_over, True)
if __name__ == '__main__':
    unittest.main()

import unittest
import grid
import pygame

x_img = pygame.image.load('../X.png')
o_img = pygame.image.load('../O.png')


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
        # table = grid.Grid(x_img, o_img, True)
        # table.set_size(3)
        pass

if __name__ == '__main__':
    unittest.main()

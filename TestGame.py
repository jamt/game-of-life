import unittest
import game_of_life

__author__ = 'James Thomas'

'''
Tests for the "rules" function and "neighbors" function
'''

class MyTestCase(unittest.TestCase):

    def test_rules(self):
        grid = [[0, 0, 0], [1, 1, 1], [0, 0, 0]]
        new_grid = [[0, 0, 0], [1, 1, 1], [0, 0, 0]]
        expected_output_grid = [[0, 1, 0], [1, 1, 1], [0, 0, 0]]

        game_of_life.rules(grid, new_grid, 0, 1)
        self.assertEqual(new_grid, expected_output_grid)

    def test_neighbors(self):
        grid = [[0, 0, 0], [1, 1, 1], [0, 0, 0]]
        count = game_of_life.neighbors(grid, 1, 1)
        self.assertEqual(count, 2)


if __name__ == '__main__':
    unittest.main()

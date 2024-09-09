import unittest

from print_map.game_objects import BoardMap
from print_map.game_objects.boardMap import _check_is_playable_boardmap

SQUARES_VALID = [1, 1, 1, 1, 1, 1, 1, 1, 1,
                 1, 4, 0, 0, 0, 0, 0, 0, 1,
                 1, 0, 3, 1, 0, 1, 3, 0, 1,
                 1, 0, 2, 1, 0, 1, 1, 0, 1,
                 1, 0, 0, 0, 3, 0, 0, 0, 1,
                 1, 0, 1, 1, 0, 1, 1, 0, 1,
                 1, 0, 3, 1, 0, 2, 1, 1, 1,
                 1, 0, 0, 0, 0, 0, 6, 1, 1,
                 1, 1, 1, 1, 1, 1, 1, 1, 1]

SQUARES_INVALID = [1, 1, 1, 1, 1, 1, 1, 1, 1,
                 1, 4, 0, 0, 0, 0, 0, 0, 1,
                 1, 0, 3, 1, 0, 1, 3, 0, 1,
                 1, 0, 2, 1, 0, 1, 1, 0, 1,
                 1, 0, 0, 0, 3, 0, 0, 0, 1,
                 1, 0, 1, 1, 0, 1, 1, 0, 1,
                 1, 0, 3, 1, 0, 2, 1, 1, 1,
                 1, 0, 0, 0, 0, 1, 6, 1, 1,
                 1, 1, 1, 1, 1, 1, 1, 1, 1]
ROWS = 9
COLS = 9

BOARD_MAP_VALID = BoardMap(ROWS, COLS)
BOARD_MAP_VALID.create_squares_of_boardmap(SQUARES_VALID)

BOARD_MAP_INVALID = BoardMap(ROWS, COLS)
BOARD_MAP_INVALID.create_squares_of_boardmap(SQUARES_INVALID)


class MyTestCase(unittest.TestCase):

    def test_correct_playable_boardmap(self):
        self.assertTrue(_check_is_playable_boardmap(BOARD_MAP_VALID))

    def test_correct_not_playable_boardmap(self):
        self.assertFalse(_check_is_playable_boardmap(BOARD_MAP_INVALID))


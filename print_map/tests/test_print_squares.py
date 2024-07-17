import unittest
from print_map.game_objects import BoardMap
from print_map.game_objects import ConsoleInterface

SQUARES_1 = [1, 1, 1,
             1, 3, 1,
             1, 1, 1]
ROWS_1 = 3
COLS_1 = 3

SQUARES_2 = [1, 1, 1, 1, 1, 1, 1, 1, 1,
             1, 4, 0, 0, 0, 0, 0, 0, 1,
             1, 0, 3, 1, 0, 1, 3, 0, 1,
             1, 0, 2, 1, 0, 1, 1, 0, 1,
             1, 0, 0, 0, 3, 0, 0, 0, 1,
             1, 0, 1, 1, 0, 1, 1, 0, 1,
             1, 0, 3, 1, 0, 2, 3, 0, 1,
             1, 0, 0, 0, 0, 0, 0, 5, 1,
             1, 1, 1, 1, 1, 1, 1, 1, 1]
ROWS_2 = 9
COLS_2 = 9

board_map_3_x_3_monster = BoardMap(ROWS_1, COLS_1)
normal_map_3_x_3_monster = ConsoleInterface.print_map(board_map_3_x_3_monster, SQUARES_1)

board_map_9_x_9_cool_mix = BoardMap(ROWS_2, COLS_2)
cool_map_9_x_9 = ConsoleInterface.print_map(board_map_9_x_9_cool_mix, SQUARES_2)


class MyTestCase(unittest.TestCase):
    def test_normal_3_x_3(self):
        self.assertEqual(normal_map_3_x_3_monster, '╔═╗\n║M║\n╚═╝')

    def test_cool_9_x_9(self):
        self.assertEqual(cool_map_9_x_9, '╔═══════╗\n'
                                         '║S      ║\n'
                                         '║ M║ ║M ║\n'
                                         '║ -╝ ╚═ ║\n'
                                         '║   M   ║\n'
                                         '║ ═╗ ╔═ ║\n'
                                         '║ M║ │M ║\n'
                                         '║      F║\n'
                                         '╚═══════╝')


if __name__ == '__main__':
    unittest.main()

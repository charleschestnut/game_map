import unittest
from print_map.game_objects import BoardMap
from print_map.game_objects import ConsoleInterface

SQUARES_1 = [1]
ROWS_1 = 1
COLS_1 = 1

SQUARES_2 = [0]
ROWS_2 = 1
COLS_2 = 1

SQUARES_3 = [2]
ROWS_3 = 1
COLS_3 = 1

SQUARES_4 = [1,1,1,1]
ROWS_4 = 2
COLS_4 = 2

SQUARES_5 = [1,1,1,1,0,1,1,1,1]
ROWS_5 = 3
COLS_5 = 3

SQUARES_6 = [1,1,1,1,2,1,1,1,1]
ROWS_6 = 3
COLS_6 = 3

SQUARES_7 = [1,1,1,1,1,1,1,1,1,
             1,0,0,0,0,0,0,0,1,
             1,0,0,1,0,1,0,0,1,
             1,0,1,1,0,1,1,0,1,
             1,0,0,0,0,0,0,0,1,
             1,0,1,1,0,1,1,0,1,
             1,0,0,1,0,1,0,0,1,
             1,0,0,0,0,0,0,0,1,
             1,1,1,1,1,1,1,1,1]
ROWS_7 = 9
COLS_7 = 9


empty_board_map = BoardMap(ROWS_2, COLS_2, SQUARES_2)
column_board_map = BoardMap(ROWS_1, COLS_1, SQUARES_1)
fake_column_board_map = BoardMap(ROWS_3, COLS_3, SQUARES_3)
map_2_x_2_board = BoardMap(ROWS_4, COLS_4, SQUARES_4)
normal_map_3_x_3_board = BoardMap(ROWS_5, COLS_5, SQUARES_5)
board_map_3_x_3_fake_column = BoardMap(ROWS_6, COLS_6, SQUARES_6)
board_map_9_x_9_normal = BoardMap(ROWS_7, COLS_7, SQUARES_7)

column = ConsoleInterface.print_map(column_board_map)
empty_map = ConsoleInterface.print_map(empty_board_map)
fake_column = ConsoleInterface.print_map(fake_column_board_map)
map_2_x_2 = ConsoleInterface.print_map(map_2_x_2_board)
normal_map_3_x_3 = ConsoleInterface.print_map(normal_map_3_x_3_board)
fake_column_3_x_3 = ConsoleInterface.print_map(board_map_3_x_3_fake_column)
normal_map_9_x_9 = ConsoleInterface.print_map(board_map_9_x_9_normal)

class MyTestCase(unittest.TestCase):
    def test_column(self):
        self.assertEqual(column, '¤')

    def test_empty(self):
        self.assertEqual(empty_map, ' ')

    def test_fake_column(self):
        self.assertEqual(fake_column, 'ø')

    def test_2_x_2(self):
        self.assertEqual(map_2_x_2, '╔╗\n╚╝')

    def test_normal_3_x_3(self):
        self.assertEqual(normal_map_3_x_3, '╔═╗\n║ ║\n╚═╝')

    def test_fake_column_3_x_3(self):
        self.assertEqual(fake_column_3_x_3, '╔╦╗\n╠┼╣\n╚╩╝')

    def test_fake_column_9_x_9(self):
        self.assertEqual(normal_map_9_x_9, '╔═══════╗\n'
                                           '║       ║\n'
                                           '║  ║ ║  ║\n'
                                           '║ ═╝ ╚═ ║\n'
                                           '║       ║\n'
                                           '║ ═╗ ╔═ ║\n'
                                           '║  ║ ║  ║\n'
                                           '║       ║\n'
                                           '╚═══════╝')


if __name__ == '__main__':

    unittest.main()

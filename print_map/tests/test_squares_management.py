import unittest
import copy
from print_map.game_objects import BoardMap, ConsoleInterface, Square, Position

position_1 = Position(0, 0)
position_2 = Position(-1, 0)
position_3 = Position(0, -1)
position_4 = Position(1, 0)
position_5 = Position(0, 1)
position_6 = Position(-2, -2)
rows_1 = 1
cols_1 = 1

boardmap_1 = BoardMap(rows_1, cols_1)

square_1 = Square(position_1, 1, boardmap_1)

squares_6 = [1, 1, 1,
             1, 3, 1,
             1, 1, 1]

squares_7 = [1, 1, 1,
             1, 3, 1,
             1, 1]

squares_one_portal = [1, 1, 1,
                      1, 5, 1,
                      1, 1, 1]

squares_two_portals = [1, 1, 1,
                       1, 5, 1,
                       1, 5, 1]

squares_three_portals = [1, 5, 1,
                         1, 5, 1,
                         1, 5, 1]

rows_6 = 3
cols_6 = 3

empty_board_3_x_3 = BoardMap(rows_6, cols_6)
board_map_3_x_3_8 = BoardMap(rows_6, cols_6)

board_map_3_x_3 = copy.deepcopy(empty_board_3_x_3)
board_map_3_x_3.create_squares_of_boardmap(squares_6)
board_map_3_x_3_8.create_squares_of_boardmap(squares_7)


class MyTestCase(unittest.TestCase):

    def test_correct_square(self):
        self.assertFalse(None, square_1)

    def test_incorrect_x_square_left(self):
        self.assertRaises(TypeError, Square, position_2, 1, boardmap_1)

    def test_incorrect_x_square_right(self):
        self.assertRaises(TypeError, Square, position_3, 1, boardmap_1)

    def test_incorrect_x_square_left(self):
        self.assertRaises(TypeError, Square, position_6, 1, boardmap_1)

    def test_incorrect_y_square_left(self):
        self.assertRaises(TypeError, Square, position_4, 1, boardmap_1)

    def test_incorrect_y_square_right(self):
        self.assertRaises(TypeError, Square, position_5, 1, boardmap_1)

    def test_append_correct_square(self):
        r = board_map_3_x_3_8.append_square(1)
        self.assertFalse(None, r)

    def test_append_extra_square(self):
        self.assertRaises(TypeError, board_map_3_x_3.append_square, 1)

    def test_create_boardmap_two_portals(self):
        try:
            empty_board_3_x_3 = BoardMap(rows_6, cols_6)
            empty_board_3_x_3.create_squares_of_boardmap(squares_two_portals)
        except TypeError:
            self.fail("The creation of Boardmap with two portals "
                      "raised ExceptionType unexpectedly!")

    def test_create_boardmap_three_portals(self):
        try:
            empty_board_3_x_3 = BoardMap(rows_6, cols_6)
            empty_board_3_x_3.create_squares_of_boardmap(squares_three_portals)
        except TypeError:
            self.fail("The creation of Boardmap with three portals "
                      "raised ExceptionType unexpectedly!")

    def test_create_boardmap_one_portals(self):
        self.assertRaises(TypeError, empty_board_3_x_3.create_squares_of_boardmap,
                          squares_one_portal)


if __name__ == '__main__':
    unittest.main()

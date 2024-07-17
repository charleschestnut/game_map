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

squares_correct_4_x_4 = [1, 1, 1, 1,
                         1, 3, 4, 1,
                         1, 0, 6, 1,
                         1, 1, 1, 1]

squares_without_start = [1, 1, 1, 1,
                         1, 0, 0, 1,
                         1, 0, 6, 1,
                         1, 1, 1, 1]

squares_with_two_start = [1, 1, 1, 1,
                          1, 4, 4, 1,
                          1, 0, 6, 1,
                          1, 1, 1, 1]

squares_without_finish = [1, 1, 1, 1,
                          1, 3, 4, 1,
                          1, 0, 0, 1,
                          1, 1, 1, 1]

squares_with_two_finish = [1, 1, 1, 1,
                           1, 3, 4, 1,
                           1, 6, 6, 1,
                           1, 1, 1, 1]


squares_one_portal = [1, 1, 1, 1,
                      1, 3, 4, 1,
                      1, 5, 6, 1,
                      1, 1, 1, 1]

squares_two_portals = [1, 1, 1, 1,
                       1, 5, 4, 1,
                       1, 5, 6, 1,
                       1, 1, 1, 1]

squares_three_portals = [1, 1, 1, 1, 1,
                         1, 5, 4, 5, 1,
                         1, 5, 6, 0, 1,
                         1, 1, 1, 1, 1]

rows_4 = 4
cols_4 = 4
cols_5 = 5

empty_board_4_x_4 = BoardMap(rows_4, cols_4)
board_4_x_4_second = copy.deepcopy(empty_board_4_x_4)
board_4_x_4_second.create_squares_of_boardmap(squares_correct_4_x_4)


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

    def test_append_extra_square(self):
        self.assertRaises(TypeError, board_4_x_4_second.append_square, 1)

    def test_create_boardmap_two_portals(self):
        try:
            empty_board_4_x_4 = BoardMap(rows_4, cols_4)
            empty_board_4_x_4.create_squares_of_boardmap(squares_two_portals)
        except TypeError:
            self.fail("The creation of Boardmap with two portals "
                      "raised ExceptionType unexpectedly!")

    def test_create_boardmap_three_portals(self):
        try:
            empty_board_4_x_5 = BoardMap(4, 5)
            empty_board_4_x_5.create_squares_of_boardmap(squares_three_portals)
        except TypeError:
            self.fail("The creation of Boardmap with three portals "
                      "raised ExceptionType unexpectedly!")

    def test_create_boardmap_one_portals(self):
        self.assertRaises(TypeError, empty_board_4_x_4.create_squares_of_boardmap,
                          squares_one_portal)

    def test_create_boardmap_without_start_position(self):
        self.assertRaises(TypeError, empty_board_4_x_4.create_squares_of_boardmap,
                          squares_without_start)

    def test_create_boardmap_with_two_start_positions(self):
        self.assertRaises(TypeError, empty_board_4_x_4.create_squares_of_boardmap,
                          squares_with_two_start)

    def test_create_boardmap_without_finish_position(self):
        self.assertRaises(TypeError, empty_board_4_x_4.create_squares_of_boardmap,
                          squares_without_finish)

    def test_create_boardmap_with_two_finish_position(self):
        try:
            empty_board_4_x_4.create_squares_of_boardmap(squares_with_two_finish)
        except Exception as e:
            self.fail("The creation of Boardmap with two finish position "
                      "raised ExceptionType unexpectedly!")


if __name__ == '__main__':
    unittest.main()

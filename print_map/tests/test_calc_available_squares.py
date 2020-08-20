import unittest
from print_map.game_objects import BoardMap, Square
from print_map.game_objects import ConsoleInterface

SQUARES_1 = [1, 1, 1, 1,
             1, 0, 0, 1,
             1, 0, 0, 1,
             1, 1, 1, 1]
ROWS_1 = 4
COLS_1 = 4


SQUARES_2 = [1,1,1,1,1,1,1,1,1,
             1,4,0,0,0,0,0,0,1,
             1,0,3,1,0,1,3,0,1,
             1,0,2,1,0,1,1,0,1,
             1,0,0,0,3,0,0,0,1,
             1,0,1,1,0,1,1,0,1,
             1,0,3,1,0,2,3,0,1,
             1,0,0,0,0,0,0,5,1,
             1,1,1,1,1,1,1,1,1]
ROWS_2 = 9
COLS_2 = 9

board_map_4_x_4_normal = BoardMap(ROWS_1, COLS_1)
board_map_4_x_4_normal.create_squares_of_boardmap(SQUARES_1)
square_1_2 = board_map_4_x_4_normal.squares[5]
normal_map_4_x_4_normal = ConsoleInterface.print_map(board_map_4_x_4_normal, SQUARES_1)

for s in square_1_2.get_availables_squares(1):
    print(s)


class MyTestCase(unittest.TestCase):
    def test_get_square_by_position_correct(self):
        square_test_1_2 = board_map_4_x_4_normal.get_square_by_position(1, 2)
        print(square_1_2)
        self.assertEqual(square_1_2, square_test_1_2)

    def test_get_square_by_position_out_range_1(self):
        square_test_1_2 = board_map_4_x_4_normal.get_square_by_position(4, 4)
        self.assertIsNone(square_test_1_2)

    '''def test_get_square_by_position_out_range_2(self):
        square_test_1_1 = board_map_4_x_4_normal.get_square_by_position(1, 1)
        self.assertEqual(square_1_1, square_test_1_1)
    
    def test_get_square_by_position_out_range_3(self):
        square_test_1_1 = board_map_4_x_4_normal.get_square_by_position(1, 1)
        self.assertEqual(square_1_1, square_test_1_1)'''


    def test_can_not_move_to_direction_left(self):
        can_move = square_1_2.can_move_to_direction('L')
        self.assertEqual(can_move, False)

    def test_can_not_move_to_direction_top(self):
        can_move = square_1_2.can_move_to_direction('T')
        self.assertEqual(can_move, False)

    def test_can_move_to_direction_right(self):
        can_move = square_1_2.can_move_to_direction('R')
        self.assertEqual(can_move, True)

    def test_can_move_to_direction_down(self):
        can_move = square_1_2.can_move_to_direction('B')
        self.assertEqual(can_move, True)

    def test_calc_possible_directions_dice_1(self):
        dice_number = 1
        possible_square_1 = board_map_4_x_4_normal.get_square_by_position(2, 2)
        possible_square_2 = board_map_4_x_4_normal.get_square_by_position(1, 1)
        possible_squares = list(set([possible_square_1, possible_square_2]))
        possible_squares_2 = square_1_2.get_availables_squares(dice_number)
        self.assertEqual(possible_squares, possible_squares_2)

    def test_calc_possible_directions_dice_2(self):
        dice_number = 2
        possible_square_1 = board_map_4_x_4_normal.get_square_by_position(2, 1)
        possible_square_2 = board_map_4_x_4_normal.get_square_by_position(1, 2)
        possible_squares = list(set([possible_square_1, possible_square_2]))
        possible_squares_2 = square_1_2.get_availables_squares(dice_number)
        self.assertEqual(possible_squares, possible_squares_2)

    # BOARDMAP OF 9X9
    def test_calc_possible_directions_dice_3(self):
        dice_number = 1
        self.assertEqual(possible_squares, possible_squares_2)

    def test_calc_possible_directions_dice_4(self):
        dice_number = 2
        self.assertEqual(possible_squares, possible_squares_2)

    def test_calc_possible_directions_dice_5(self):
        dice_number = 3
        self.assertEqual(possible_squares, possible_squares_2)

    def test_calc_possible_directions_dice_6(self):
        dice_number = 4
        self.assertEqual(possible_squares, possible_squares_2)

    def test_calc_possible_directions_dice_7(self):
        dice_number = 5
        self.assertEqual(possible_squares, possible_squares_2)

if __name__ == '__main__':
    unittest.main()

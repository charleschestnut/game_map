import unittest
from print_map.game_objects import BoardMap, Square, VitalStatus, Character, Weapon
from print_map.game_objects import ConsoleInterface
from print_map.game_objects.weapon import Specialty

SQUARES_1 = [1, 1, 1, 1,
             1, 4, 0, 1,
             1, 0, 6, 1,
             1, 1, 1, 1]
ROWS_1 = 4
COLS_1 = 4


SQUARES_2 = [1,1,1,1,1,1,1,1,1,
             1,4,0,0,0,0,0,0,1,
             1,0,3,1,0,1,3,0,1,
             1,2,2,1,0,1,1,5,1,
             1,0,0,0,3,0,0,0,1,
             1,0,1,1,0,1,1,0,1,
             1,0,3,1,5,2,3,0,1,
             1,0,0,0,0,0,0,6,1,
             1,1,1,1,1,1,1,1,1]
ROWS_2 = 9
COLS_2 = 9

board_map_4_x_4_normal = BoardMap(ROWS_1, COLS_1)
board_map_4_x_4_normal.create_squares_of_boardmap(SQUARES_1)
square_1_2 = board_map_4_x_4_normal.squares[5]
normal_map_4_x_4_normal = ConsoleInterface.print_map(board_map_4_x_4_normal, SQUARES_1)

board_map_9_x_9 = BoardMap(ROWS_2, COLS_2)
board_map_9_x_9.create_squares_of_boardmap(SQUARES_2)
ConsoleInterface.print_map(board_map_9_x_9, SQUARES_2)
square_1_7_9x9 = board_map_9_x_9.get_square_by_position(1, 7)
square_4_4_9x9 = board_map_9_x_9.get_square_by_position(4, 4)
square_6_6_9x9 = board_map_9_x_9.get_square_by_position(6, 6)


# Character's attributes
status_proportion = [0.5, 0.5, 0.7, 0.9, 0.8]
extra_level = 1
v_status_character = VitalStatus(10, 3, 4, 6, 20, status_proportion, extra_level)
v_status_weapon = VitalStatus(2, 3, -1, 5, 1, None, 1)
weapon_special = Weapon("Super book", "This book increases your magic power.", v_status_weapon,
                        Specialty.CROSS_WALLS)
character_name = "Onion Knight"
uses_magic = True


class MyTestCase(unittest.TestCase):
    def test_get_square_by_position_correct(self):
        square_test_1_2 = board_map_4_x_4_normal.get_square_by_position(1, 2)
        self.assertEqual(square_1_2, square_test_1_2)

    def test_get_square_by_position_out_range_1(self):
        square_test_1_2 = board_map_4_x_4_normal.get_square_by_position(4, 4)
        self.assertIsNone(square_test_1_2)

    def test_get_square_by_position_out_range_2(self):
        square_test_1_1 = board_map_4_x_4_normal.get_square_by_position(5, 5)
        self.assertIsNone(square_test_1_1)

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
        possible_squares = {possible_square_1, possible_square_2}
        possible_squares_dice = square_1_2.get_available_squares(dice_number)

        self.assertSetEqual(possible_squares, set(possible_squares_dice))

    def test_calc_possible_directions_dice_2(self):
        dice_number = 2
        possible_square_1 = board_map_4_x_4_normal.get_square_by_position(2, 1)
        possible_squares = {possible_square_1}
        possible_squares_dice = square_1_2.get_available_squares(dice_number)

        self.assertSetEqual(possible_squares, set(possible_squares_dice))

    # BOARDMAP OF 9X9
    def test_calc_possible_directions_dice_3(self):
        dice_number = 1
        possible_square_1 = board_map_9_x_9.get_square_by_position(2, 7)
        possible_square_2 = board_map_9_x_9.get_square_by_position(1, 6)
        possible_squares = {possible_square_1, possible_square_2}
        possible_squares_dice = square_1_7_9x9.get_available_squares(dice_number)

        self.assertSetEqual(possible_squares, set(possible_squares_dice))

    def test_calc_possible_directions_dice_4(self):
        dice_number = 2
        possible_square_1 = board_map_9_x_9.get_square_by_position(3, 7)
        # possible_square_2 = board_map_9_x_9.get_square_by_position(1, 5)
        possible_square_3 = board_map_9_x_9.get_square_by_position(2, 6)
        possible_squares = {possible_square_1, possible_square_3}
        possible_squares_dice = square_1_7_9x9.get_available_squares(dice_number)

        self.assertSetEqual(possible_squares, set(possible_squares_dice))

    def test_calc_possible_directions_dice_4_can_cross_walls(self):
        character = Character(character_name, uses_magic, v_status_character)
        character.level = 7
        character.add_weapon(weapon_special)

        dice_number = 3

        possible_square_1 = board_map_9_x_9.get_square_by_position(4, 7)
        possible_square_2 = board_map_9_x_9.get_square_by_position(1, 6)
        possible_square_3 = board_map_9_x_9.get_square_by_position(1, 4)
        possible_square_4 = board_map_9_x_9.get_square_by_position(2, 7)
        possible_squares = {possible_square_1, possible_square_2, possible_square_3, possible_square_4}
        possible_squares_dice = square_1_7_9x9.get_available_squares(dice_number, character)

        self.assertSetEqual(possible_squares, set(possible_squares_dice))

    def test_calc_possible_directions_dice_5(self):
        dice_number = 3
        possible_square_1 = board_map_9_x_9.get_square_by_position(4, 7)
        possible_square_2 = board_map_9_x_9.get_square_by_position(1, 6)
        possible_square_3 = board_map_9_x_9.get_square_by_position(2, 7)
        possible_squares = list({possible_square_1, possible_square_2, possible_square_3})
        possible_squares_dice = square_1_7_9x9.get_available_squares(dice_number)

        self.assertSetEqual(set(possible_squares), set(possible_squares_dice))

    def test_calc_possible_directions_dice_6(self):
        dice_number = 1
        possible_square_1 = board_map_9_x_9.get_square_by_position(4, 3)
        possible_square_2 = board_map_9_x_9.get_square_by_position(4, 5)
        possible_square_3 = board_map_9_x_9.get_square_by_position(3, 4)
        possible_square_4 = board_map_9_x_9.get_square_by_position(5, 4)
        possible_squares = {possible_square_1, possible_square_2, possible_square_3,
                            possible_square_4}
        possible_squares_dice = square_4_4_9x9.get_available_squares(dice_number)

        self.assertSetEqual(possible_squares, set(possible_squares_dice))

    def test_calc_possible_directions_dice_7(self):
        dice_number = 2
        possible_square_1 = board_map_9_x_9.get_square_by_position(4, 2)
        possible_square_2 = board_map_9_x_9.get_square_by_position(4, 6)
        possible_square_3 = board_map_9_x_9.get_square_by_position(2, 4)
        possible_square_4 = board_map_9_x_9.get_square_by_position(6, 4)
        possible_squares = {possible_square_1, possible_square_2, possible_square_3,
                            possible_square_4}
        possible_squares_dice = square_4_4_9x9.get_available_squares(dice_number)

        self.assertSetEqual(possible_squares, set(possible_squares_dice))

    def test_calc_possible_directions_dice_8(self):
        dice_number = 3
        possible_square_1 = board_map_9_x_9.get_square_by_position(4, 1)
        possible_square_2 = board_map_9_x_9.get_square_by_position(4, 7)
        possible_square_3 = board_map_9_x_9.get_square_by_position(1, 4)
        possible_square_4 = board_map_9_x_9.get_square_by_position(7, 4)
        possible_squares = {possible_square_1, possible_square_2, possible_square_3,
                            possible_square_4}
        possible_squares_dice = square_4_4_9x9.get_available_squares(dice_number)

        self.assertSetEqual(possible_squares, set(possible_squares_dice))

    def test_calc_possible_directions_dice_9_cannot_cross(self):
        dice_number = 4
        possible_square_1 = board_map_9_x_9.get_square_by_position(1, 3)
        possible_square_3 = board_map_9_x_9.get_square_by_position(3, 1)
        possible_square_4 = board_map_9_x_9.get_square_by_position(3, 7)
        possible_square_5 = board_map_9_x_9.get_square_by_position(5, 7)
        possible_square_6 = board_map_9_x_9.get_square_by_position(5, 1)
        possible_square_7 = board_map_9_x_9.get_square_by_position(7, 3)
        possible_square_8 = board_map_9_x_9.get_square_by_position(7, 5)

        possible_squares = {possible_square_1, possible_square_3,
                            possible_square_4, possible_square_5, possible_square_6,
                            possible_square_7, possible_square_8}
        possible_squares_dice = square_4_4_9x9.get_available_squares(dice_number)

        self.assertSetEqual(possible_squares, set(possible_squares_dice))

    def test_calc_possible_directions_dice_9_can_cross(self):
        character = Character(character_name, uses_magic, v_status_character)
        character.level = 7
        character.add_weapon(weapon_special)

        dice_number = 4
        possible_square_1 = board_map_9_x_9.get_square_by_position(1, 3)
        possible_square_2 = board_map_9_x_9.get_square_by_position(2, 6)
        possible_square_3 = board_map_9_x_9.get_square_by_position(3, 1)
        possible_square_4 = board_map_9_x_9.get_square_by_position(3, 7)
        possible_square_5 = board_map_9_x_9.get_square_by_position(5, 7)
        possible_square_6 = board_map_9_x_9.get_square_by_position(5, 1)
        possible_square_7 = board_map_9_x_9.get_square_by_position(7, 3)
        possible_square_8 = board_map_9_x_9.get_square_by_position(7, 5)
        possible_square_9 = board_map_9_x_9.get_square_by_position(6, 2)

        possible_squares = {possible_square_1, possible_square_2, possible_square_3,
                            possible_square_4, possible_square_5, possible_square_6,
                            possible_square_7, possible_square_8, possible_square_9}
        possible_squares_dice = square_4_4_9x9.get_available_squares(dice_number, character)

        self.assertSetEqual(possible_squares, set(possible_squares_dice))

    def test_calc_possible_directions_dice_10(self):
        dice_number = 1
        possible_square_1 = board_map_9_x_9.get_square_by_position(6, 7)
        possible_square_2 = board_map_9_x_9.get_square_by_position(7, 6)
        possible_squares = {possible_square_1, possible_square_2}
        possible_squares_dice = square_6_6_9x9.get_available_squares(dice_number)
        self.assertSetEqual(possible_squares, set(possible_squares_dice))

    def test_calc_possible_directions_dice_11(self):
        dice_number = 2
        possible_square_1 = board_map_9_x_9.get_square_by_position(7, 7)
        possible_square_2 = board_map_9_x_9.get_square_by_position(7, 5)
        possible_square_3 = board_map_9_x_9.get_square_by_position(5, 7)
        possible_squares = {possible_square_1, possible_square_2, possible_square_3}
        possible_squares_dice = square_6_6_9x9.get_available_squares(dice_number)
        self.assertSetEqual(possible_squares, set(possible_squares_dice))

    def test_calc_possible_directions_dice_12(self):
        dice_number = 3
        possible_square_1 = board_map_9_x_9.get_square_by_position(7, 6)
        possible_square_2 = board_map_9_x_9.get_square_by_position(6, 7)
        possible_square_3 = board_map_9_x_9.get_square_by_position(7, 4)
        possible_square_4 = board_map_9_x_9.get_square_by_position(4, 7)
        possible_squares = {possible_square_1, possible_square_2, possible_square_3,
                            possible_square_4}
        possible_squares_dice = square_6_6_9x9.get_available_squares(dice_number)
        self.assertSetEqual(possible_squares, set(possible_squares_dice))


if __name__ == '__main__':
    unittest.main()

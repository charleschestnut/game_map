import unittest
from unittest.mock import patch
from print_map.game_objects import BoardMap, Character, Weapon, VitalStatus, Position

SQUARES = [1, 1, 1, 1, 1, 1, 1, 1, 1,
           1, 4, 0, 0, 0, 0, 0, 0, 1,
           1, 0, 3, 1, 0, 1, 3, 0, 1,
           1, 0, 2, 1, 0, 1, 1, 0, 1,
           1, 0, 0, 0, 3, 0, 0, 0, 1,
           1, 0, 1, 1, 0, 1, 1, 0, 1,
           1, 0, 3, 1, 0, 2, 3, 0, 1,
           1, 0, 0, 0, 0, 0, 0, 5, 1,
           1, 1, 1, 1, 1, 1, 1, 1, 1]
ROWS = 9
COLS = 9

board_map = BoardMap(ROWS, COLS)
board_map.create_squares_of_boardmap(SQUARES)

status_proportion = [0.5, 0.5, 0.7, 0.9, 0.8]
extra_level = 1
v_status_character = VitalStatus(10, 3, 4, 6, 20, status_proportion, extra_level)

v_status_weapon_1 = VitalStatus(2, 3, -1, 5, 1, None, 0)
v_status_weapon_2 = VitalStatus(2, 3, -2, 4, 1, None, 0)
v_status_weapon_3 = VitalStatus(2, 3, 5, 5, 3, None, -1)
v_status_weapon_4 = VitalStatus(2, 3, -1, 5, 1, None, 1)
v_status_weapon_5 = VitalStatus(1, 1, 1, 1, 1, None, 0)

weapon_1 = Weapon("Super sword", "This sword cut what it wants.", v_status_weapon_1)
weapon_2 = Weapon("Super shield", "This sword cut what it wants.", v_status_weapon_2)
weapon_3 = Weapon("Super hat", "This hat makes you invisible.", v_status_weapon_3)
weapon_4 = Weapon("Super boots", "Those boots let you pass though poisoned rivers.", v_status_weapon_4)
weapon_5 = Weapon("Super book", "This book increase your magic power.", v_status_weapon_5)

character_name_1 = "Onion Knight"
character_name_2 = "Shield Soldier"


class MyTestCase(unittest.TestCase):
    def test_create_character(self):
        character = Character(character_name_1, v_status_character, board_map)
        position_start = Position(1, 7)
        self.assertIsNotNone(character)
        self.assertEqual(character.position.x, position_start.x)
        self.assertEqual(character.position.y, position_start.y)

    def test_create_character_incorrectly_1(self):
        self.assertRaises(Exception, Character, character_name_1, None, board_map)

    def test_create_character_incorrectly_1(self):
        self.assertRaises(Exception, Character, "", v_status_character, board_map)

    def test_create_character_incorrectly_1(self):
        self.assertRaises(Exception, Character, character_name_1, v_status_character, None)

    def test_create_character_with_one_weapon(self):
        raises = False
        try:
            character = Character(character_name_1, v_status_character, board_map)
            character.add_weapon(weapon_1)
        except:
            raises = True
        self.assertFalse(raises)

    def test_create_character_with_multiple_weapon(self):
        raises = False
        try:
            character = Character(character_name_1, v_status_character, board_map)
            character.add_weapon(weapon_1)
            character.add_weapon(weapon_2)
            character.add_weapon(weapon_3)
            character.add_weapon(weapon_4)
        except:
            raises = True
        self.assertFalse(raises)

    @patch('builtins.input', side_effect=['3'])
    def test_create_character_with_five_weapon_and_select_third(self, input):
        raises = False
        try:
            character = Character(character_name_1, v_status_character, board_map)
            character.add_weapon(weapon_1)
            character.add_weapon(weapon_2)
            character.add_weapon(weapon_3)
            character.add_weapon(weapon_4)
            character.add_weapon(weapon_5)
        except:
            raises = True
        self.assertFalse(raises)
        self.assertSetEqual(set(character.weapons), set([weapon_1, weapon_2, weapon_3, weapon_5]))

    @patch('builtins.input', side_effect=['6'])
    def test_create_character_with_five_weapon_and_select_sixth(self, input):
        raises = False
        try:
            character = Character(character_name_1, v_status_character, board_map)
            character.add_weapon(weapon_1)
            character.add_weapon(weapon_2)
            character.add_weapon(weapon_3)
            character.add_weapon(weapon_4)
            character.add_weapon(weapon_5)
        except:
            raises = True
        self.assertTrue(raises)

    @patch('builtins.input', side_effect=['4'])
    def test_create_character_with_five_weapon_and_select_fourth(self, input):
        raises = False
        try:
            character = Character(character_name_1, v_status_character, board_map)
            character.add_weapon(weapon_1)
            character.add_weapon(weapon_2)
            character.add_weapon(weapon_3)
            character.add_weapon(weapon_4)
            character.add_weapon(weapon_5)
        except:
            raises = True
        self.assertFalse(raises)
        self.assertSetEqual(set(character.weapons), set([weapon_1, weapon_2, weapon_3, weapon_4]))

    def test_remove_weapon_correct(self):
        raises = False
        try:
            character = Character(character_name_1, v_status_character, board_map)
            character.add_weapon(weapon_5)
            character.remove_weapon(0)
        except:
            raises = True
        self.assertFalse(raises)

    def test_remove_weapon_incorrect_index(self):
        raises = False
        try:
            character = Character(character_name_1, v_status_character, board_map)
            character.add_weapon(weapon_5)
            character.remove_weapon(1)
        except:
            raises = True
        self.assertTrue(raises)

if __name__ == '__main__':
    unittest.main()

import unittest
from unittest.mock import patch
from print_map.game_objects import BoardMap, Character, Weapon, VitalStatus, Position, Game
from print_map.game_objects.errors import WallError
from print_map.game_objects.weapon import Specialty

SQUARES = [1, 1, 1, 1, 1, 1, 1, 1, 1,
           1, 4, 0, 0, 0, 0, 0, 0, 1,
           1, 0, 3, 1, 0, 1, 3, 0, 1,
           1, 0, 2, 1, 0, 1, 1, 0, 1,
           1, 0, 0, 0, 3, 0, 0, 0, 1,
           1, 0, 1, 1, 0, 1, 1, 0, 1,
           1, 0, 3, 1, 0, 2, 3, 0, 1,
           1, 0, 0, 0, 0, 0, 6, 0, 1,
           1, 1, 1, 1, 1, 1, 1, 1, 1]
ROWS = 9
COLS = 9

board_map = BoardMap(ROWS, COLS)
board_map.create_squares_of_boardmap(SQUARES)

game = Game(board_map)

status_proportion = [0.5, 0.5, 0.7, 0.9, 0.8]
extra_level = 1
v_status_character = VitalStatus(10, 3, 4, 6, 20, status_proportion, extra_level)

v_status_weapon_1 = VitalStatus(2, 3, -1, 5, 1, None, 1)
v_status_weapon_2 = VitalStatus(2, 3, -2, 4, 1, None, 0)
v_status_weapon_3 = VitalStatus(2, 3, 5, 5, 3, None, -1)
v_status_weapon_4 = VitalStatus(2, 3, -1, 5, 1, None, 1)
v_status_weapon_5 = VitalStatus(1, 1, 1, 1, 1, None, 0)

weapon_1 = Weapon("Super sword", "This sword cuts what it wants.", v_status_weapon_1)
weapon_2 = Weapon("Super shield", "This sword cuts what it wants.", v_status_weapon_2)
weapon_3 = Weapon("Super hat", "This hat makes you invisible.", v_status_weapon_3)
weapon_4 = Weapon("Super boots", "Those boots let you pass though poisoned rivers.",
                  v_status_weapon_4)
weapon_5 = Weapon("Super book", "This book increases your magic power.", v_status_weapon_5)
weapon_special = Weapon("Super book", "This book increases your magic power.", v_status_weapon_5,
                        Specialty.CROSS_WALLS)

character_name_1 = "Onion Knight"
character_name_2 = "Shield Soldier"

uses_magic = True
doesnt_use_magic = False


class MyTestCase(unittest.TestCase):
    def test_create_correctly_character(self):
        character = Character(character_name_1, uses_magic, v_status_character)
        game.append_character(character)
        position_start = Position(1, 7)
        self.assertIsNotNone(character)
        self.assertEqual(character.position.x, position_start.x)
        self.assertEqual(character.position.y, position_start.y)

    def test_initiation_character_with_wrong_name(self):
        self.assertRaises(Exception, Character, "", doesnt_use_magic, v_status_character)

    def test_initiation_character_without_name_(self):
        self.assertRaises(Exception, Character, None, doesnt_use_magic, v_status_character)

    def test_initiation_character_without_uses_magic(self):
        self.assertRaises(Exception, Character, character_name_1, None, v_status_character)

    def test_initiation_character_with_wrong_uses_magic(self):
        self.assertRaises(Exception, Character, character_name_1, 'False', v_status_character)

    def test_initiation_character_with_wrong_vital_status(self):
        self.assertRaises(Exception, Character, character_name_1, uses_magic, 'vitalStatus')

    def test_initiation_character_without_vital_status(self):
        self.assertRaises(Exception, Character, character_name_1, uses_magic, None)

    def test_create_character_with_one_weapon(self):
        # Arrange: Create a character
        character = Character(character_name_1, doesnt_use_magic, v_status_character)

        # Act: Add a weapon to the character
        character.add_weapon(weapon_1)

        # Assert: Verify the weapon was added successfully
        self.assertIn(weapon_1, character.weapons,
                      "The weapon was not added to the character's weapon list")

    def test_create_character_with_multiple_weapon(self):
        character = Character(character_name_1, uses_magic, v_status_character)
        character.add_weapon(weapon_1)
        character.add_weapon(weapon_2)
        character.add_weapon(weapon_3)
        character.add_weapon(weapon_4)

        self.assertEqual(set(character.weapons), {weapon_1, weapon_2, weapon_3, weapon_4})

    @patch('builtins.input', side_effect=['3'])
    def test_create_character_with_five_weapon_and_select_third(self, input):
        character = Character(character_name_1, uses_magic, v_status_character)
        character.add_weapon(weapon_1)
        character.add_weapon(weapon_2)
        character.add_weapon(weapon_3)
        character.add_weapon(weapon_4)
        character.add_weapon(weapon_5)

        self.assertSetEqual(set(character.weapons), {weapon_1, weapon_2, weapon_3, weapon_5})

    @patch('builtins.input', side_effect=['6'])
    def test_create_character_with_five_weapon_and_select_sixth(self, input):
        # Arrange: Create a character and add five weapons
        character = Character(character_name_1, doesnt_use_magic, v_status_character)
        character.add_weapon(weapon_1)
        character.add_weapon(weapon_2)
        character.add_weapon(weapon_3)
        character.add_weapon(weapon_4)

        # Act and Assert: Try to add a sixth weapon and assert that it raises the expected exception
        with self.assertRaises(Exception):  # Replace with the actual exception expected
            character.add_weapon(weapon_5)  # Attempting to add the weapon into the sixth position

    @patch('builtins.input', side_effect=['4'])
    def test_create_character_with_five_weapon_and_select_fourth(self, input):
        character = Character(character_name_1, uses_magic, v_status_character)
        character.add_weapon(weapon_1)
        character.add_weapon(weapon_2)
        character.add_weapon(weapon_3)
        character.add_weapon(weapon_4)
        character.add_weapon(weapon_5)

        self.assertSetEqual(set(character.weapons), {weapon_1, weapon_2, weapon_3, weapon_4})

    def test_remove_weapon_correct(self):
        character = Character(character_name_1, doesnt_use_magic, v_status_character)
        character.add_weapon(weapon_5)
        character.remove_weapon(0)
        self.assertEqual(character.weapons, [])

    def test_remove_weapon_incorrect_index(self):
        character = Character(character_name_1, uses_magic, v_status_character)
        character.add_weapon(weapon_5)
        with self.assertRaises(IndexError):
            character.remove_weapon(1)

    def test_character_set_position_correctly(self):
        position_2 = Position(4, 4)
        character = Character(character_name_1, uses_magic, v_status_character)
        game.append_character(character)
        character.position = position_2
        self.assertEqual(game.characters, [character])

    def test_character_set_position_true_wall(self):
        position_true_wall = Position(0, 0)
        character = Character(character_name_1, doesnt_use_magic, v_status_character)
        game.append_character(character)

        with self.assertRaises(WallError):
            character.position = position_true_wall

    def test_character_set_position_fake_wall(self):
        position_fake_wall = Position(2, 5)
        character = Character(character_name_1, doesnt_use_magic, v_status_character)
        game.append_character(character)

        with self.assertRaises(WallError):
            character.position = position_fake_wall

    def test_character_get_total_level(self):
        character = Character(character_name_1, uses_magic, v_status_character)
        character.add_weapon(weapon_1)
        character.add_weapon(weapon_2)
        character.add_weapon(weapon_3)
        character.add_weapon(weapon_4)
        character.level = 7
        self.assertEqual(8, character.get_level_with_weapons())

    def test_character_get_total_vital_status(self):
        character = Character(character_name_1, uses_magic, v_status_character)
        character.level = 7
        character.add_weapon(weapon_1)
        character.add_weapon(weapon_2)
        character.add_weapon(weapon_3)
        character.add_weapon(weapon_4)
        real_level = character.get_level_with_weapons()

        weapon_health = (weapon_1.vital_status.health + weapon_2.vital_status.health +
                         weapon_3.vital_status.health + weapon_4.vital_status.health)
        weapon_attack = (weapon_1.vital_status.attack + weapon_2.vital_status.attack +
                         weapon_3.vital_status.attack + weapon_4.vital_status.attack)
        weapon_defense = (weapon_1.vital_status.defense + weapon_2.vital_status.defense +
                          weapon_3.vital_status.defense + weapon_4.vital_status.defense)
        weapon_magic_power = (weapon_1.vital_status.magic_power +
                              weapon_2.vital_status.magic_power +
                              weapon_3.vital_status.magic_power +
                              weapon_4.vital_status.magic_power)
        weapon_magic_defense = (weapon_1.vital_status.magic_defense +
                                weapon_2.vital_status.magic_defense +
                                weapon_3.vital_status.magic_defense +
                                weapon_4.vital_status.magic_defense)

        character_level_status = character.vital_status.get_vital_status_at_level(real_level)
        final_status = character.get_total_vital_status()

        total_health = weapon_health + character_level_status.health
        total_attack = weapon_attack + character_level_status.attack
        total_magic_power = weapon_magic_power + character_level_status.magic_power
        total_defense = weapon_defense + character_level_status.defense
        total_magic_defense = weapon_magic_defense + character_level_status.magic_defense

        self.assertEqual(final_status.health, total_health)
        self.assertEqual(final_status.attack, total_attack)
        self.assertEqual(final_status.magic_power, total_magic_power)
        self.assertEqual(final_status.defense, total_defense)
        self.assertEqual(final_status.magic_defense, total_magic_defense)

    def test_character_special_weapon(self):
        character = Character(character_name_1, uses_magic, v_status_character)
        character.level = 7
        character.add_weapon(weapon_special)
        self.assertTrue(character.can_cross_walls())


if __name__ == '__main__':
    unittest.main()

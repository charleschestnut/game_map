
import unittest
from print_map.game_objects import Battle, BoardMap, Character, Weapon, VitalStatus, Monster, Game


SQUARES = [1, 1, 1, 1, 1, 1, 1, 1, 1,
           1, 4, 0, 0, 0, 0, 0, 0, 1,
           1, 0, 3, 1, 0, 1, 3, 0, 1,
           1, 0, 2, 1, 0, 1, 1, 0, 1,
           1, 0, 0, 0, 3, 0, 0, 5, 1,
           1, 0, 1, 1, 0, 1, 1, 0, 1,
           1, 0, 3, 1, 0, 2, 3, 0, 1,
           1, 0, 0, 0, 0, 0, 6, 5, 1,
           1, 1, 1, 1, 1, 1, 1, 1, 1]
ROWS = 9
COLS = 9

status_proportion = [0.5, 0.5, 0.7, 0.9, 0.8]
extra_level = 1

v_status_character = VitalStatus(30, 5, 5, 5, 5, status_proportion, extra_level)
v_status_monster_1 = VitalStatus(25, 4, 4, 4, 4, None, None)
v_status_monster_2 = VitalStatus(100000, 2000, 3000, 5000, 5000, None, None)

v_status_weapon_1 = VitalStatus(2, 3, -1, 5, 1, None, 0)
v_status_weapon_2 = VitalStatus(2, 3, -2, 4, 1, None, 0)
v_status_weapon_3 = VitalStatus(2, 3, 5, 5, 3, None, -1)
v_status_weapon_4 = VitalStatus(2, 3, -1, 5, 1, None, 1)
v_status_weapon_5 = VitalStatus(1, 1, 1, 1, 1, None, 0)

weapon_1 = Weapon("Super sword", "This sword cuts what it wants.", v_status_weapon_1)
weapon_2 = Weapon("Super shield", "This sword cuts what it wants.", v_status_weapon_2)
weapon_3 = Weapon("Super hat", "This hat makes you invisible.", v_status_weapon_3)
weapon_4 = Weapon("Super boots", "Those boots let you pass though poisoned rivers.",
                  v_status_weapon_4)
weapon_monster = Weapon("Super book", "This book increases your magic power.", v_status_weapon_5)

character_name = "Onion Knight"
monster_name_1 = "Gannondorf"
monster_name_2 = "Dark link"
uses_magic = True
doesnt_use_magic = False

board_map = BoardMap(ROWS, COLS)
board_map.create_squares_of_boardmap(SQUARES)

game = Game(board_map)

monster_1 = Monster(monster_name_1, doesnt_use_magic, v_status_monster_1, weapon_monster)
monster_2 = Monster(monster_name_2, doesnt_use_magic, v_status_monster_2, weapon_monster)

character = Character(character_name, uses_magic, v_status_character)
character.level = 4

game.append_monster_list([monster_1, monster_2])
game.append_character(character)
game.append_weapon_list([weapon_1, weapon_2, weapon_3, weapon_4])


class MyTestCase(unittest.TestCase):
    def test_initiation_battle(self):
        # Act: Initialize a Battle instance with the character
        battle = Battle(character)
        # Assert: Verify that the battle was initiated correctly
        self.assertIsInstance(battle, Battle,
                              "The battle should be an instance of the Battle class")
        self.assertEqual(battle.character, character,
                         "The battle's character should be set correctly")

    def test_battle_development(self):
        battle = Battle(character)
        has_won, acc = battle.realise()
        if has_won:
            self.assertEqual(game.characters_alive, [character])
            self.assertEqual(character.level, 5)
        else:
            self.assertSetEqual(set(game.characters_alive), set([]))


if __name__ == '__main__':
    unittest.main()

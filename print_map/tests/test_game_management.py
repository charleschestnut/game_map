import unittest
from print_map.game_objects import Game, BoardMap, VitalStatus, Monster, Weapon

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

vital_status_monster = VitalStatus(10, 4, 3, 10, 3, None, None)
vital_status_weapon = VitalStatus(1, 1, 1, 1, 1, None, None)

weapon_monster = Weapon('Super sword', ' This sword cuts what it wants.', vital_status_weapon)
monster_1 = Monster('Goomba', True, vital_status_monster, weapon_monster)
monster_2 = Monster('Koopa', True, vital_status_monster, weapon_monster)


class MyTestCase(unittest.TestCase):

    def test_game_get_random_monster(self):
        game.append_monster(monster_1)
        game.append_monster(monster_2)
        monster_random = game.get_random_monster()
        self.assertIn(monster_random, [monster_1, monster_2])

    def test_game_append_monster(self):
        game.append_monster(monster_1)
        game.append_monster(monster_2)
        self.assertEqual(len(game.monsters), 2)

    def test_game_append_monster_list(self):
        game.append_monster_list([monster_1, monster_2])
        self.assertEqual(len(game.monsters), 2)

    def test_game_none_append_monster(self):
        # Assert that appending None raises an exception (e.g., TypeError, ValueError, etc.)
        with self.assertRaises(TypeError, msg="Appending None should raise a TypeError"):
            game.append_monster(None)

    def test_game_wrong_instance_append_monster(self):
        # Assert that appending a string instead of a monster
        # raises a TypeError (or appropriate exception)
        with self.assertRaises(TypeError,
                               msg="Appending a non-monster object should raise a TypeError"):
            game.append_monster('Monster')


if __name__ == '__main__':
    unittest.main()

import unittest
from print_map.game_objects import Monster, VitalStatus, Weapon

vital_status_monster = VitalStatus(10, 4, 3, 10, 3, None, None)
vital_status_weapon = VitalStatus(1, 1, 1, 1, 1, None, None)

weapon_monster = Weapon('Super sword', ' This sword cuts what it wants.', vital_status_weapon)


class MyTestCase(unittest.TestCase):
    def test_correct_initiation(self):
        uses_magic = False
        monster_name = 'Goomba'

        # Act: Create a Monster instance
        monster = Monster(monster_name, uses_magic, vital_status_monster, weapon_monster)

        # Assert: Verify the monster was initialized correctly
        self.assertEqual(monster.name, monster_name, "The monster's name should be 'Goomba'")
        self.assertEqual(monster.uses_magic, uses_magic, "The monster should not use magic")
        self.assertEqual(monster.vital_status, vital_status_monster,
                         "The monster's vital status should match the provided value")
        self.assertEqual(monster.weapon, weapon_monster,
                         "The monster's weapon should match the provided weapon")

    def test_correct_initiation_without_weapon(self):
        uses_magic = False
        monster_name = 'Goomba'

        # Act: Create a Monster instance
        monster = Monster(monster_name, uses_magic, vital_status_monster)

        # Assert: Verify the monster was initialized correctly
        self.assertEqual(monster.name, monster_name, "The monster's name should be 'Goomba'")
        self.assertEqual(monster.uses_magic, uses_magic, "The monster should not use magic")
        self.assertEqual(monster.vital_status, vital_status_monster,
                         "The monster's vital status should match the provided value")
        self.assertEqual(monster.weapon, None,
                         "The monster's weapon should match the provided weapon")

    def test_initiation_without_name(self):
        uses_magic = False
        self.assertRaises(Exception, Monster, None, uses_magic, vital_status_monster)

    def test_initiation_with_wrong_name(self):
        uses_magic = False
        self.assertRaises(Exception, Monster, 3, uses_magic, vital_status_monster)

    def test_initiation_without_uses_magic(self):
        self.assertRaises(Exception, Monster, 'Goomba', None, vital_status_monster)

    def test_initiation_with_wrong_uses_magic(self):
        self.assertRaises(Exception, Monster, 'Goomba', 'False', vital_status_monster)

    def test_initiation_without_vitalstatus(self):
        uses_magic = False
        self.assertRaises(Exception, Monster, 'Goomba', uses_magic, None)

    def test_initiation_without_vitalstatus_2(self):
        uses_magic = False
        self.assertRaises(Exception, Monster, 'Goomba', uses_magic)

    def test_initiation_with_wrong_vitalstatus(self):
        uses_magic = False
        self.assertRaises(Exception, Monster, 'Goomba', uses_magic, 'vitalStatus')

    def test_initiation_with_wrong_weapon(self):
        uses_magic = False
        self.assertRaises(Exception, Monster, 'Goomba', uses_magic, vital_status_monster, 'weapon')


if __name__ == '__main__':
    unittest.main()

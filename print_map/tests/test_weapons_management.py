import unittest
from print_map.game_objects import Weapon
from print_map.game_objects import VitalStatus


status_proportion = [0.5, 0.5, 0.7, 0.9, 0.8]
v_status_normal = VitalStatus(10, 10, 10, 10, 10, status_proportion)
v_status_normal_positive = VitalStatus(10, 10, 10, 10, 10, status_proportion, 1)
v_status_negative = VitalStatus(10, 10, 10, 10, 10, status_proportion, -1)

name_weapon_1 = "Super Sword"
name_weapon_2 = "Super Shield"
description_weapon_1 = "This sword can cut everything"
description_weapon_2 = "This shield can repel all the attacks"


class MyTestCase(unittest.TestCase):
    def test_create_single_weapon(self):
        weapon = Weapon(name_weapon_1, description_weapon_1, v_status_normal)
        self.assertIsNotNone(weapon)

    def test_create_short_name(self):
        self.assertRaises(Exception, Weapon, '.', description_weapon_1, v_status_normal)

    def test_create_short_description(self):
        self.assertRaises(Exception, Weapon, name_weapon_1, '.....', v_status_normal)

    def test_create_none_v_status(self):
        self.assertRaises(Exception, Weapon, name_weapon_1, description_weapon_1, None)

    def test_create_v_status_wrong_instance(self):
        self.assertRaises(Exception, Weapon, name_weapon_1, description_weapon_1, "I'm not a v_status")


if __name__ == '__main__':
    unittest.main()

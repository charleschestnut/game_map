import unittest
from print_map.game_objects import Weapon
from print_map.game_objects import VitalStatus
from print_map.game_objects.weapon import Specialty

# Constants
STATUS_PROPORTION = [0.5, 0.5, 0.7, 0.9, 0.8]
V_STATUS_NORMAL = VitalStatus(10, 10, 10, 10, 10, STATUS_PROPORTION)
V_STATUS_NORMAL_POSITIVE = VitalStatus(10, 10, 10, 10, 10, STATUS_PROPORTION, 1)
V_STATUS_NEGATIVE = VitalStatus(10, 10, 10, 10, 10, STATUS_PROPORTION, -1)

NAME_WEAPON_1 = "Super Sword"
NAME_WEAPON_2 = "Super Shield"
NAME_LONGER = "Super Ultra Mega Hero of all the Times"

DESCRIPTION_WEAPON_1 = "This sword can cut everything"
DESCRIPTION_WEAPON_2 = "This shield can repel all the attacks"
DESCRIPTION_LONG = ("Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed do eiusmod "
                    "tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam,"
                    " quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo.")


class MyTestCase(unittest.TestCase):
    def test_create_single_weapon(self):
        weapon = Weapon(NAME_WEAPON_1, DESCRIPTION_WEAPON_1, V_STATUS_NORMAL)
        self.assertIsNotNone(weapon)

    def test_create_short_name(self):
        self.assertRaises(ValueError, Weapon, '.', DESCRIPTION_WEAPON_1, V_STATUS_NORMAL)

    def test_create_long_name(self):
        self.assertRaises(ValueError, Weapon, NAME_LONGER, DESCRIPTION_WEAPON_1, V_STATUS_NORMAL)

    def test_create_long_description(self):
        self.assertRaises(ValueError, Weapon, NAME_WEAPON_1, DESCRIPTION_LONG, V_STATUS_NORMAL)

    def test_create_short_description(self):
        self.assertRaises(ValueError, Weapon, NAME_WEAPON_1, ".......", V_STATUS_NORMAL)

    def test_create_none_v_status(self):
        self.assertRaises(ValueError, Weapon, NAME_WEAPON_1, DESCRIPTION_WEAPON_1, None)

    def test_create_v_status_wrong_instance(self):
        self.assertRaises(ValueError, Weapon, NAME_WEAPON_1, DESCRIPTION_WEAPON_1,
                          "I'm not a v_status")

    def test_create_specialty_weapon(self):
        weapon = Weapon(NAME_WEAPON_1, DESCRIPTION_WEAPON_1, V_STATUS_NORMAL, Specialty.CROSS_WALLS)
        self.assertIsNotNone(weapon)
        weapon = Weapon(NAME_WEAPON_1, DESCRIPTION_WEAPON_1, V_STATUS_NORMAL,
                        Specialty.PORTAL_SELECTION)
        self.assertIsNotNone(weapon)
        weapon = Weapon(NAME_WEAPON_1, DESCRIPTION_WEAPON_1, V_STATUS_NORMAL,
                        Specialty.NEVER_SURPRISE_BATTLE)
        self.assertIsNotNone(weapon)


if __name__ == '__main__':
    unittest.main()

import unittest
from print_map.game_objects import VitalStatus


class MyTestCase(unittest.TestCase):
    def test_single_vital_status(self):
        status_proportion = [0.5, 0.5, 0.7, 0.9, 0.8]
        extra_level = 1
        v_status = VitalStatus(10, 3, 4, 6, 20, status_proportion, extra_level)
        self.assertFalse(None, v_status)

    def test_single_vital_status_default(self):
        raises = False
        try:
            VitalStatus(10, 3, 4, 6, 20, None, 1)
        except:
            raises = True
        self.assertFalse(raises)

    def test_single_vital_status_len_four(self):
        status_proportion = [0.5, 0.5, 0.7, 0.9]
        self.assertRaises(Exception, VitalStatus, 10, 3, 4, 6, 20, status_proportion, 1)

    def test_single_vital_status_len_six(self):
        status_proportion = [0.5, 0.5, 0.7, 0.9, 0.8, 0.1]
        self.assertRaises(Exception, VitalStatus, 10, 3, 4, 6, 20, status_proportion, 1)

    def test_single_vital_status_none(self):
        status_proportion = [0.5, 0.5, 0.7, 0.9, None]
        self.assertRaises(Exception, VitalStatus, 10, 3, 4, 6, 20, status_proportion, 1)

    def test_single_vital_status_integer(self):
        status_proportion = [0.5, 0.5, 0.7, 0.9, 2]
        self.assertRaises(Exception, VitalStatus, 10, 3, 4, 6, 20, status_proportion, 1)

    def test_single_vital_status_negative(self):
        status_proportion = [0.5, 0.5, 0.7, 0.9, -0.2]
        self.assertRaises(Exception, VitalStatus, 10, 3, 4, 6, 20, status_proportion, 1)

    def test_negative_extra_level(self):
        status_proportion = [0.5, 0.5, 0.7, 0.9, 0.8]
        v_status = VitalStatus(10, 3, 4, 6, 20, status_proportion, -1)
        self.assertIsNotNone(v_status)

    def test_get_vital_status_level_one(self):
        status_proportion = [0.5, 0.5, 0.7, 0.9, 0.8]
        v_status = VitalStatus(10, 10, 10, 10, 10, status_proportion, 0)
        status_level_one = v_status.get_vital_status_at_level(1)
        self.assertEqual(v_status.health, status_level_one.health)
        self.assertEqual(v_status.attack, status_level_one.attack)
        self.assertEqual(v_status.magic_power, status_level_one.magic_power)
        self.assertEqual(v_status.magic_defense, status_level_one.magic_defense)
        self.assertEqual(v_status.defense, status_level_one.defense)

    def test_get_vital_status_level_two(self):
        status_proportion = [0.5, 0.5, 0.7, 0.9, 0.8]
        v_status = VitalStatus(10, 10, 10, 10, 10, status_proportion, -1)
        status_level_two = v_status.get_vital_status_at_level(2)
        v_status_two = VitalStatus(15, 15, 17, 19, 18, status_proportion, -1)
        self.assertEqual(v_status_two.health, status_level_two.health)
        self.assertEqual(v_status_two.attack, status_level_two.attack)
        self.assertEqual(v_status_two.magic_power, status_level_two.magic_power)
        self.assertEqual(v_status_two.defense, status_level_two.defense)
        self.assertEqual(v_status_two.magic_defense, status_level_two.magic_defense)

    def test_get_vital_status_level_five(self):
        status_proportion = [0.5, 0.5, 0.5, 0.5, 0.5]
        v_status = VitalStatus(10, 10, 10, 10, 10, status_proportion, -1)
        status_level_two = v_status.get_vital_status_at_level(5)
        v_status_two = VitalStatus(50, 50, 50, 50, 50, status_proportion, -1)
        self.assertEqual(v_status_two.health, status_level_two.health)
        self.assertEqual(v_status_two.attack, status_level_two.attack)
        self.assertEqual(v_status_two.magic_power, status_level_two.magic_power)
        self.assertEqual(v_status_two.defense, status_level_two.defense)
        self.assertEqual(v_status_two.magic_defense, status_level_two.magic_defense)


if __name__ == '__main__':
    unittest.main()

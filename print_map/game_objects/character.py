from .boardMap import BoardMap
from .vitalStatus import VitalStatus
from .weapon import Weapon


class Character:

    def __init__(self, name, uses_magic, vital_status):
        if not name or not isinstance(name, str):
            raise (Exception, 'The character can not have a None name.')
        if not vital_status or not isinstance(vital_status, VitalStatus):
            raise (Exception, 'The character can not have a None vital status.')
        if uses_magic is None or not isinstance(uses_magic, bool):
            raise(Exception, 'The character can not have a uses_magic instance that is not Boolean')

        self.name = name
        self.uses_magic = uses_magic
        self.vital_status = vital_status
        self.position = None
        self.level = 1
        self.weapons = []
        self.game = None

    def __str__(self):
        return 'Character :' + str(self.name) + ' - Map: ' + str(self.game.board_map) + ' Position: ' + str(self.position)

    def get_total_vital_status(self):
        total_vital_status = self.vital_status
        vital_status_level = self.vital_status.get_vital_status_at_level(self.get_level_with_weapons())
        total_vital_status.attack = vital_status_level.attack
        total_vital_status.health = vital_status_level.health
        total_vital_status.magic_power = vital_status_level.magic_power
        total_vital_status.defense = vital_status_level.defense
        total_vital_status.magic_defense = vital_status_level.magic_defense
        for weapon in self.weapons:
            total_vital_status.attack += weapon.vital_status.attack
            total_vital_status.health += weapon.vital_status.health
            total_vital_status.magic_power += weapon.vital_status.magic_power
            total_vital_status.defense += weapon.vital_status.defense
            total_vital_status.magic_defense += weapon.vital_status.magic_defense
        return total_vital_status

    def add_weapon(self, weapon):
        if not isinstance(weapon, Weapon):
            raise(Exception, 'To add a weapon, use a Weapon instance.')

        if len(self.weapons) >= 4:
            self.change_weapons(weapon)
        else:
            self.weapons.append(weapon)
            self.level += weapon.vital_status.extra_level

    def remove_weapon(self, index):
        if index + 1 > len(self.weapons):
            raise (Exception, 'To remove a weapon, select a integer between zero(0) and ' + str(len(self.weapons)))
        else:
            del self.weapons[index]

    def change_weapons(self, new_weapon):
        weapons_string = 'Select from 0 to 3, the weapon that you want to change.\n' \
                         'In case of maintain the actual weapons, select 4.:\n'
        [weapons_string.join(weapon.__str__()) for weapon in self.weapons]
        weapons_string.join(new_weapon.__str__())
        weapons_input = input(weapons_string)
        try:
            int(weapons_input)
        except:
            weapons_input = -1

        # Repeat input if: 1. It's not an int
        # 2. It's lower than zero (0)  3. It's lower than four (4)
        while not isinstance(int(weapons_input), int) or \
                (0 > int(weapons_input) or int(weapons_input) > 4):
            weapons_input = input(weapons_string)
            try:
                int(weapons_input)
            except:
                weapons_input = -1
        weapons_input_int = int(weapons_input)

        if weapons_input_int < 4:
            old_weapon = self.weapons[weapons_input_int]

            self.level += new_weapon.vital_status.extra_level - old_weapon.vital_status.extra_level
            self.weapons[weapons_input_int] = new_weapon

    def set_position(self, position):
        square_to_move = self.game.board_map.get_square_by_position(position.x, position.y)
        if square_to_move.type == 1:
            raise (Exception, 'The character can not move to this position because this square'
                              ' with position ' + str(position) + ' is a wall.')
        if square_to_move.type == 2 and self.level < 3:
            raise (Exception, 'The character can not move to this position because this square'
                              ' with position ' + str(position) + ' is a fake wall and the level is '
                   + str(self.level) + '. The character need to have a higher level.')
        self.position = position

    def get_level_with_weapons(self):
        level = self.level
        for weapon in self.weapons:
            if weapon.vital_status.extra_level:
                level +=weapon.vital_status.extra_level
        return level

    def set_start_position(self):
        if self.game:
            self.position = self.game.board_map.get_start_position()

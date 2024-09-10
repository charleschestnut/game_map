from . import Position
from .boardMap import BoardMap
from .errors import WallError, InvalidCharacterError
from .vitalStatus import VitalStatus
from .weapon import Weapon, Specialty

class Character:

    def __init__(self, name: str, uses_magic: bool, vital_status: VitalStatus):
        if not name or not isinstance(name, str):
            raise InvalidCharacterError('The character can not have a None name.')
        if not vital_status or not isinstance(vital_status, VitalStatus):
            raise InvalidCharacterError('The character can not have a None vital status.')
        if uses_magic is None or not isinstance(uses_magic, bool):
            raise InvalidCharacterError(
                'The character can not have a uses_magic instance that is not Boolean')
        self._name = name
        self._uses_magic = uses_magic
        self._vital_status = vital_status
        self._position = None
        self._level = 1
        self._weapons = []
        self._game = None

    def __str__(self):
        game_map = getattr(self._game, 'board_map', 'No board map')  # Safeguard if _game is None
        return f'Character: {self._name} - Map: {game_map} - Position: {self._position}'

    # Getter and setter for name
    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if not value:
            raise InvalidCharacterError('The character cannot have a None name.')
        self._name = value

    # Getter and setter for uses_magic
    @property
    def uses_magic(self):
        return self._uses_magic

    @uses_magic.setter
    def uses_magic(self, value):
        if value is None:
            raise InvalidCharacterError(
                'The character cannot have a uses_magic instance that is not Boolean')
        self._uses_magic = value

    # Getter and setter for vital_status
    @property
    def vital_status(self):
        return self._vital_status

    @vital_status.setter
    def vital_status(self, value):
        if not value:
            raise InvalidCharacterError('The character cannot have a None vital status.')
        self._vital_status = value

    # Getter and setter for position
    @property
    def position(self):
        return self._position

    @position.setter
    def position(self, position: Position):
        square_to_move = self.game.board_map.get_square_by_position(position.x, position.y)

        if square_to_move.type_square == 1 or square_to_move.type_square == 2:
            raise WallError(position)

        self._position = position

    # Getter and setter for level
    @property
    def level(self):
        return self._level

    @level.setter
    def level(self, value):
        self._level = value

    # Getter and setter for weapons
    @property
    def weapons(self):
        return self._weapons

    # Getter and setter for game
    @property
    def game(self):
        return self._game

    @game.setter
    def game(self, value):
        self._game = value

    def get_total_vital_status(self):
        total_vital_status = self.vital_status
        vital_status_level = self.vital_status.get_vital_status_at_level(
            self.get_level_with_weapons())
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

    def add_weapon(self, weapon: Weapon):
        if not isinstance(weapon, Weapon):
            raise (Exception, 'To add a weapon, use a Weapon instance.')

        if len(self.weapons) >= 4:
            self.change_weapons(weapon)
        else:
            self.weapons.append(weapon)
            self.level += weapon.vital_status.extra_level

    def remove_weapon(self, index):
        if index + 1 > len(self.weapons):
            raise IndexError(f'To remove a weapon, select a integer between zero(0) and '
                             f'{str(len(self.weapons))}')
        else:
            del self.weapons[index]

    def change_weapons(self, new_weapon):
        weapons_list_str = '\n'.join([f"{i}: {weapon}" for i, weapon in enumerate(self.weapons)])
        weapons_list_str += '\n4: Maintain the current weapons.\n'

        weapons_string = f"Select from 0 to 4, the weapon you want to change:\n{weapons_list_str}\n"

        while True:
            weapons_input = input(weapons_string).strip()

            if weapons_input.isdigit():
                weapons_input_int = int(weapons_input)
                if 0 <= weapons_input_int <= 4:
                    break

            print("Invalid input. Please enter a number between 0 and 4.")

        if weapons_input_int < 4:
            old_weapon = self.weapons[weapons_input_int]
            level_difference = (new_weapon.vital_status.extra_level -
                                old_weapon.vital_status.extra_level)
            self.level += level_difference
            self.weapons[weapons_input_int] = new_weapon

    def get_level_with_weapons(self):
        level = self.level
        for weapon in self.weapons:
            if weapon.vital_status.extra_level:
                level += weapon.vital_status.extra_level
        return level

    def set_start_position(self):
        if self.game:
            self.position = self.game.board_map.get_start_position()

    def can_cross_walls(self):
        for weapon in self.weapons:
            if weapon.specialty == Specialty.CROSS_WALLS:
                return True

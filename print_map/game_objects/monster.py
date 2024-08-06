from .vitalStatus import VitalStatus
from .weapon import Weapon


class Monster:
    def __init__(self, name: str, uses_magic: bool, vital_status: VitalStatus, weapon=None):
        self._name = name
        self._uses_magic = uses_magic
        self._vital_status = vital_status
        self._weapon = weapon
        self._game = None

    def __str__(self):
        return 'Monster '+self._name

    # Getter and setter for name
    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if not value or not isinstance(value, str):
            raise Exception('Can not create a Monster without name, it also needs to be a string.')
        self._name = value

    # Getter and setter for uses_magic
    @property
    def uses_magic(self):
        return self._uses_magic

    @uses_magic.setter
    def uses_magic(self, value):
        if value is None or not isinstance(value, bool):
            raise Exception('The uses_magic attribute of the monster needs to be a Boolean.')
        self._uses_magic = value

    # Getter and setter for vital_status
    @property
    def vital_status(self):
        return self._vital_status

    @vital_status.setter
    def vital_status(self, value):
        if not isinstance(value, VitalStatus):
            raise Exception('Vital status of the monster needs to be a VitalStatus instance.')
        self._vital_status = value

    # Getter and setter for weapon
    @property
    def weapon(self):
        return self._weapon

    @weapon.setter
    def weapon(self, value):
        if value and not isinstance(value, Weapon):
            raise Exception('Weapon of the monster needs to be a Weapon instance.')
        self._weapon = value

    # Getter and setter for game
    @property
    def game(self):
        return self._game

    @game.setter
    def game(self, value):
        self._game = value

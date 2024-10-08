from .vitalStatus import VitalStatus
from .weapon import Weapon


class Monster:
    def __init__(self, name: str, uses_magic: bool, vital_status: VitalStatus, weapon=None):
        if not name or not isinstance(name, str):
            raise (Exception, "Monster must have a valid name as a string.")
        if not vital_status or not isinstance(vital_status, VitalStatus):
            raise ValueError("Monster's vital_status must be a VitalStatus instance.")
        if uses_magic is None or not isinstance(uses_magic, bool):
            raise TypeError("Monster's uses_magic attribute must be a boolean.")
        if weapon and not isinstance(weapon, Weapon):
            raise TypeError("Monster's weapon must be a Weapon instance if provided.")
        self._name = name
        self._uses_magic = uses_magic
        self._vital_status = vital_status
        self._weapon = weapon
        self._game = None

    def __str__(self):
        return f'Monster {self._name}'

    # Getter and setter for name
    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if not value or not isinstance(value, str):
            raise ValueError('Monster name must be a non-empty string.')
        self._name = value

    # Getter and setter for uses_magic
    @property
    def uses_magic(self):
        return self._uses_magic

    @uses_magic.setter
    def uses_magic(self, value):
        if value is None or not isinstance(value, bool):
            raise TypeError('The uses_magic attribute of the monster needs to be a boolean.')
        self._uses_magic = value

    # Getter and setter for vital_status
    @property
    def vital_status(self):
        return self._vital_status

    @vital_status.setter
    def vital_status(self, value):
        if not isinstance(value, VitalStatus):
            raise TypeError('Vital status of the monster needs to be a VitalStatus instance.')
        self._vital_status = value

    # Getter and setter for weapon
    @property
    def weapon(self):
        return self._weapon

    @weapon.setter
    def weapon(self, value):
        if value and not isinstance(value, Weapon):
            raise TypeError('Weapon of the monster needs to be a Weapon instance.')
        self._weapon = value

    # Getter and setter for game
    @property
    def game(self):
        return self._game

    @game.setter
    def game(self, value):
        self._game = value

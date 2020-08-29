from .vitalStatus import VitalStatus
from .weapon import Weapon


class Monster:
    def __init__(self, name, uses_magic, vital_status, weapon=None):
        if not name or not isinstance(name, str):
            raise(Exception, 'Can not create a Monster without name, it also needs to be an string.')

        if not vital_status or not isinstance(vital_status, VitalStatus):
            raise(Exception, 'Vital status of the monster needs to be a VitalStatus instance.')
        if uses_magic is None or not isinstance(uses_magic, bool):
            raise(Exception, 'The uses_magic attribute of the monster needs to be a Boolean.')
        if weapon and not isinstance(weapon, Weapon):
            raise(Exception, 'Weapon of the monster needs to be a Weapon instance.')

        self.name = name
        self.uses_magic = uses_magic
        self.vital_status = vital_status
        self.weapon = weapon
        self.game = None

    def __str__(self):
        return 'Monster '+self.name

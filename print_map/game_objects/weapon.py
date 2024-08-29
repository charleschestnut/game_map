from enum import Enum

from .vitalStatus import VitalStatus


class Specialty(Enum):
    CROSS_WALLS = 1
    PORTAL_SELECTION = 2
    NEVER_SURPRISE_BATTLE = 3

Specialty_list = ''

class Weapon:
    def __init__(self, name, description, vital_status, specialty=None):
        if not name or len(name) > 20 or len(name) < 3:
            raise ValueError('The length of the name must be between 4 and 20 characters.')

        if not description or len(description) > 200 or len(description) < 10:
            raise ValueError('The length of the description must be between 10 and 200 characters.')

        if not isinstance(vital_status, VitalStatus):
            raise ValueError('The vital status of the weapon must be a valid VitalStatus instance.')

        if specialty and not isinstance(specialty, Specialty):
            raise ValueError(f"The Weapon's specialty must be none or it needs "
                             f"to be inside of {str(Specialty)}")

        self.name = name
        self.description = description
        self.vital_status = vital_status
        self.specialty = specialty

    def __str__(self):
        return (f"WEAPON:\n"
                f"Name: {self.name}: {self.description[:20]}...\n"
                f"VITAL STATUS: {self.vital_status}\n"
                f"SPECIALTY: {self.specialty}")

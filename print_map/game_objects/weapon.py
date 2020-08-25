from .vitalStatus import VitalStatus


class Weapon:
    def __init__(self, name, description, vital_status):
        if name:
            if len(name) < 3:
                raise (Exception, 'The length of the name must be longer than 10 characters')
        if description:
            if len(description) < 10:
                raise(Exception, 'The length of the description must be longer than 10 characters')
        if not vital_status:
            raise (Exception, 'The vital status of the weapon can not be None.')
        if not isinstance(vital_status, VitalStatus):
            raise (Exception, 'The vital status of the weapon is not a VitalStatus instance')



        self.name = name
        self.description = description
        self.vital_status = vital_status

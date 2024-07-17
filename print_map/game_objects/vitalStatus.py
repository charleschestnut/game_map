class VitalStatus:

    def __init__(self, health, attack, magic_power, defense, magic_defense, status_proportion=None,
                 extra_level=None):

        for state in [health, attack, magic_power, defense, magic_defense]:
            if not state:
                raise Exception('The state can not be None.')
            elif not isinstance(state, int):
                raise Exception('The state must be an integer.')
            elif state <= 0:
                if status_proportion:
                    raise Exception('The state must be higher than zero.')

        if status_proportion:
            if len(status_proportion) != 5:
                raise Exception(
                    "Upgrade list must content 5 elements: hp, attack, magic power, "
                    "defense and magic defense.")
            for upgrade in status_proportion:
                if not upgrade:
                    raise Exception("Sorry, there's an upgrade that is None.")
                elif isinstance(upgrade, int):
                    raise Exception('The upgrades can only be floats.')
                elif upgrade <= 0:
                    raise Exception('The upgrades need to be greater than 0.0.')

            self.status_proportion = status_proportion
        else:
            self.status_proportion = []

        self.health = health
        self.attack = attack
        self.magic_power = magic_power
        self.defense = defense
        self.magic_defense = magic_defense
        if extra_level:
            self.extra_level = extra_level
        else:
            self.extra_level = 0

    def __str__(self):
        res = ('HP: ' + str(self.health) + '\n'
               + 'ATK: ' + str(self.attack) + '\n'
               + 'M. PWR: ' + str(self.magic_power) + '\n'
               + 'DEF: ' + str(self.defense) + '\n'
               + 'M.DEF: ' + str(self.magic_defense))
        return res

    def get_vital_status_at_level(self, level):
        health = self.health
        attack = self.attack
        magic_power = self.magic_power
        defense = self.defense
        magic_defense = self.magic_defense
        for lvl in range(level-1):
            health *= (1 + self.status_proportion[0])
            attack *= (1 + self.status_proportion[1])
            magic_power *= (1 + self.status_proportion[2])
            defense *= (1 + self.status_proportion[3])
            magic_defense *= (1 + self.status_proportion[4])
        health = int(health)
        attack = int(attack)
        magic_power = int(magic_power)
        defense = int(defense)
        magic_defense = int(magic_defense)
        return VitalStatus(health, attack, magic_power, defense, magic_defense)

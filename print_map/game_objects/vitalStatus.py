class VitalStatus:

    def __init__(self, health, attack, magic_power, defense, magic_defense, status_proportion=None, extra_level=None):

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
                    "Upgrade list must content 5 elements: hp, attack, magic power, defense and magic defense.")
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
        res = 'HP: '+str(self.health)+'\n'+'ATK: '\
        +str(self.attack)+'\n'+'M. PWR: '\
        +str(self.magic_power)+'\n'\
        +'DEF: '+str(self.defense)+'\n'\
        +'M.DEF: '+str(self.magic_defense)
        return res

    def get_vital_status_at_level(self, level):

        for lvl in range(level-1):
            self.health *= (1 + self.status_proportion[0])
            self.attack *= (1 + self.status_proportion[1])
            self.magic_power *= (1 + self.status_proportion[2])
            self.defense *= (1 + self.status_proportion[3])
            self.magic_defense *= (1 + self.status_proportion[4])
        self.health = int(self.health)
        self.attack = int(self.attack)
        self.magic_power = int(self.magic_power)
        self.defense = int(self.defense)
        self.magic_defense = int(self.magic_defense)
        return self

class VitalStatus:

    def __init__(self, health: int, attack: int, magic_power: int, defense: int, magic_defense: int,
                 status_proportion=None, extra_level=None):
        # Validate the primary attributes
        for state, name in zip([health, attack, magic_power, defense, magic_defense],
                               ['health', 'attack', 'magic_power', 'defense', 'magic_defense']):
            if state is None:
                raise ValueError(f"{name} cannot be None.")
            if not isinstance(state, int):
                raise TypeError(f"{name} must be an integer.")
            if state <= 0:
                if status_proportion:
                    raise ValueError(f"{name} must be greater than zero.")

        # Validate status_proportion if provided
        if status_proportion:
            if len(status_proportion) != 5:
                raise ValueError(
                    "Upgrade list must contain 5 elements: hp, attack, magic power, defense, "
                    "and magic defense.")
            for upgrade in status_proportion:
                if upgrade is None:
                    raise ValueError("Each upgrade in the list cannot be None.")
                if not isinstance(upgrade, float):
                    raise TypeError("Upgrades must be floats.")
                if upgrade <= 0:
                    raise ValueError("Each upgrade must be greater than zero.")

            self.status_proportion = status_proportion
        else:
            self.status_proportion = [0.0] * 5  # Default to a list of 5 zeroes

        self.health = health
        self.attack = attack
        self.magic_power = magic_power
        self.defense = defense
        self.magic_defense = magic_defense
        self.extra_level = extra_level if extra_level is not None else 0

    def __str__(self):
        return (f"HP: {self.health}\n"
                f"ATK: {self.attack}\n"
                f"M. PWR: {self.magic_power}\n"
                f"DEF: {self.defense}\n"
                f"M.DEF: {self.magic_defense}")

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

        return VitalStatus(
            health=int(health),
            attack=int(attack),
            magic_power=int(magic_power),
            defense=int(defense),
            magic_defense=int(magic_defense))

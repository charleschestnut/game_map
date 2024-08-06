from . import VitalStatus
from .character import Character
from .monster import Monster
import random


class Battle:
    def __init__(self, character: Character):
        if not character:
            raise (Exception, '')

        self.is_surprise = bool(random.getrandbits(1))
        self._dice_damage = round(random.uniform(-0.5, 0.5), 1)
        self.character = character
        self.monster = character.game.get_random_monster()
        self.has_won = False

    # Getter and setter for is_surprise
    @property
    def is_surprise(self):
        return self._is_surprise

    @is_surprise.setter
    def is_surprise(self, value):
        self._is_surprise = value

    # Getter and setter for dice_damage
    @property
    def dice_damage(self):
        return self._dice_damage

    # Getter and setter for character
    @property
    def character(self):
        return self._character

    @character.setter
    def character(self, value):
        self._character = value

    # Getter and setter for monster
    @property
    def monster(self):
        return self._monster

    @monster.setter
    def monster(self, value):
        self._monster = value

    # Getter and setter for has_won
    @property
    def has_won(self):
        return self._has_won

    @has_won.setter
    def has_won(self, value):
        self._has_won = value

    def realise(self):
        character_hp = self.character.vital_status.health
        monster_hp = self.monster.vital_status.health
        character_status = self.character.get_total_vital_status()

        character_damage, monster_damage = self.get_damages_in_battle(character_status)

        acc = 0
        if self.is_surprise:
            while character_hp > 0 and monster_hp > 0:
                acc += 1
                character_hp -= monster_damage
                if character_hp <= 0:
                    break
                monster_hp -= character_damage
        else:
            while character_hp > 0 and monster_hp > 0:
                acc += 1
                monster_hp -= character_damage
                if monster_hp <= 0:
                    break
                character_hp -= monster_damage
        has_won = self.finish_battle(character_hp)
        return has_won, acc

    def get_damages_in_battle(self, character_status: VitalStatus):
        if self.character.uses_magic:
            character_damage = int(character_status.magic_power * self.dice_damage)\
                            - self.monster.vital_status.magic_defense
        else:
            character_damage = int(character_status.attack * self.dice_damage) \
                            - self.monster.vital_status.defense
        if self.monster.uses_magic:
            monster_damage = self.monster.vital_status.magic_power\
                             - character_status.magic_defense
        else:
            monster_damage = self.monster.vital_status.attack \
                             - character_status.defense
        if character_damage <= 0:
            character_damage = 1
        if monster_damage <= 0:
            monster_damage = 1
        return character_damage, monster_damage

    def finish_battle(self, character_hp):
        if character_hp > 0:
            self.character.level += 1
            if self.monster.weapon:
                self.character.add_weapon(self.monster.weapon)
            return True
        else:
            self.character.game.characters_alive.remove(self.character)
            return False

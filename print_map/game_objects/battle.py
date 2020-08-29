from .character import Character
from .monster import Monster
import random


class Battle:
    def __init__(self, character):
        if not character or not isinstance(character, Character):
            raise (Exception, '')

        self.is_surprise = bool(random.getrandbits(1))
        self.dice_damage = round(random.uniform(-0.5, 0.5), 1)
        self.character = character
        self.monster = character.game.get_random_monster()
        self.has_won = False

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

    def get_damages_in_battle(self, character_status):
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
            print("NO MUEREEEEEEEEEEEEEE")
            self.character.level += 1
            if self.monster.weapon:
                self.character.add_weapon(self.monster.weapon)
            return True
        else:
            print("HA MUERTO0000000000000000000")
            self.character.game.characters_alive.remove(self.character)
            return False

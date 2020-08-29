from .character import Character
from .monster import Monster
import random


class Battle:
    def __init__(self, character):
        if not character or not isinstance(character, Character):
            raise (Exception, '')

        self.is_surprise = bool(random.getrandbits(1))
        self.dice_damage = random.uniform(-0.5, 0.5)
        self.character = character
        self.monster = character.board_map.get_random_monster()

    def realise(self):
        character_hp = self.character.vital_status.health
        monster_hp = self.monster.vital_status.health
        if character.uses_magic:
            character_damage = int(self.character.vital_status.magic * self.dice_damage)\
                            - self.monster.vital_status.magic_deffense
        else:
            character_damage = int(self.character.vital_status.attack * self.dice_damage) \
                            - self.monster.vital_status.deffense
        if monster.uses_magic:
            monster_damage = self.monster.vital_status.magic\
                             - self.character.vital_status.magic_deffense
        else:
            monster_damage = self.monster.vital_status.attack \
                             - self.character.vital_status.deffense
        # TODO Añadir categoría, si el character es melé o es mágico.
        # Para así usar ataque o magia y defensa o defensa mágica.
        if self.is_surprise:
            while character_hp > 0 and monster_hp > 0:
                character_hp -= monster_damage
                if character_hp <= 0:
                    break
                monster_hp -= character_damage
        else:
            while character_hp > 0 and monster_hp > 0:
                monster_hp -= character_damage
                if monster_hp <= 0:
                    break
                character_hp -= monster_damage

        if character_hp > 0:
            self.character.level += 1
            if self.monster.weapon:
                self.character.add_weapon(self.monster.weapon)
        else:
            self.character.board_map.characters_alive.remove(self.character)


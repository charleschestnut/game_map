from .consoleInterface import ConsoleInterface
from .character import Character
from .monster import Monster
from .weapon import Weapon
from .consoleInterface import ConsoleInterface
from .battle import Battle
import random


class Game:
    def __init__(self, board_map):
        self.board_map = board_map
        self.characters = []
        self.characters_alive = []
        self.monsters = []
        self.weapons = []

    def append_character(self, character):
        if isinstance(character, Character):
            if character not in self.characters:
                self.characters.append(character)
                self.characters_alive.append(character)
                character.game = self
                character.set_start_position()
        else:
            raise(Exception, 'To append a character to the game, use a character instance')

    def append_character_list(self, character_list):
        if character_list:
            [self.append_character(c) for c in character_list]

    def remove_character(self, character):
        if character in self.characters:
            self.characters.remove(character)
            self.characters_alive.remove(character)
            character.game = None

    def remove_character_alive(self, character):
        if character in self.characters_alive:
            self.characters_alive.remove(character)

    def append_monster(self, monster):
        if isinstance(monster, Monster):
            if monster not in self.monsters:
                self.monsters.append(monster)
                monster.game = self
        else:
            raise (Exception, 'To append a monster to the game, use a monster instance')

    def append_monster_list(self, monster_list):
        if monster_list:
            [self.append_monster(m) for m in monster_list]

    def remove_monster(self, monster):
        if monster in self.monsters:
            self.monsters.remove(monster)
            monster.game = None

    def get_random_monster(self):
        return random.choice(self.monsters)

    def append_weapon(self, weapon):
        if isinstance(weapon, Weapon):
            if weapon not in self.weapons:
                self.weapons.append(weapon)
                weapon.game = self
        else:
            raise (Exception, 'To append a weapon to the game, use a weapon instance')

    def append_weapon_list(self, weapon_list):
        if weapon_list:
            [self.append_weapon(w) for w in weapon_list]

    def remove_weapon(self, weapon):
        if weapon in self.weapons:
            self.weapons.remove(weapon)
            weapon.game = None

    def has_any_character_won(self):
        has_won = False
        for character in self.characters_alive:
            square_character = self.board_map.get_square_by_position(character.position.x, character.position.y)
            if square_character.type == 5:
                has_won = True
                break
        return has_won

    def start_game_console(self):
        winner = None
        ConsoleInterface.welcome()
        while len(self.characters_alive) > 0 or not self.has_any_character_won:
            for character in self.characters_alive:
                ConsoleInterface.print_map(self.board_map, self.board_map.get_square_types_list())
                actual_square = self.board_map.get_square_by_position(character.position.x, character.position.y)
                dice = ConsoleInterface.throw_dice(actual_square.position, character.name)
                available_squares = actual_square.get_available_squares(dice)
                selected_square = ConsoleInterface.select_available_squares(available_squares)
                character.set_position(selected_square.position)
                if selected_square.type == 3:  # BATTLE
                    battle = Battle(character)
                    has_won, rounds = battle.realise()
                    ConsoleInterface.print_finish_battle(battle, has_won, rounds)
                elif selected_square.type == 4:  # FINISH
                    winner = character
                    break
                elif selected_square.type == 5:  #
                    ''
                elif selected_square.type == 6:  #
                    ''
                elif selected_square.type == 7:  #
                    ''
        ConsoleInterface.finish_game(self, winner)

    def start_game_only_movement(self):
        winner = None
        ConsoleInterface.welcome()
        while len(self.characters_alive) > 0 and not self.has_any_character_won():
            for character in self.characters_alive:
                ConsoleInterface.print_map(self.board_map, self.board_map.get_square_types_list())
                actual_square = self.board_map.get_square_by_position(character.position.x, character.position.y)
                dice = ConsoleInterface.throw_dice(actual_square.position, character.name)
                available_squares = actual_square.get_available_squares(dice)
                selected_square = ConsoleInterface.select_available_squares(available_squares)
                character.set_position(selected_square.position)

                if selected_square.type == 5:
                    winner = character
                    break
        ConsoleInterface.finish_game(self, winner)

from .character import Character
from .monster import Monster
from .weapon import Weapon
from .consoleInterface import ConsoleInterface
from .battle import Battle
from .boardMap import BoardMap
import random


class Game:
    def __init__(self, board_map: BoardMap):
        self._board_map = board_map
        self._characters = []
        self._characters_alive = []
        self._current_character = None
        self._monsters = []
        self._weapons = []

    # Getter for board_map
    @property
    def board_map(self):
        return self._board_map

    # Getter for characters
    @property
    def characters(self):
        return self._characters

    # Getter for characters_alive
    @property
    def characters_alive(self):
        return self._characters_alive

    # Getter for monsters
    @property
    def monsters(self):
        return self._monsters

    # Getter for weapons
    @property
    def weapons(self):
        return self._weapons

    @property
    def current_character(self):
        return self._current_character

    @current_character.setter
    def current_character(self, character: Character):
        if character in self.characters_alive:
            self._current_character = character

    def append_character(self, character: Character):
        if not isinstance(character, Character):
            raise TypeError('To append a character to the game, use a character instance')

        if character not in self.characters:
            self.characters.append(character)
            self.characters_alive.append(character)
            character.game = self
            character.set_start_position()

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
        if not isinstance(monster, Monster):
            raise TypeError('To append a monster to the game, use a monster instance')
        if monster not in self.monsters:
            self.monsters.append(monster)
            monster.game = self

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
        if not isinstance(weapon, Weapon):
            raise TypeError('To append a weapon to the game, use a weapon instance')
        if weapon not in self.weapons:
            self.weapons.append(weapon)
            weapon.game = self

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
            square_character = self.board_map.get_square_by_position(
                character.position.x, character.position.y)
            if square_character.type_square == 6:
                has_won = True
                break
        return has_won

    def start_game_console(self):
        winner = None
        ConsoleInterface.welcome()

        while len(self.characters_alive) > 0 and not self.has_any_character_won():
            for character in self.characters_alive:
                selected_square = self.dice_process(character)

                if selected_square.type_square == 3:  # BATTLE
                    battle = Battle(character)
                    has_won, rounds = battle.realise()
                    ConsoleInterface.print_finish_battle(battle, has_won, rounds)
                elif selected_square.type_square == 4:  # START POSITION
                    pass

                elif selected_square.type_square == 5:  # PORTAL
                    self.portal_process(character)

                elif selected_square.type_square == 6:  # FINISH
                    winner = character
                    character.position = selected_square.position
                    break
                elif selected_square.type_square == 7:  #
                    pass

            if winner:
                break
        ConsoleInterface.finish_game(self, winner)

    def start_game_only_movement(self):
        winner = None
        ConsoleInterface.welcome()

        while len(self.characters_alive) > 0 and not self.has_any_character_won():
            for character in self.characters_alive:
                selected_square = self.dice_process(character)

                if selected_square.type_square == 5:  # PORTAL
                    self.portal_process(character)
                elif selected_square.type_square == 6:
                    winner = character
                    character.position = selected_square.position
                    break
            if winner:
                break

        ConsoleInterface.finish_game(self, winner)

    def portal_process(self, character):
        portals = self.board_map.get_portals()
        selected_portal = ConsoleInterface.select_available_portal(portals,
                                                                   character.position)
        character.position = selected_portal

    def dice_process(self, character):
        ConsoleInterface.print_map(self.board_map, self.board_map.get_square_types_list(),
                                   character.position)
        print(f"YOUR CURRENT POSITION IS {character.position}")

        current_square = self.board_map.get_square_by_position(
            character.position.x, character.position.y)
        dice_roll = ConsoleInterface.throw_dice(current_square.position, character.name)

        available_squares = current_square.get_available_squares(dice_roll, character)

        selected_square = ConsoleInterface.select_available_squares(available_squares)
        character.position = selected_square.position

        return selected_square

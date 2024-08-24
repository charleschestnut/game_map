import random
from typing import List
from .position import Position

# Define constants for wall types
EMPTY = 0
MONSTER = 3
START = 4
PORTAL = 5
FINISH = 6
TREASURE = 7
NORMAL_WALL = 1
FAKE_WALL = 2

# Define wall symbols
NORMAL_WALL_SYMBOLS = [
    '¤', '║', '═', '╔', '║', '║', '╚', '╠', '═', '╗', '═', '╦', '╝', '╣', '╩', '╬'
]
FAKE_WALL_SYMBOLS = [
    'ø', '│', '-', '┌', '│', '│', '└', '├', '-', '┐', '-', '┬', '┘', '┤', '┴', '┼'
]


class ConsoleInterface:

    @staticmethod
    def print_map(boardmap, numeric_square_list, character_position=None):
        game_map = ''
        for acc in range(len(numeric_square_list)):
            game_map += square_to_string(boardmap, numeric_square_list, acc)
            # Si no es la última fila, añado salto de línea
            if (acc + 1) % boardmap.rows == 0 and int((acc + 1) / boardmap.rows) < boardmap.cols:
                game_map += '\n'
        if character_position:
            game_map = print_character_position(game_map, character_position)
        print(game_map)
        return game_map

    # WELCOME
    @staticmethod
    def welcome():
        string = """
        ############################################################################################
        #                                                                                          #
        #    #######  ##########  ####   ####  #######        #####   #####  #########  #######    #
        #    ##       ##      ##  ## ## ## ##  ##             ##  ## ##  ##  ##     ##  ##   ##    #
        #    ##       ##      ##  ##  ###  ##  ##             ##   ###   ##  ##     ##  ##   ##    #
        #    ## ####  ##########  ##   #   ##  ######   ####  ##    #    ##  #########  #######    #
        #    ##   ##  ##      ##  ##       ##  ##             ##         ##  ##     ##  ##         #
        #    #######  ##      ##  ##       ##  #######        ##         ##  ##     ##  ##         #
        #                                                                                          #
        ############################################################################################
        """
        print(string)

    # THROW DICE
    @staticmethod
    def throw_dice(position, character_name):
        dice = random.randint(1, 6)
        string = (character_name + " IT'S YOUR TURN! YOUR ACTUAL POSITION IS" +
                  str(position) + "YOU HAVE THROWN YOUR DICE AND THE RESULT IS...")
        if dice == 1:
            string += """
                 #####
                 ## ##
                    ##
                    ##
                 ########"""
        elif dice == 2:
            string += """
                 ########
                       ##
                 ########
                 ##
                 ########"""
        elif dice == 3:
            string += """
                 ########
                       ##
                 ########
                       ##
                 ########"""
        elif dice == 4:
            string += """
                 ##    ##
                 ##    ##
                 ########
                       ##
                       ##"""
        elif dice == 5:
            string += """
                 ########
                 ##
                 ########
                       ##
                 ########"""
        else:
            string += """
                 ########
                 ##
                 ########
                 ##    ##
                 ########"""
        print(string)
        return dice

    # SQUARES CONSOLE
    @staticmethod
    def select_available_squares(squares):
        def describe_square(index, square):
            descriptions = {
                0: "Square",
                3: "There's a monster.",
                4: "This is your start position of the game.",
                5: "There's a portal.",
                6: "YOU CAN WIN!",
                7: "There's a 7."
            }
            return (f"Square number {index}: {square.position} - "
                    f"{descriptions.get(square.type_square, 'Unknown type')}")

        max_index = len(squares) - 1
        str_input = (f'Introduce the number of any of this position to move '
                     f'your character (from 0 to {str(len(squares) - 1)}) \n')
        acc = 0
        for square in squares:
            str_input += describe_square(acc, square) + '\n'
            acc += 1

        # Input and validate user selection
        while True:
            index = input(str_input).strip()
            if index.isdigit():
                index_int = int(index)
                if 0 <= index_int <= max_index:
                    return squares[index_int]
            print('Invalid input. Please enter a number between 0 and ', max_index)


    # BATTLE CONSOLE
    @staticmethod
    def print_finish_battle(battle, has_won, acc):
        battle_string = """
        ##########                                      # \                       / #
        #  #  #  #                                      #  \                     /  #
        #        #                                      #############################
        ##########                                      ##   ..               ..   ##
            ##            ###      ###   #######        ##   # \             / #   ##
            ##             ##      ##    ##             ##   #__\           /__#   ##
        ##  ##  ##          ##    ##     #######        ##                         ##
         ########            ##  ##           ##        ##                         ##
            ##                ####       #######        ##   ##################    ##
            ##                                          ##   #/\/\/\/\/\/\/\/\#    ##
           ####                                         ##   ##################    ##
          ##  ##                                        ##                         ##
         ##    ##                                       #############################
        """
        print(battle_string)

        if has_won:
            win_message = """
            ###     ###  ########  ########  ##########  ########  ########  ##    ##    ##
             ##     ##      ##     ##            ##      ##    ##  ##    ##   ##  ##     ##
              ##   ##       ##     ##            ##      ##    ##  ########    ####      ##
               ## ##        ##     ##            ##      ##    ##  ##   ##      ##       
                ###      ########  ########      ##      ########  ##    ##     ##       ##
            """

            print(win_message)

            print(f'You have won in {str(acc)} iterations! Congratulations!\n'
                  f'Now you UPGRADED TO LEVEL {str(battle.character.level)}.\n'
                  f'Your current status is:\n'
                  f'{str( battle.character.get_total_vital_status())} \n'
                  f'Your current position is {str(battle.character.position)}')
        else:
            lose_message = ('You... HAVE LOST and HAVE BEEN REMOVED FROM THE GAME!!! \n'
                            "MUAHAHAHAHAHAHAHA!!!!! \n"
                            "...\n"
                            "I mean... You have been defeated, good luck next time!\n"
                            "PS: You have lost in only {str(acc)} interactions..\n."
                            "MY GRANNY WOULD SURVIVE BETTER THAN YOU MUAHAHAHAHA!!!!\n\n")
            print(lose_message)

    # PORTAL
    @staticmethod
    def select_available_portal(portals: List, character_position):
        # Remove character position from the portals list
        portals.remove(character_position)
        random_portal = random.choice(portals)
        portal_message = """
        You have entered into a... PORTAL!
        
                    .,-:;//;:=,
                 . :H@@@MM@M#H/.,+%;,
              ,/X+ +M@@M@MM%=,-%HMMM@X/,
             -+@MM; $M@@MH+-,;XMMMM@MMMM@+-
            ;@M@@M- XM@X;. -+XXXXXHHH@M@M#@/.
          ,%MM@@MH ,@%=            .---=-=:=,.
          -@#@@@MX .,              -%HX$$%%%+;
         =-./@M@M$                  .;@MMMM@MM:
         X@/ -$MM/                    .+MM@@@M$
        ,@M@H: :@:                    . -X#@@@@-
        ,@@@MMX, .                    /H- ;@M@M=
        .H@@@@M@+,                    %MM+..%#$.
         /MMMM@MMH/.                  XM@MH; -;
          /%+%$XHH@$=              , .H@@@@MX,
           .=--------.           -%H.,@@@@@MX,
           .%MM@@@HHHXX$$$%+- .:$MMX -M@@MM%.
             =XMMM@MM@MM#H;,-+HMM@M+ /MMMX=
               =%@M@M#@$-.=$@MM@@@M; %M%=
                 ,:+$+-,/H#MMMMMMM@- -,
                       =++%%%%+/:-.
        
        
        YOU HAVE BEEN TELEPORTED, YOU WERE ON {character_position} POSITION, 
        BUT YOUR CURRENT POSITION IS ACTUALLY {random_portal}.
        """.format(character_position=character_position, random_portal=random_portal)
        print(portal_message)
        return random_portal

    # WIN GAME
    @staticmethod
    def finish_game(game, winner):
        def format_loser_message(name):
            return (f"Come on, {name}. How could you lose in that way?\n"
                    "We're too embarrassed, really... Next time will be better...\n"
                    "I guess...\n")

        # Initialize the message
        if winner:
            result_message = (f'The winner is... {winner.name.upper()}!!! \n'
                              'CON-GRA-TU-LA-TIONS!!!\n'
                              "But not to your mates, who were horrible at playing. "
                              "Oh my goodness...\n\n\n")

            # Append messages for all non-winners
            result_message += ''.join(format_loser_message(character.name)
                                      for character in game.characters
                                      if character.name != winner.name)

        else:
            result_message = ''.join(format_loser_message(character.name)
                                     for character in game.characters)

        result_message += "\n\n\n I hope that you enjoyed this demo!\nSee you all soon!"
        print(result_message)


def print_character_position(printed_map, character_position: Position):
    printed_map_split = printed_map.split('\n')
    n_column = len(printed_map_split[0])
    x = character_position.x
    y = n_column - character_position.y - 1
    char_list = list(printed_map_split[y])
    char_list[x] = "@"
    printed_map_split[y] = ''.join(char_list)
    map_with_character = '\n'.join(printed_map_split)
    return map_with_character


def square_to_string(boardmap, numeric_square_list, index):
    x = index % boardmap.rows
    y = int(index / boardmap.rows)

    actual = is_wall(boardmap, numeric_square_list, x, y, True)
    left = is_wall(boardmap, numeric_square_list, x - 1, y, False)
    right = is_wall(boardmap, numeric_square_list, x + 1, y, False)
    top = is_wall(boardmap, numeric_square_list, x, y - 1, False)
    bottom = is_wall(boardmap, numeric_square_list, x, y + 1, False)
    wall = get_wall_type(actual, left, top, right, bottom)
    return wall


def is_wall(boardmap, numeric_square_list, x, y, is_actual_square):
    if x < 0 or x >= boardmap.rows or y < 0 or y >= boardmap.cols:
        return 0

    index = boardmap.rows * y + x
    square_value = numeric_square_list[index]

    if square_value in (NORMAL_WALL, FAKE_WALL):
        return square_value if is_actual_square else NORMAL_WALL
    return square_value if is_actual_square else EMPTY


def get_wall_type(actual, left, top, right, bottom):
    if actual == EMPTY:
        return ' '
    elif actual == MONSTER:
        return 'M'
    elif actual == START:
        return 'S'
    elif actual == PORTAL:
        return 'P'
    elif actual == FINISH:
        return 'F'
    elif actual == TREASURE:
        return 'T'
    elif actual == NORMAL_WALL:
        return get_wall_symbol(left, top, right, bottom, NORMAL_WALL_SYMBOLS)
    else:  # FAKE_WALL
        return get_wall_symbol(left, top, right, bottom, FAKE_WALL_SYMBOLS)


def get_wall_symbol(left, top, right, bottom, symbols):
    wall_binary_list = [left, top, right, bottom]
    wall_index = wall_binary_list_to_index(wall_binary_list)
    return symbols[wall_index]


def wall_binary_list_to_index(binary_list):
    binary_string = ''.join(map(str, binary_list))
    binary_index = int(binary_string, 2)
    return binary_index if binary_index < len(NORMAL_WALL_SYMBOLS) else 0
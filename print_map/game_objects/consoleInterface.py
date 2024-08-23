import random
from typing import List
from .position import Position


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
        str_input = ('Introduce the number of any of this position '
                     'to move your character (from 0 to ') + str(len(squares) - 1) + '): \n'
        acc = 0
        for square in squares:
            if square.type_square == 0:
                str_input += "Square number " + str(acc) + ": " + str(square.position) + ' \n'
            elif square.type_square == 3:
                str_input += ("Square number " + str(acc) + ": " + str(square.position) +
                              " - There's a monster.\n")
            elif square.type_square == 4:
                str_input += ("Square number " + str(acc) + ": " + str(square.position) +
                              " - This is your start position of the game\n")
            elif square.type_square == 5:
                str_input += ("Square number " + str(acc) + ": " + str(square.position) +
                              " - There's a portal.\n")
            elif square.type_square == 6:
                str_input += ("Square number " + str(acc) + ": " + str(square.position) +
                              " - YOU CAN WIN!.\n")
            elif square.type_square == 7:
                str_input += ("Square number " + str(acc) + ": " + str(square.position) +
                              " - There's a 7.\n")
            acc += 1

        index = input(str_input)
        try:
            index_int = int(index)
            assert (0 <= index_int <= len(squares) - 1)
            selected_square = squares[index_int]
        except ValueError:
            # Handle the case where index is not a valid integer
            selected_square = ConsoleInterface.select_available_squares(squares)
        except AssertionError:
            # Handle the case where index_int is out of range
            selected_square = ConsoleInterface.select_available_squares(squares)
        return selected_square

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
            string = """
            ###     ###  ########  ########  ##########  ########  ########  ##    ##    ##
             ##     ##      ##     ##            ##      ##    ##  ##    ##   ##  ##     ##
              ##   ##       ##     ##            ##      ##    ##  ########    ####      ##
               ## ##        ##     ##            ##      ##    ##  ##   ##      ##       
                ###      ########  ########      ##      ########  ##    ##     ##       ##
            """

            print(string)
            print('You have won in ' + str(acc) + ' iterations! Congratulations!\n'
                                                  'Now you UPGRADED TO LEVEL ' + str(
                battle.character.level) + '.\n'
                                          'Your current status is:\n' + str(
                battle.character.get_total_vital_status()) + '\n'
                                                             'Your current position is ' + str(
                battle.character.position))

        else:
            string = 'You... HAVE LOST and HAVE BEEN REMOVED FROM THE GAME!!! \n' \
                     "MUAHAHAHAHAHAHAHA!!!!! \n" \
                     "...\n" \
                     "I mean... You have been defeated, good luck next time!\n" \
                     "PS: You have lost in only " + str(acc) + " interactions..\n." \
                     "MY GRANNY WOULD SURVIVE BETTER THAN YOU MUAHAHAHAHA!!!!\n\n"
            print(string)

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
        string = ''
        if winner:
            string = 'The winner is...' + str(winner.name.upper()) + '!!! \n' \
                     "CON-GRA-TU-LA-TIONS!!!\n"\
                     "But not to your mates, that were horrrible " \
                     "playing, oh my godness...\n\n\n"
            for character in game.characters:
                if character.name != winner.name:
                    c_name = character.name
                    string += "Come on, " + str(c_name) + \
                              ". How could you lose in that way?\n" \
                              "We're too embarrased, really... Next time will be " \
                              "better...\n" \
                              "I guess...\n"

        else:
            for character in game.characters:
                c_name = character.name
                string = "Come on, " + str(c_name) + \
                         ". How could you lose in that way?\n" \
                         "We're too embarrased, really... Next time will be better...\n" \
                         "I guess...\n"
        string += "\n\n\n" \
                  "I hope that you enjoyed that demo!\n" \
                  "See you all soon!"
        print(string)


def print_character_position(printed_map, character_position: Position):
    printed_map_split = printed_map.split('\n')
    n_column = len(printed_map_split[0])
    x = character_position.x
    y = n_column - character_position.y
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
    if x == -1 or x >= boardmap.rows:
        return 0
    if y == -1 or y >= boardmap.cols:
        return 0
    index = boardmap.rows * y + x
    # El valor 1 será para las paredes normales, el 2 es para las paredes fakes
    if numeric_square_list[index] == 1 or numeric_square_list[index] == 2:
        if is_actual_square:
            return numeric_square_list[index]
        else:
            return 1
    else:
        if is_actual_square:
            return numeric_square_list[index]
        else:
            return 0


def get_wall_type(actual, left, top, right, bottom):
    if actual == 0:  # Empty
        return ' '
    elif actual == 3:  # Monster
        return 'M'
    elif actual == 4:  # Start point
        return 'S'
    elif actual == 5:  # PORTAL
        return 'P'
    elif actual == 6:  # FINISH POINT
        return 'F'
    elif actual == 7:  # TREASURE
        return 'T'

    elif actual == 1:
        return get_normal_wall([left, top, right, bottom])
    else:  # Fake wall -> actual == 2
        return get_fake_wall([left, top, right, bottom])


def get_normal_wall(wall_binary_list):
    if wall_binary_list == [0, 0, 0, 0]:
        return '¤'
    elif wall_binary_list == [0, 0, 0, 1]:
        return '║'
    elif wall_binary_list == [0, 0, 1, 0]:
        return '═'
    elif wall_binary_list == [0, 0, 1, 1]:
        return '╔'
    elif wall_binary_list == [0, 1, 0, 0]:
        return '║'
    elif wall_binary_list == [0, 1, 0, 1]:
        return '║'
    elif wall_binary_list == [0, 1, 1, 0]:
        return '╚'
    elif wall_binary_list == [0, 1, 1, 1]:
        return '╠'
    elif wall_binary_list == [1, 0, 0, 0]:
        return '═'
    elif wall_binary_list == [1, 0, 0, 1]:
        return '╗'
    elif wall_binary_list == [1, 0, 1, 0]:
        return '═'
    elif wall_binary_list == [1, 0, 1, 1]:
        return '╦'
    elif wall_binary_list == [1, 1, 0, 0]:
        return '╝'
    elif wall_binary_list == [1, 1, 0, 1]:
        return '╣'
    elif wall_binary_list == [1, 1, 1, 0]:
        return '╩'
    else:
        return '╬'


def get_fake_wall(wall_binary_list):
    if wall_binary_list == [0, 0, 0, 0]:
        return 'ø'
    elif wall_binary_list == [0, 0, 0, 1]:
        return '│'
    elif wall_binary_list == [0, 0, 1, 0]:
        return '-'
    elif wall_binary_list == [0, 0, 1, 1]:
        return '┌'
    elif wall_binary_list == [0, 1, 0, 0]:
        return '│'
    elif wall_binary_list == [0, 1, 0, 1]:
        return '│'
    elif wall_binary_list == [0, 1, 1, 0]:
        return '└'
    elif wall_binary_list == [0, 1, 1, 1]:
        return '├'
    elif wall_binary_list == [1, 0, 0, 0]:
        return '-'
    elif wall_binary_list == [1, 0, 0, 1]:
        return '┐'
    elif wall_binary_list == [1, 0, 1, 0]:
        return '-'
    elif wall_binary_list == [1, 0, 1, 1]:
        return '┬'
    elif wall_binary_list == [1, 1, 0, 0]:
        return '┘'
    elif wall_binary_list == [1, 1, 0, 1]:
        return '┤'
    elif wall_binary_list == [1, 1, 1, 0]:
        return '┴'
    else:
        return '┼'

from print_map.game_objects import Battle, BoardMap, Character, ConsoleInterface, Monster, \
    Game, Position, VitalStatus, Weapon


SQUARES = [1, 1, 1, 1, 1, 1, 1, 1, 1,
           1, 4, 0, 0, 0, 0, 0, 0, 1,
           1, 0, 3, 1, 0, 1, 3, 0, 1,
           1, 0, 2, 1, 0, 1, 1, 0, 1,
           1, 0, 0, 0, 3, 0, 0, 0, 1,
           1, 0, 1, 1, 0, 1, 1, 0, 1,
           1, 0, 3, 1, 0, 2, 3, 0, 1,
           1, 5, 0, 0, 0, 0, 6, 5, 1,
           1, 1, 1, 1, 1, 1, 1, 1, 1]
ROWS = 9
COLS = 9

board_map = BoardMap(ROWS, COLS)
board_map.create_squares_of_boardmap(SQUARES)

status_proportion = [0.5, 0.5, 0.7, 0.9, 0.8]
v_status_character = VitalStatus(10, 3, 4, 6, 20, status_proportion)

character_1 = Character("Onion knight", False, v_status_character)
character_2 = Character("Time knight", False, v_status_character)

game = Game(board_map)
game.append_character_list([character_1, character_2])


if __name__ == '__main__':
    game.start_game_only_movement()
from print_map.game_objects import Battle, BoardMap, Character, ConsoleInterface, Monster, \
    Game, Position, VitalStatus, Weapon


SQUARES = [1, 1, 1, 1, 1, 1, 1, 1, 1,
           1, 4, 0, 0, 0, 0, 0, 0, 1,
           1, 0, 3, 1, 0, 1, 3, 0, 1,
           1, 0, 2, 1, 0, 1, 1, 0, 1,
           1, 0, 0, 0, 3, 0, 0, 0, 1,
           1, 0, 1, 1, 0, 1, 1, 0, 1,
           1, 0, 3, 1, 0, 2, 3, 0, 1,
           1, 5, 0, 0, 0, 0, 0, 5, 1,
           1, 1, 1, 1, 1, 1, 1, 1, 1]
ROWS = 9
COLS = 9

board_map = BoardMap(ROWS, COLS)
board_map.create_squares_of_boardmap(SQUARES)

status_proportion = [0.5, 0.5, 0.7, 0.9, 0.8]

v_status_character = VitalStatus(10, 3, 4, 6, 20, status_proportion)
v_status_weapon_1 = VitalStatus(2, 3, -1, 5, 1, None, 1)
v_status_weapon_2 = VitalStatus(2, 3, -2, 4, 1, None, 0)
v_status_weapon_3 = VitalStatus(2, 3, 5, 5, 3, None, -1)
v_status_weapon_4 = VitalStatus(2, 3, -1, 5, 1, None, 1)
v_status_weapon_5 = VitalStatus(1, 1, 1, 1, 1, None, 0)
v_status_weapon_6 = VitalStatus(1, 1, 3, 1, 1, None, 0)
v_status_weapon_7 = VitalStatus(10, 1, 6, 2, 1, None, 0)
v_status_monster_1 = VitalStatus(10, 10, 10, 10, 10)
v_status_monster_2 = VitalStatus(7, 3, 10, 1, 1)
v_status_monster_3 = VitalStatus(1000, 1000, 1000, 1000, 1000)

weapon_1 = Weapon("Super sword", "This sword cuts what it wants.", v_status_weapon_1)
weapon_2 = Weapon("Super shield", "This sword cuts what it wants.", v_status_weapon_2)
weapon_3 = Weapon("Super hat", "This hat makes you invisible.", v_status_weapon_3)
weapon_4 = Weapon("Super boots", "Those boots let you pass though poisoned rivers.", v_status_weapon_4)
weapon_5 = Weapon("Super book", "This book increases your magic power.", v_status_weapon_5)
weapon_6 = Weapon("Super bow", "This bow throws arrows faster than sound.", v_status_weapon_6)
weapon_7 = Weapon("Super face", "This face is stronger than any shield built for America Captain.", v_status_weapon_7)

character_1 = Character("Onion knight", False, v_status_character)
character_2 = Character("Time knight", False, v_status_character)

monster_1 = Monster('Goomba', True, v_status_monster_1, weapon_7)
monster_2 = Monster('Dragon', False, v_status_monster_2)
monster_3 = Monster('Instant death', False, v_status_monster_3)

game = Game(board_map)
game.append_character_list([character_1, character_2])
game.append_monster_list([monster_1, monster_2, monster_3])
game.append_weapon_list([weapon_1, weapon_2, weapon_3, weapon_4, weapon_5, weapon_6, weapon_7])


if __name__ == '__main__':
    game.start_game_console()

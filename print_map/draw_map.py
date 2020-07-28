
from draw_first_map import draw_square
from round_squares import round_map


vertical_walls = [1, 1]
horizontal_walls_1 = [1, 0]
col_1 = 1,
row_1 = 1

VERTICAL_WALLS_2 = [0, 1, 0, 1, 0, 0, 1, 0, 1, 0, 1, 0, 0, 0, 1, 1, 0, 1, 0, 1, 1, 1, 0, 1, 0]
HORIZONTAL_WALLS_2 = [0, 1, 1, 0, 0, 0, 0, 0, 1, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 0]
COL_2 = 4
ROW_2 = 5

VERTICAL_3 = [1, 0, 0, 0, 0, 1, 1, 0, 1, 1, 0, 1, 1, 0, 0, 0, 0, 1, 1, 0, 1, 1, 0, 1, 1, 0, 0, 0, 0, 1]
HORIZONTAL_3 = [1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1]
MONSTERS_3 = [0, 0, 0, 1, 0, 0, 1, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 1]
ROW_3 = 5
COL_3 = 5

# Método para el mapa
def get_list_of_positions(list, rows, cols):
    counter = 0
    list_position = []
    for l in list:
        x = int(counter/rows)
        y = counter % rows
        list_position.append([x, y])
        counter += 1
    return list_position

def get_square_of_map(map, x, y):
    map_matrix = map.splitlines()
    # Una casilla tiene 3x9 caracteres
    square = ""
    counter = 0
    for line in map_matrix:
        if 3*y <= counter < 3*(y+1):
            square += line[9*x: 9*(x+1)]
            square += '\n'
        counter += 1
    return square



def print_map(horizontal_walls, vertical_walls, rows, cols):
    map = ""
    for counter_row in range(rows):
        map_0 = ""
        map_1 = ""
        map_2 = ""

        for counter_col in range(cols):
            casilla_idx = cols * (rows - 1 - counter_row) + counter_col
            map_0, map_1, map_2 = draw_square(map_0, map_1, map_2, casilla_idx,
                                                  horizontal_walls, vertical_walls,
                                                  rows, cols, counter_col, counter_row)

        map_0 += '\n'
        map_1 += '\n'
        map_2 += '\n'
        map += map_0 + map_1 + map_2
    print(map)
    map_rounded = round_map(map, horizontal_walls, vertical_walls, rows, cols)
    print(map_rounded)
    return map_rounded


#print_map(horizontal_walls_2, vertical_walls_2, row_2, col_2)
map_1 = print_map(HORIZONTAL_3, VERTICAL_3, ROW_3, COL_3)
square_0_0 = get_square_of_map(map_1, 0, 0)
square_1_1 = get_square_of_map(map_1, 1, 1)
print(square_1_1)
print(square_0_0)

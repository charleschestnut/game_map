
from draw_first_map import draw_square
from round_squares import round_map
from insert_types_square import insert_types_square

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
DICT_TYPES_LIST_3 = {
    "MONSTER": [0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    "START": [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    "FINISH": [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1]
}
ROW_3 = 5
COL_3 = 5


def print_map(horizontal_walls, vertical_walls, rows, cols, dict_types_square):
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
    map_rounded = round_map(map, horizontal_walls, vertical_walls, rows, cols)
    map_typed = insert_types_square(map_rounded, dict_types_square, rows)
    return map_rounded


#print_map(horizontal_walls_2, vertical_walls_2, row_2, col_2)
print_map(HORIZONTAL_3, VERTICAL_3, ROW_3, COL_3, DICT_TYPES_LIST_3)

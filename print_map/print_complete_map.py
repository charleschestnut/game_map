import numpy
from draw_first_map import print_basic_map
from insert_walls import print_walls
from auxiliary_methods import rotate_90_degrees_list
from insert_type_squares import insert_types_square




def print_complete_map(dict_types, horizontal_walls, vertical_walls, rows, cols):
    map = print_basic_map(rows, cols)
    map_walled = print_walls(map, horizontal_walls, vertical_walls, rows, cols)
    dict_types_rotated = rotate_90_degrees_list(dict_types, rows, cols)
    map_typed = insert_types_square(map_walled, dict_types_rotated, rows)
    return map_typed


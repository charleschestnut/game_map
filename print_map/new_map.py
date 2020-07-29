ROWS_1 = 5
COLS_1 = 5
VERTICAL_1 = [1, 0, 0, 0, 0, 1, 1, 0, 1, 1, 0, 1, 1, 0, 0, 0, 0, 1, 1, 0, 1, 1, 0, 1, 1, 0, 0, 0, 0, 1]
HORIZONTAL_1 = [1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1]


def insert_horizontal_walls(map_matrix, horizontal_walls, rows):
    counter = 0
    for h_w in horizontal_walls:
        if h_w == 1:
            row = int(counter / rows) * 3
            start = (counter % rows) * 4
            end = start + 5
            replace_count = 5
            line_wall = map_matrix[row][start: end]
            line_wall_edit = line_wall.replace('.', '#', replace_count)
            map_matrix[row] = map_matrix[row][:start] + line_wall_edit + map_matrix[row][end:]
        counter += 1
    return map_matrix


def insert_vertical_walls(map_matrix, vertical_walls, cols):
    counter = 0
    c = 0
    for v_w in vertical_walls:
        if v_w == 1:
            row = int(counter / (cols + 1)) * 3  # SI NO FUNCIONA CON OTRO MAPA, CAMBIAR COLS POR ROWS
            start = (counter % (cols +1)) * 4
            replace_count = 4
            for i in range(replace_count):
                wall_character = '#'
                map_matrix[row+i] = map_matrix[row+i][:start] + wall_character + map_matrix[row+i][start+1:]
            c += 1
        counter += 1
    return map_matrix

def print_walls(map, horizontal_walls, vertical_walls, rows, cols):
    map_matrix = map.splitlines()
    map_matrix_with_h_walls = insert_horizontal_walls(map_matrix, horizontal_walls, rows)
    map_matrix_full_h_v_walls = insert_vertical_walls(map_matrix_with_h_walls, vertical_walls, cols)

    map_walled = ''
    for line in map_matrix_full_h_v_walls:
        for c in line:
            map_walled += c
        map_walled += '\n'
    return map_walled


def print_basic_map(rows, cols):

    length_cols = cols * 4 + 1
    length_rows = rows * 3 + 1

    map = ''
    for r in range(length_rows):
        is_row_line = r == 0 or r % 3 == 0
        for c in range(length_cols):
            is_col_line = c == 0 or c % 4 == 0
            if is_row_line or is_col_line:
                map += '.'
            else:
                map += ' '
        map += '\n'
    print(map)
    return map

def create_complete_map(horizontal_walls, vertical_walls, rows, cols):
    map = print_basic_map(rows, cols)
    map_walled = print_walls(map, horizontal_walls, vertical_walls, rows, cols)
    #map_typed = print_types()
    return map_walled
print(create_complete_map(HORIZONTAL_1, VERTICAL_1, ROWS_1, COLS_1))

#print(print_basic_map(2, 2))

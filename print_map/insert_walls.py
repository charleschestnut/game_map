from auxiliary_methods import matrix_to_map


def insert_horizontal_walls(map_matrix, horizontal_walls, rows):
    counter = 0
    for h_w in horizontal_walls:
        if h_w == 1:
            row = int(counter / rows) * 3
            start = (counter % rows) * 8
            end = start + 9
            replace_count = 9
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
            start = (counter % (cols + 1)) * 8
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

    map_walled = matrix_to_map(map_matrix_full_h_v_walls)
    return map_walled

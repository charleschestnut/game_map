from auxiliary_methods import matrix_to_map


def get_square_of_map(map_matrix, x, y, str_replace):
    # Una casilla tiene 3x9 caracteres
    for line in range(len(map_matrix)):
        if 3 * y <= line < 3 * (y + 1):
            start = 8 * x
            end = 8 * (x + 1)
            line_square = map_matrix[line][start:end]
            line_square_edit = line_square.replace('       ', str_replace)
            map_matrix[line] = map_matrix[line][:start] + line_square_edit + map_matrix[line][end:]

    return map_matrix


def print_map_square_types(map, dict_type_list):
    map_matrix = map.splitlines()
    for type in dict_type_list:
        for m in dict_type_list[type]:
            if type == "MONSTER":
                map_matrix = get_square_of_map(map_matrix, m[0], m[1], '|M|.|M|')
            if type == "START":
                map_matrix = get_square_of_map(map_matrix, m[0], m[1], '|S|.|S|')
            if type == "FINISH":
                map_matrix = get_square_of_map(map_matrix, m[0], m[1], '|F|.|F|')
    new_map = matrix_to_map(map_matrix)

    return new_map


# Método para el mapa
def get_list_of_positions(list, rows):
    counter = 0
    list_position = []
    for l in list:
        if l ==1 :
            x = int(counter/rows)
            y = counter % rows
            list_position.append([x, y])
        counter += 1
    return list_position


def insert_types_square(map, dict_types, rows):
    new_dict = {}
    for type in dict_types:
        new_dict[type] = get_list_of_positions(dict_types[type], rows)
    map_types_inserted = print_map_square_types(map, new_dict)
    return map_types_inserted

def get_square_of_map(map, x, y, str_replace):
    map_matrix = map.splitlines()
    # Una casilla tiene 3x9 caracteres
    new_map = ""
    counter = 0
    for line in range(len(map_matrix)):
        if 3*y <= counter < 3*(y)+2:
            start = 9*x
            end = 9*(x)+6
            line_square = map_matrix[line][start:end]
            line_square_edit = line_square.replace('   ', str_replace)
            map_matrix[line] = map_matrix[line][:start] + line_square_edit + map_matrix[line][end:]
        counter += 1

    for row in map_matrix:
        for c in row:
            new_map += c
        new_map += '\n'

    return new_map


def print_map_square_types(map, dict_type_list):
    for type in dict_type_list:
        for m in dict_type_list[type]:
            if type == "MONSTER":
                map = get_square_of_map(map, m[0], m[1], '|M|')
            if type == "START":
                map = get_square_of_map(map, m[0], m[1], '|S|')
            if type == "FINISH":
                map = get_square_of_map(map, m[0], m[1], '|F|')
    print(map)
    return map


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

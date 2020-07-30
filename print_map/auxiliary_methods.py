def matrix_to_map(matrix):
    map = ''
    for line in matrix:
        for c in line:
            map += c
        map += '\n'
    return map


def rotate_90_degrees_list(dict_types, rows, cols):
    for type in dict_types:
        square_list = dict_types[type]
        new_list = [None] * (rows * cols)
        for counter in range(len(square_list)):
            x, y = int(counter / rows), counter % cols
            x_1, y_1 = y, cols - x - 1

            new_idx = x_1 * rows + y_1
            new_list[new_idx] = square_list[counter]
        dict_types[type] = new_list
    return dict_types

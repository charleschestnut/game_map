
def check_is_left(square, col):
    if square % col == 0:
        return 1
    else:
        return 0


def check_is_bottom(square, col):
    if int(square / col) == 0:
        return 1
    else:
        return 0


def check_is_top(square, col):
    if int(square / col) == col:
        return 1
    else:
        return 0


def check_is_right(square, col):
    if square % col == col - 1:
        return 1
    else:
        return 0


def round_corners(map_matrix, vertical_walls, horizontal_walls, casilla_idx, rows, cols, counter_row, counter_col):
    l = vertical_walls[casilla_idx + rows - 1 - counter_row]
    r = vertical_walls[casilla_idx + rows - counter_row]
    b = horizontal_walls[casilla_idx]
    t = horizontal_walls[casilla_idx + cols]

    on_right = check_is_right(casilla_idx, cols)
    on_left = check_is_left(casilla_idx, cols)
    on_top = check_is_top(casilla_idx, cols)
    on_bottom = check_is_bottom(casilla_idx, cols)

    if l and b and not on_left and not on_bottom:  # esquina |_
        map_matrix[3 * (counter_row + 1)][9 * counter_col - 3: 9 * counter_col] = '###'
        # map_matrix[3 * (counter_row + 1)][9 * counter_col - 3: 9 * counter_col] = '%%%'
        ''
    elif l and t and not on_left and not on_top:  # esquina |-
        map_matrix[3 * counter_row - 1][9 * (counter_col) - 3: 9 * (counter_col)] = '###'
        # map_matrix[3 * counter_row - 1][9 * (counter_col)-3: 9 * (counter_col)] = 'XXX'
    elif r and b and not on_right and not on_bottom:  # esquina _|
        map_matrix[3 * (counter_row + 1)][9 * (counter_col + 1): 9 * (counter_col + 1) + 3] = '###'
        # map_matrix[3 * (counter_row + 1)][9 * (counter_col+1): 9 * (counter_col+1)+3] = '***'
    elif r and t and not on_right and not on_top:  # esquina -|
        map_matrix[3 * counter_row - 1][9 * (counter_col + 1): 9 * (counter_col + 1) + 3] = '###'
        # map_matrix[3 * counter_row - 1][9 * (counter_col+1): 9 * (counter_col+1)+3] = '@@@'

    return map_matrix


def round_map(map, horizontal_walls, vertical_walls, rows, cols):
    map_list = map.splitlines()
    map_matrix = [[character for character in row] for row in map_list]
    new_map = ""
    for counter_row in range(rows):
        for counter_col in range(cols):
            casilla_idx = cols * (rows - 1 - counter_row) + counter_col
            map_matrix = round_corners(map_matrix, vertical_walls,
                                       horizontal_walls, casilla_idx,
                                       rows, cols, counter_row, counter_col)

    for row in map_matrix:
        for c in row:
            new_map += c
        new_map += '\n'
    return new_map
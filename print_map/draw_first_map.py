SQUARES = [
    [["         "], ["         "], ["         "]],
    [["###      "], ["###      "], ["###      "]],  # L
    [["      ###"], ["      ###"], ["      ###"]],  # R
    [["#########"], ["         "], ["         "]],  # T
    [["         "], ["         "], ["#########"]],  # B

    [["###      "], ["###      "], ["#########"]],  # LB 5
    [["#########"], ["###      "], ["###      "]],  # LT

    [["###   ###"], ["###   ###"], ["###   ###"]],  # LR 7
    [["#########"], ["      ###"], ["      ###"]],  # RT

    [["      ###"], ["      ###"], ["#########"]],  # RB 9
    [["#########"], ["         "], ["#########"]],  # TB

    [["###   ###"], ["###   ###"], ["#########"]],  # LBR 11
    [["#########"], ["###      "], ["#########"]],  # LBT

    [["#########"], ["###   ###"], ["###   ###"]],  # LTR 13
    [["#########"], ["      ###"], ["#########"]],  # BTR

    [["#########"], ["###   ###"], ["#########"]],  # 15
    [["#########"], ["#########"], ["#########"]]  #

]


def convert_map_square(str_0, str_1, str_2, square_number):
    str_0 += SQUARES[square_number][0][0]
    str_1 += SQUARES[square_number][1][0]
    str_2 += SQUARES[square_number][2][0]
    return str_0, str_1, str_2


def draw_square(map_0, map_1, map_2, casilla_idx, horizontal_walls, vertical_walls, rows, cols, counter_col, counter_row):
    l = vertical_walls[casilla_idx + rows - 1 - counter_row]
    r = vertical_walls[casilla_idx + rows - counter_row]
    b = horizontal_walls[casilla_idx]
    t = horizontal_walls[casilla_idx + cols]

    if l and r and t and b:
        return convert_map_square(map_0, map_1, map_2, 15)
    elif l and r and t and not b:
        return convert_map_square(map_0, map_1, map_2, 13)
    elif l and r and not t and b:
        return convert_map_square(map_0, map_1, map_2, 11)
    elif l and r and not t and not b:
        return convert_map_square(map_0, map_1, map_2, 7)
    elif l and not r and t and b:
        return convert_map_square(map_0, map_1, map_2, 12)
    elif l and not r and t and not b:
        return convert_map_square(map_0, map_1, map_2, 6)
    elif l and not r and not t and b:
        return convert_map_square(map_0, map_1, map_2, 5)
    elif l and not r and not t and not b:
        return convert_map_square(map_0, map_1, map_2, 1)

    if not l and r and t and b:
        return  convert_map_square(map_0, map_1, map_2, 14)
    elif not l and r and t and not b:
        return convert_map_square(map_0, map_1, map_2, 8)
    elif not l and r and not t and b:
        return convert_map_square(map_0, map_1, map_2, 9)
    elif not l and r and not t and not b:
        return convert_map_square(map_0, map_1, map_2, 2)
    elif not l and not r and t and b:
        return convert_map_square(map_0, map_1, map_2, 10)
    elif not l and not r and t and not b:
        return convert_map_square(map_0, map_1, map_2, 3)
    elif not l and not r and not t and b:
        return convert_map_square(map_0, map_1, map_2, 4)
    elif not l and not r and not t and not b:
        return convert_map_square(map_0, map_1, map_2, 0)

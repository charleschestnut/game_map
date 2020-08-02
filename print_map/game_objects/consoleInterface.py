from .boardMap import BoardMap


class ConsoleInterface:

    @staticmethod
    def print_map(boardmap):
        map = ''
        for acc in range(len(boardmap.squares)):
            map += square_to_string(boardmap, acc)
            # Si no es la última fila, añado salto de línea
            if (acc + 1) % boardmap.rows == 0 and int((acc + 1) / boardmap.rows) < boardmap.cols:
                map += '\n'
        print(map)
        return map


def square_to_string(boardmap, index):
    x = index % boardmap.rows
    y = int(index / boardmap.rows)

    actual = is_wall(boardmap, x, y, True)
    left = is_wall(boardmap, x - 1, y, False)
    right = is_wall(boardmap, x + 1, y, False)
    top = is_wall(boardmap, x, y - 1, False)
    bottom = is_wall(boardmap, x, y + 1, False)
    wall = get_wall_type(actual, left, top, right, bottom)
    return wall


def is_wall(boardmap, x, y, is_actual_square):
    if x == -1 or x >= boardmap.rows:
        return 0
    if y == -1 or y >= boardmap.cols:
        return 0
    index = boardmap.rows * y + x
    # El valor 1 será para las paredes normales, el 2 es para las paredes fakes
    if boardmap.squares[index] == 1 or boardmap.squares[index] == 2:
        if is_actual_square:
            return boardmap.squares[index]
        else:
            return 1
    else:
        if is_actual_square:
            return boardmap.squares[index]
        else:
            return 0


def get_wall_type(actual, left, top, right, bottom):
    print('actual', actual)
    if actual == 0:  # Empty
        return ' '
    elif actual == 3:  # Monster
        return 'M'
    elif actual == 4:  # Start point
        return 'S'
    elif actual == 5:  # Finish point
        return 'F'
    elif actual == 6:  # Treasure
        return 'T'
    elif actual == 7:  # Portal
        return 'P'

    elif actual == 1:
        return get_normal_wall([left, top, right, bottom])
    else:  # Fake wall -> actual == 2
        return get_fake_wall([left, top, right, bottom])


def get_normal_wall(wall_binary_list):
    if wall_binary_list == [0, 0, 0, 0]:
        return '¤'
    elif wall_binary_list == [0, 0, 0, 1]:
        return '║'
    elif wall_binary_list == [0, 0, 1, 0]:
        return '═'
    elif wall_binary_list == [0, 0, 1, 1]:
        return '╔'
    elif wall_binary_list == [0, 1, 0, 0]:
        return '║'
    elif wall_binary_list == [0, 1, 0, 1]:
        return '║'
    elif wall_binary_list == [0, 1, 1, 0]:
        return '╚'
    elif wall_binary_list == [0, 1, 1, 1]:
        return '╠'
    elif wall_binary_list == [1, 0, 0, 0]:
        return '═'
    elif wall_binary_list == [1, 0, 0, 1]:
        return '╗'
    elif wall_binary_list == [1, 0, 1, 0]:
        return '═'
    elif wall_binary_list == [1, 0, 1, 1]:
        return '╦'
    elif wall_binary_list == [1, 1, 0, 0]:
        return '╝'
    elif wall_binary_list == [1, 1, 0, 1]:
        return '╣'
    elif wall_binary_list == [1, 1, 1, 0]:
        return '╩'
    else:
        return '╬'


def get_fake_wall(wall_binary_list):
    if wall_binary_list == [0, 0, 0, 0]:
        return 'ø'
    elif wall_binary_list == [0, 0, 0, 1]:
        return '│'
    elif wall_binary_list == [0, 0, 1, 0]:
        return '-'
    elif wall_binary_list == [0, 0, 1, 1]:
        return '┌'
    elif wall_binary_list == [0, 1, 0, 0]:
        return '│'
    elif wall_binary_list == [0, 1, 0, 1]:
        return '│'
    elif wall_binary_list == [0, 1, 1, 0]:
        return '└'
    elif wall_binary_list == [0, 1, 1, 1]:
        return '├'
    elif wall_binary_list == [1, 0, 0, 0]:
        return '-'
    elif wall_binary_list == [1, 0, 0, 1]:
        return '┐'
    elif wall_binary_list == [1, 0, 1, 0]:
        return '-'
    elif wall_binary_list == [1, 0, 1, 1]:
        return '┬'
    elif wall_binary_list == [1, 1, 0, 0]:
        return '┘'
    elif wall_binary_list == [1, 1, 0, 1]:
        return '┤'
    elif wall_binary_list == [1, 1, 1, 0]:
        return '┴'
    else:
        return '┼'

def print_basic_map(rows, cols):

    length_cols = cols * 8 + 1
    length_rows = rows * 3 + 1

    map = ''
    for r in range(length_rows):
        is_row_line = r == 0 or r % 3 == 0
        for c in range(length_cols):
            is_col_line = c == 0 or c % 8 == 0
            if is_row_line or is_col_line:
                map += '.'
            else:
                map += ' '
        map += '\n'
    return map
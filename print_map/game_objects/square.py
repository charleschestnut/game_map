class Square:

    def __init__(self, position, type, boardmap):
        if position.x == -1 or position.x >= boardmap.rows:
            raise TypeError('Position.X value ('+str(position.x)+') is out of range (0, '+str(boardmap.rows)+')')
        if position.y == -1 or position.y >= boardmap.cols:
            raise TypeError('Position.Y value ('+str(position.y)+') is out of range (0, '+str(boardmap.cols))

        self.position = position
        self.type = type
        self.boardmap = boardmap


    def get_availables_squares(self, map, dice_number):
        available_squares = calc_available_squares(map, dice_number, None, positions = [])
        return available_squares

    def calc_available_squares(map_square, dice_number, direction, positions = []):
        return ''
        '''    if direction is not None:
        map_square = next_axis_position(direction, map_square)

        if dice_number == 0:
            positions.append(map_square)

        else:
            dice_number -= 1
            directions = calc_directions(map_square, direction)
            for direction_value in directions:
                get_map_squares_availables(map_square, dice_number, direction_value, positions)
    else:
        dice_number -= 1
        directions = calc_directions(map_square, direction)
        for direction_value in directions:
            get_map_squares_availables(map_square, dice_number,
                                      direction_value, positions)
    return list(set(positions))'''


    '''def next_axis_position(direction, map_square):
    axis_position = map_square.axis_position
    if direction == WALLS_VALUES['L'] or direction == WALLS_VALUES['R'] or \
            direction == WALLS_VALUES['T'] or direction == WALLS_VALUES['B']:

        if direction == WALLS_VALUES['L']:
            filter_square = Q(axis_position__x_axis=axis_position.x_axis - 1) & \
                            Q(axis_position__y_axis=axis_position.y_axis)

        elif direction == WALLS_VALUES['R']:
            filter_square = Q(axis_position__x_axis=axis_position.x_axis + 1) & \
                            Q(axis_position__y_axis=axis_position.y_axis)

        elif direction == WALLS_VALUES['T']:
            filter_square = Q(axis_position__x_axis=axis_position.x_axis) & \
                            Q(axis_position__y_axis=axis_position.y_axis + 1)

        else:
            filter_square = Q(axis_position__x_axis=axis_position.x_axis) & \
                            Q(axis_position__y_axis=axis_position.y_axis - 1)

        map_game = MapGame.objects.get(id=map_square.map_id)
        map_square_2 = MapSquare.objects.all().filter(map__name__exact=map_game.name).filter(filter_square)[0]

        return map_square_2
    else:
        print('Wrong direction movement. Only can be: L, R, T, B')'''
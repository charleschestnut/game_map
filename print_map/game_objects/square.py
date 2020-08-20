class Square:

    def __init__(self, position, type, boardmap):
        if position.x == -1 or position.x >= boardmap.rows:
            raise TypeError(
                'Position.X value (' + str(position.x) + ') is out of range (0, ' + str(boardmap.rows) + ')')
        if position.y == -1 or position.y >= boardmap.cols:
            raise TypeError('Position.Y value (' + str(position.y) + ') is out of range (0, ' + str(boardmap.cols))

        self.position = position
        self.type = type
        self.boardmap = boardmap

    def __str__(self):
        return str(self.position)+' - type: '+str(self.type)

    def can_move_to_direction(self, direction):
        next_square = None
        if direction == 'L':
            next_square = self.boardmap.get_square_by_position(self.position.x - 1, self.position.y) #TODO
        elif direction == 'R':
            next_square = self.boardmap.get_square_by_position(self.position.x + 1, self.position.y)
        elif direction == 'T':
            next_square = self.boardmap.get_square_by_position(self.position.x, self.position.y + 1)
        elif direction == 'B':
            next_square = self.boardmap.get_square_by_position(self.position.x, self.position.y - 1)

        if next_square.type == 1:
            return False
        elif next_square.type == 2:
            # Ver si el personaje de la casilla tiene o no el objeto posible para el movimiento
            # Mientras tanto, hace el mismo efecto que si es una pared normal
            return False
        else:
            return True

    def get_availables_squares(self, dice_number):
        available_squares = self.calc_available_squares(self, dice_number, None, positions=[])
        return available_squares

    @staticmethod
    def calc_available_squares(map_square, dice_number, direction, positions=[]):
        if direction is not None:
            map_square = map_square.next_axis_position(direction)
            if dice_number == 0:
                positions.append(map_square)

            else:
                dice_number -= 1
                directions = map_square.calc_possible_directions()
                for direction_value in directions:
                    map_square.calc_available_squares(map_square, dice_number,
                                               direction_value, positions)
        else:
            dice_number -= 1
            directions = map_square.calc_possible_directions()
            for direction_value in directions:
                map_square.calc_available_squares(map_square, dice_number,
                                           direction_value, positions)
        return list(set(positions))

    def calc_possible_directions(self):
        available_directions = []
        for dir in ['L', 'R', 'T', 'B']:
            if self.can_move_to_direction(dir):
                available_directions.append(dir)
        return available_directions

    def next_axis_position(self, direction):
        position = self.position
        if direction == 'L' or direction == 'R' or \
                direction == 'T' or direction == 'B':

            if direction == 'L':
                next_square = self.boardmap.get_square_by_position(position.x - 1, position.y)

            elif direction == 'R':
                next_square = self.boardmap.get_square_by_position(position.x + 1, position.y)

            elif direction == 'T':
                next_square = self.boardmap.get_square_by_position(position.x, position.y + 1)

            else:
                next_square = self.boardmap.get_square_by_position(position.x, position.y - 1)

            return next_square
        else:
            print('Wrong direction movement. Only can be: L, R, T, B')

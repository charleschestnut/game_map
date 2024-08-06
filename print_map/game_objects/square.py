from .position import Position


class Square:

    @property
    def boardmap(self):
        return self._boardmap

    def __init__(self, position, type_square, boardmap):
        if (not isinstance(position, Position) or position.x >= boardmap.cols or
                position.y >= boardmap.rows):
            raise Exception("Position is not a valid position instance")
        elif type_square not in range(8):
            raise Exception("The valid types of square are between 0 and 8")

        self._position = position
        self._type_square = type_square
        self._boardmap = boardmap

    @property
    def position(self):
        return self._position

    @position.setter
    def position(self, position):
        if position.x >= self._boardmap.cols:
            raise ValueError(
                f'Position.X value ({position.x}) is out of range (0, {self._boardmap.cols})')
        if position.y >= self._boardmap.rows:
            raise ValueError(
                f'Position.Y value ({position.y}) is out of range (0, {self._boardmap.rows})')
        self._position = position

    @property
    def type_square(self):
        return self._type_square

    @type_square.setter
    def type_square(self, value):
        if value not in range(8):  # Assuming type should be between 0 and 7 inclusive
            raise ValueError(f'Invalid type value: {value}')
        self._type_square = value

    @property
    def boardmap(self):
        return self._boardmap

    @boardmap.setter
    def boardmap(self, value):
        self._boardmap = value

    def __str__(self):
        return str(self.position) + ' - type_square: ' + str(self.type_square)

    def __lt__(self, other):
        if self.position.x == other.position.x:
            return self.position.y < other.position.y
        else:
            return self.position.x < other.position.x

    def can_move_to_direction(self, direction):
        next_square = None
        if direction == 'L':
            next_square = self.boardmap.get_square_by_position(self.position.x - 1, self.position.y)
        elif direction == 'R':
            next_square = self.boardmap.get_square_by_position(self.position.x + 1, self.position.y)
        elif direction == 'T':
            next_square = self.boardmap.get_square_by_position(self.position.x, self.position.y + 1)
        elif direction == 'B':
            next_square = self.boardmap.get_square_by_position(self.position.x, self.position.y - 1)

        if next_square.type_square == 1:
            return False
        elif next_square.type_square == 2:
            # Ver si el personaje de la casilla tiene o no el objeto posible para el movimiento
            # Mientras tanto, hace el mismo efecto que si es una pared normal
            return False
        else:
            return True

    def get_available_squares(self, dice_number):
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
                directions = map_square.calc_possible_directions(direction)
                for direction_value in directions:
                    map_square.calc_available_squares(map_square, dice_number,
                                                      direction_value, positions)
        else:
            dice_number -= 1
            directions = map_square.calc_possible_directions(direction)
            for direction_value in directions:
                map_square.calc_available_squares(map_square, dice_number,
                                                  direction_value, positions)
        return list(set(positions))

    def calc_possible_directions(self, direction):
        def remove_opposite_direction(directions, dir):
            if dir == 'L':
                directions.remove('R')
            elif dir == 'R':
                directions.remove('L')
            elif dir == 'T':
                directions.remove('B')
            elif dir == 'B':
                directions.remove('T')
            return directions

        available_directions = []
        for dir in ['L', 'R', 'T', 'B']:
            if self.can_move_to_direction(dir):
                available_directions.append(dir)
        if len(available_directions) > 1:
            available_directions = remove_opposite_direction(available_directions, direction)

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

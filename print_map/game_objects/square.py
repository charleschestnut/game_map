from . import BoardMap
from .position import Position


class Square:

    def __init__(self, position, type_square, boardmap):
        if not isinstance(position, Position):
            raise TypeError("Position must be an instance of the Position class.")
        if position.x >= boardmap.cols or position.y >= boardmap.rows:
            raise ValueError("Position is out of the boardmap boundaries.")
        if not isinstance(boardmap, BoardMap):  # Assuming BoardMap is a class
            raise TypeError("boardmap must be an instance of the BoardMap class.")
        if not (0 <= type_square < 8):
            raise ValueError("The valid types of square are between 0 and 7.")

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
        return f'{str(self.position)} - type_square: {str(self.type_square)}'

    def __lt__(self, other):
        if self.position.x == other.position.x:
            return self.position.y < other.position.y
        else:
            return self.position.x < other.position.x

    def can_move_to_direction(self, direction):
        directions_map = {
            'L': (-1, 0),  # Move Left (x - 1)
            'R': (1, 0),  # Move Right (x + 1)
            'T': (0, 1),  # Move Up (y + 1)
            'B': (0, -1)  # Move Down (y - 1)
        }

        if direction not in directions_map:
            raise ValueError(
                f"Invalid direction '{direction}'. Valid directions are 'L', 'R', 'T', 'B'.")

        dx, dy = directions_map[direction]
        next_square = self.boardmap.get_square_by_position(self.position.x + dx,
                                                           self.position.y + dy)

        if next_square is None:
            return False  # Out of bounds or invalid position
        elif next_square.type_square in {1, 2}:
            return False  # Can't move into walls or special type_square 2
        else:
            return True

    def get_available_squares(self, dice_number):
        available_squares = self.calc_available_squares(self, dice_number)
        return available_squares

    @staticmethod
    def calc_available_squares(map_square, dice_number, direction=None, positions=None):
        if positions is None:
            positions = []

        if dice_number < 0:
            return list(set(positions))

        if direction:
            map_square = map_square.next_axis_position(direction)

        if dice_number == 0:
            positions.append(map_square)
        else:
            dice_number -= 1
            directions = map_square.calc_possible_directions(direction)
            for direction_value in directions:
                # Recursive call for each possible direction
                map_square.calc_available_squares(map_square, dice_number, direction_value,
                                                  positions)

        return list(set(positions))

    def calc_possible_directions(self, direction):
        def remove_opposite_direction(directions, direction_selected):
            opposite_directions = {
                'L': 'R',
                'R': 'L',
                'T': 'B',
                'B': 'T'
            }
            opposite = opposite_directions.get(direction_selected)
            if opposite in directions:
                directions.remove(opposite)
            return directions

        available_directions = [d for d in ['L', 'R', 'T', 'B'] if self.can_move_to_direction(d)]

        if direction:
            available_directions = remove_opposite_direction(available_directions, direction)

        return available_directions

    def next_axis_position(self, direction):
        position = self.position
        direction_offsets = {
            'L': (-1, 0),
            'R': (1, 0),
            'T': (0, 1),
            'B': (0, -1)
        }

        if direction in direction_offsets:
            dx, dy = direction_offsets[direction]
            next_position = Position(position.x + dx, position.y + dy)
            next_square = self.boardmap.get_square_by_position(next_position.x, next_position.y)
            return next_square
        else:
            raise ValueError("Invalid direction. Only 'L', 'R', 'T', 'B' are allowed.")

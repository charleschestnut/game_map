from .position import Position
from .square import Square


class BoardMap:
    def __init__(self, rows, cols):
        if rows <= 0 or cols <= 0:
            raise (Exception, 'Can not create a Boardmap with rows or columns lower than ZERO (0)')
        self._rows = rows
        self._cols = cols
        self._squares = []

    # Getter and setter for rows
    @property
    def rows(self):
        return self._rows

    @rows.setter
    def rows(self, value):
        self._rows = value

    # Getter and setter for cols
    @property
    def cols(self):
        return self._cols

    @cols.setter
    def cols(self, value):
        self._cols = value

    # Getter and setter for squares
    @property
    def squares(self):
        return self._squares

    @squares.setter
    def squares(self, value):
        self._squares = value

    def get_portals(self):
        return [square.position for square in self.squares if square.type_square == 5]

    def create_squares_of_boardmap(self, squares):
        if len(self.squares) != 0:
            raise TypeError('The boardmap has all it squares: '
                            + str(len(self.squares) + 1) +
                            '. Please, check them and modify'
                            ' them if you want to append another one.')
        # We have to check the portals available in the map, they need to be:
        # Portals != 1
        if not _check_portal_pass_restrictions(squares):
            raise TypeError('The boardmap cannot have an unique portal. It needs to '
                            'have 0 or more than two.')

        # We have to check that there's always ONE only start position
        if not _check_start_position_restrictions(squares):
            raise TypeError('The boardmap must have an unique start position square')
        # We have to check that there's always one or more finish position
        if not _check_finish_position_restrictions(squares):
            raise TypeError('The boardmap must have, at least, one finish position square')

        for sq in squares:
            self.append_square(sq)

    def append_square(self, square_type_square):
        if len(self.squares) >= self.rows * self.cols:
            raise TypeError('The boardmap has all it squares: ' + str(len(self.squares)) +
                            '. Please, check them and modify'
                            ' them if you want to append another one.')
        cols = self.cols
        rows = self.rows
        index = len(self.squares)
        x = (index % cols)
        y = rows - 1 - (index // cols)
        square = Square(Position(x, y), square_type_square, self)
        self.squares.append(square)

    def modify_square(self, x, y, square):
        index = x * self.cols + y
        square.position.x = x
        square.position.y = y
        square.boardmap = self
        self.squares[index] = square

    def get_square_by_position(self, position_x, position_y):
        squares = self.squares
        for square in squares:
            if position_x == square.position.x and position_y == square.position.y:
                return square

    def get_start_position(self):
        for square in self.squares:
            if square.type_square == 4:
                return square.position

    def get_square_types_list(self):
        return [square.type_square for square in self.squares]


def _check_portal_pass_restrictions(squares):
    counter = len([1 for square in squares if square == 5])
    return counter != 1


def _check_start_position_restrictions(squares):
    counter = len([1 for square in squares if square == 4])
    return counter == 1


def _check_finish_position_restrictions(squares):
    counter = len([1 for square in squares if square == 6])
    return counter >= 1

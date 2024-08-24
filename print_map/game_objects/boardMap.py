from .position import Position


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

    def _generate_error_message(self, message):
        return f'Error: {message} Currently, there are {len(self.squares)} squares.'

    def create_squares_of_boardmap(self, squares):
        if self.squares:
            raise TypeError(self._generate_error_message(
                'The boardmap already contains squares. Modify existing ones if you want to add '
                'more.'))

        if not _check_portal_pass_restrictions(squares):
            raise TypeError(self._generate_error_message(
                'The boardmap must have either 0 or more than two portals.'))

        if not _check_start_position_restrictions(squares):
            raise TypeError(self._generate_error_message(
                'The boardmap must have exactly one start position square.'))

        if not _check_finish_position_restrictions(squares):
            raise TypeError(self._generate_error_message(
                'The boardmap must have at least one finish position square.'))

        for square in squares:
            self.append_square(square)

    def append_square(self, square_type_square):
        from .square import Square
        if len(self.squares) >= self.rows * self.cols:
            raise TypeError(
                f'The boardmap has all it squares {str(len(self.squares))}'
                f'Please, check them and modify them if you want to append another one.')

        # Calculate position of new square
        index = len(self.squares)
        x = (index % self.cols)
        y = self.rows - 1 - (index // self.cols)

        # Create and append Square
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

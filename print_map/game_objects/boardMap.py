from .position import Position


def check_is_playable(create_square_method):
    def wrapper(self, *args, **kwargs):
        # Call the original __init__ method to initialize the boardmap
        create_square_method(self, *args, **kwargs)

        if not _check_is_playable_boardmap(self):
            raise ValueError("The boardmap is not playable")
    return wrapper


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

    @check_is_playable
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

    def get_start_square(self):
        for square in self.squares:
            if square.type_square == 4:
                return square

    def get_finish_square(self):
        for square in self.squares:
            if square.type_square == 6:
                return square

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

def _check_is_playable_boardmap(boardmap, squares_tree=None, actual_square=None):
    finish_square = boardmap.get_finish_square()
    if squares_tree is None:
        start_square = boardmap.get_start_square()
        actual_square = start_square
        squares_tree = {start_square}

    contiguous_squares = actual_square.get_available_squares(dice_number=1)
    contiguous_squares_filter = [valor for valor in contiguous_squares if valor not in squares_tree]

    if finish_square in contiguous_squares_filter:
        return True

    squares_tree.add(actual_square)

    for square in contiguous_squares_filter:
        if _check_is_playable_boardmap(boardmap, squares_tree=squares_tree,
                                       actual_square=square):
            return True
    return False

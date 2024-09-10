class InvalidPositionError(Exception):
    pass


class InvalidCharacterError(Exception):
    pass


class WallError(InvalidPositionError):
    def __init__(self, position):
        super().__init__(f"The character cannot move to this position because "
                         f"the square at position {position} is a wall.")

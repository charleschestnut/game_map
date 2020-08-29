from .position import Position
from .square import Square
from .monster import Monster
import random

class BoardMap:
    def __init__(self, rows, cols):
        self.rows = rows
        self.cols = cols
        self.squares = []
        self.game = None

    def create_squares_of_boardmap(self, squares):
        if len(self.squares) != 0:
            raise TypeError('The boardmap has all it squares: ' + str(len(self.squares) + 1) +
                            '. Please, check them and modify'
                            ' them if you want to append another one.')
        for sq in squares:
            self.append_square(sq)

    def append_square(self, square_type):

        if len(self.squares) >= self.rows * self.cols:
            raise TypeError('The boardmap has all it squares: ' + str(len(self.squares)) +
                            '. Please, check them and modify'
                            ' them if you want to append another one.')
        index = len(self.squares)
        y = self.rows - 1 - int(index / self.rows)
        x = index % self.cols
        square = Square(Position(x, y), square_type, self)
        self.squares.append(square)

    def modify_square(self, x, y, square):
        index = x * cols + y
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
            if square.type == 4:
                return square.position

    def get_square_types_list(self):
        return [square.type for square in self.squares]
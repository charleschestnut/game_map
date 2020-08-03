class BoardMap:
    def __init__(self, rows, cols):
        self.rows = rows
        self.cols = cols
        self.squares = []

    def append_square(self, square):
        if len(self.squares) >= self.rows*self.cols:
            raise TypeError('The boardmap has all it squares: '+str(len(self.squares)+1) +
                            '. Please, check them and modify'
                            ' them if you want to append another one.')
        index = len(self.squares)
        x = index / self.rows
        y = index % self.cols
        square.position.x = x
        square.position.y = y

        self.squares.append(square)
        square.boardmap = self

    def modify_square(self, x, y, square):
        index = x * cols + y
        square.position.x = x
        square.position.y = y
        square.boardmap = self
        self.squares[index] = square

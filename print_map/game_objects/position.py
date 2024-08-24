class Position:
    def __init__(self, x, y):
        if (not isinstance(x, int) or x < 0) or (not isinstance(y, int) or y < 0):
            raise ValueError("The axis X and Y must be positive integer values.")
        self._x = x
        self._y = y

    def __str__(self):
        return '(' + str(self.x) + ', ' + str(self.y) + ')'

    @property
    def x(self):
        return self._x

    @x.setter
    def x(self, value):
        if not isinstance(value, int) or value < 0:
            raise ValueError("The axis X must be positive integer values.")
        self._x = value

    @property
    def y(self):
        return self._y

    @y.setter
    def y(self, value):
        if not isinstance(value, int) or value < 0:
            raise ValueError("The axis Y must be positive integer values.")
        self._y = value


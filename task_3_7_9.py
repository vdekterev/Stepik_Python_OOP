class Vector:
    def __init__(self, *coords):
        self.coords = [c for c in coords if type(c) in (int, float)]

    def __add__(self, other):
        if len(self.coords) != len(other.coords):
            raise ArithmeticError('размерности векторов не совпадают')
        return Vector(*[c1 + c2 for c1, c2 in zip(self.coords, other.coords)])

    def __sub__(self, other):
        if len(self.coords) != len(other.coords):
            raise ArithmeticError('размерности векторов не совпадают')
        return Vector(*[c1 - c2 for c1, c2 in zip(self.coords, other.coords)])

    def __mul__(self, other):
        if len(self.coords) != len(other.coords):
            raise ArithmeticError('размерности векторов не совпадают')
        return Vector(*[c1 * c2 for c1, c2 in zip(self.coords, other.coords)])

    def __iadd__(self, other):
        if type(other) == Vector and len(self.coords) != len(other.coords):
            raise ArithmeticError('размерности векторов не совпадают')
        if type(other) == int:
            self.coords = [c + other for c in self.coords]
        elif type(other) == Vector:
            return self.__add__(other)
        return self

    def __isub__(self, other):
        if type(other) == Vector and len(self.coords) != len(other.coords):
            raise ArithmeticError('размерности векторов не совпадают')
        if type(other) == int:
            self.coords = [c - other for c in self.coords]
        elif type(other) == Vector:
            return self.__sub__(other)
        return self

    def __eq__(self, other):
        return self.coords == other.coords

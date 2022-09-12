class RadiusVector2D:
    MIN_COORD = -100
    MAX_COORD = 1024

    def __init__(self, x=0, y=0):
        self.__x = self.__y = 0
        self.x = x
        self.y = y

    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, x: (int, float)):
        if self.__verify(x):
            self.__x = x

    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, y: (int, float)):
        if self.__verify(y):
            self.__y = y

    @staticmethod
    def norm2(vector):
        import math
        return pow(vector.x, 2) + pow(vector.y, 2)

    @classmethod
    def __verify(cls, n):
        return type(n) in (int, float) and RadiusVector2D.MIN_COORD <= n <= RadiusVector2D.MAX_COORD

class Point:
    def __init__(self, x: (int, float), y: (int, float)):
        self.__x = self.__y = 0
        if type(x) in (int, float) and  type(y) in (int, float):
            self.__x = x
            self.__y = y

    def get_coords(self):
        return self.__x, self.__y


class Rectangle:
    def __init__(self, a, b, c=None, d=None):
        self.__sp = self.__ep = None
        if isinstance(a, Point) and isinstance(b, Point):
            self.__sp = a
            self.__ep = b
        elif all(map(lambda x: type(x) in (int, float), (a, b, c, d))):
            self.__sp = Point(a, b)
            self.__ep = Point(c, d)

    def set_coords(self, sp, ep):
        self.__sp = sp
        self.__ep = ep

    def get_coords(self):
        return self.__sp, self.__ep

    def draw(self):
        print(f'Прямоугольник с координатами: {self.__sp.get_coords(), self.__ep.get_coords()}')


rect = Rectangle(Point(0, 0), Point(20, 34))
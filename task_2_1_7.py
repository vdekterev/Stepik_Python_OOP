class Line:
    def __init__(self, x1: int, y1: int, x2: int, y2: int):
        self.__x1, self.__y1 = x1, y1
        self.__x2, self.__y2 = x2, y2

    def set_coords(self, x1: int, y1: int, x2: int, y2: int):
        self.__x1, self.__y1 = x1, y1
        self.__x2, self.__y2 = x2, y2

    def get_coords(self):
        return self.__x1, self.__y1, self.__x2, self.__y2

    def draw(self):
        print(*[self.__x1, self.__y1, self.__x2, self.__y2])

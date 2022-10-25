class GamePole:
    __instance = None

    def __new__(cls, *args, **kwargs):
        if cls.__instance is None:
            cls.__instance = super().__new__(cls)
            return cls.__instance

    def __init__(self, N, M, total_mines):
        self.N = N
        self.M = M
        self.total_mines = total_mines
        self.__pole_cells = tuple()

    def init_pole(self):
        import random


    @property
    def pole(self):
        return self.__pole_cells


class Cell:
    def __init__(self):
        self.__is_mine = self.__number = self.__is_open = None

    @property
    def is_mine(self):
        return self.__is_mine

    @is_mine.setter
    def is_mine(self, value: bool):
        if type(value) == bool:
            self.__is_mine = value
        raise ValueError("недопустимое значение атрибута")

    @property
    def number(self):
        return self.__number

    @number.setter
    def number(self, n: int):
        if type(n) == int and 0 <= n <= 8:
            self.__number = n
        raise ValueError("недопустимое значение атрибута")

    @property
    def is_open(self):
        return self.__is_open

    @is_open.setter
    def is_open(self, value: bool):
        if type(value) == bool:
            self.__is_open = value
        raise ValueError("недопустимое значение атрибута")

    def __bool__(self):
        return self.__is_open


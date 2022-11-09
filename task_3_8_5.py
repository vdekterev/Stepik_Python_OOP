class IntegerValue:
    def __set_name__(self, owner, name):
        self.name = '_' + name

    def __set__(self, instance, value):
        if type(value) != int:
            raise ValueError('возможны только целочисленные значения')
        setattr(instance, self.name, value)

    def __get__(self, instance, owner):
        return getattr(instance, self.name)


class CellInteger:
    value = IntegerValue()

    def __init__(self, start_value=0):
        self.start_value = start_value


class TableValues:
    def __init__(self, rows: int, cols: int, cell=None):
        self.rows = rows if type(rows) == int else 0
        self.cols = cols if type(cols) == int else 0
        if cell is None:
            raise ValueError('параметр cell не указан')
        self.cells = tuple(tuple(cell() for _ in range(cols)) for _ in range(rows))

    def __check_index(self, value):
        col, row = value[0], value[1]
        if type(col) != int or type(row) != int:
            raise ValueError('col and row must be integers!')
        elif not(0 <= col <= self.cols and 0 <= row <= self.rows):
            raise IndexError('Index out of range!')

    def __getitem__(self, item):
        self.__check_index(item)
        return self.cells[item[0]][item[1]].value

    def __setitem__(self, key, value):
        self.__check_index(key)
        if type(value) != int:
            raise ValueError('возможны только целочисленные значения')
        self.cells[key[0]][key[1]] = value


table = TableValues(2, 3, cell=CellInteger)
table[0, 1] = 111

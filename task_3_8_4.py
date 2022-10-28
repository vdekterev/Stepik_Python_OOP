class Array:
    def __init__(self, max_length, cell):
        self.__array = [cell() for _ in range(max_length)]

    def __getitem__(self, item):
        if type(item) == int and 0 <= item <= len(self.__array):
            return self.__array[item].value
        raise IndexError('неверный индекс для доступа к элементам массива')

    def __setitem__(self, key, value):
        if not (0 <= key <= len(self.__array) - 1):
            raise IndexError('неверный индекс для доступа к элементам массива')
        self.__array[key].value = value

    def __repr__(self):
        return ' '.join(map(str, self.__array))


class Integer:
    def __init__(self, start_value=0):
        self.__value = start_value

    @property
    def value(self):
        return self.__value

    @value.setter
    def value(self, val):
        if type(val) != int:
            raise ValueError('должно быть целое число')
        self.__value = val

    def __repr__(self):
        return str(self.__value)

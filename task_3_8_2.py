class Record:
    def __init__(self, **fields):
        self.__dict__.update(**fields)
        self.keys = list(fields.keys())

    def __getitem__(self, item):
        if type(item) == int and 0 <= item <= len(self.keys) - 1:
            return self.__dict__[self.keys[item]]
        raise IndexError('неверный индекс поля')

    def __setitem__(self, key, value):
        try:
            self.__dict__[self.keys[key]] = value
        except IndexError:
            raise IndexError('неверный индекс поля')

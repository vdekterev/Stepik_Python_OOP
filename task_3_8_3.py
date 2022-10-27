class Track:
    def __init__(self, start_x, start_y):
        self.start_x = start_x
        self.start_y = start_y
        self.coords = []

    def add_point(self, x, y, speed):
        self.coords.append([(x, y), speed])

    def __getitem__(self, item):
        if type(item) == int and 0 <= item <= len(self.coords) - 1:
            return self.coords[item]
        else:
            raise IndexError('некорректный индекс')

    def __setitem__(self, key, value):
        if type(value) == int and 0 <= key <= len(self.coords) - 1:
            self.coords[key][1] = value
        else:
            raise IndexError('некорректный индекс')

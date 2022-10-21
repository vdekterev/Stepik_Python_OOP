class Ellipse:
    def __init__(self, *args):
        if args:
            self.x1 = args[0]
            self.y1 = args[1]
            self.x2 = args[2]
            self.y2 = args[3]

    def __bool__(self):
        return 'x1' in self.__dict__

    def get_coords(self):
        if not bool(self):
            raise AttributeError('нет координат для извлечения')
        return (self.x1, self.y1, self.x2, self.y2)


lst_geom = [Ellipse(), Ellipse(), Ellipse(1, 2, 3, 4), Ellipse(5, 6, 7, 8)]
for el in lst_geom:
    if bool(el):
        el.get_coords()

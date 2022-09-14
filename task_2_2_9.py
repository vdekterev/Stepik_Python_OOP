class PathLines:
    def __init__(self, *lines):
        if len(lines) > 0:
            self.lines = [[0, 0, lines[0].line_x, lines[0].line_y]]
        if len(lines) > 1:
            for l in lines[1:]:
                self.add_line(l)
        if len(lines) == 0:
            self.lines = []

    def get_path(self):
        return self.lines

    def get_length(self):
        from math import sqrt
        if len(self.lines) == 0:
            return 0
        L = 0
        x0, y0, x1, y1 = 0, 1, 2, 3
        for l in self.lines:
            L += sqrt((l[x1]-l[x0])**2 + (l[y1]-l[y0])**2)
        return L

    def add_line(self, line):
        self.lines.append([*self.lines[-1][-2:], line.x, line.y]
                          if len(self.lines) > 0 else [0, 0, line.x, line.y])


class LineTo:
    def __init__(self, x, y):   # координаты КОНЦА
        self.x = x
        self.y = y

    @property
    def line_x(self):
        return self.x

    @property
    def line_y(self):
        return self.y

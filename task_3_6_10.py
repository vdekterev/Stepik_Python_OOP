class Triangle:
    def __init__(self, a, b, c):
        self.a = self.checkvalue(a)
        self.b = self.checkvalue(b)
        self.c = self.checkvalue(c)
        if not self.a < self.b + self.c and self.b < self.a + self.c and self.c < self.a + self.b:
            raise ValueError("с указанными длинами нельзя образовать треугольник")

    @staticmethod
    def checkvalue(n):
        if type(n) in (int, float) and n > 0:
            return n
        raise ValueError("длины сторон треугольника должны быть положительными числами")

    def __len__(self):
        return int(self.a) + int(self.b) + int(self.c)

    def __call__(self, *args, **kwargs):
        from math import sqrt
        p = self.__len__() / 2
        return sqrt(p * (p-self.a) * (p-self.b) * (p-self.c))

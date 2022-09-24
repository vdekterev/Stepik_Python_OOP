class Box3D:
    def __init__(self, width, height, depth):
        self.width = self.height = self.depth = None
        if type(width) == int:
            self.width = width
        if type(height) == int:
            self.height = height
        if type(depth) == int:
            self.depth = depth

    def __add__(self, other):
        w = self.width + other.width
        h = self.height + other.height
        d = self.depth + other.depth
        return Box3D(w, h, d)

    def __radd__(self, other):
        return self.__add__(other)

    def __iadd__(self, other):
        return self.__add__(other)

    def __sub__(self, other):
        w = self.width - other.width
        h = self.height - other.height
        d = self.depth - other.depth
        return Box3D(w, h, d)

    def __rsub__(self, other):
        return self.__sub__(other)

    def __isub__(self, other):
        return self.__sub__(other)

    def __floordiv__(self, other):
        w = self.width // other
        h = self.height // other
        d = self.depth // other
        return Box3D(w, h, d)

    def __ifloordiv__(self, other):
        return self.__floordiv__(other)

    def __rfloordiv__(self, other):
        return self.__floordiv__(other)

    def __mod__(self, other):
        w = self.width % other
        h = self.height % other
        d = self.depth % other
        return Box3D(w, h, d)

    def __imod__(self, other):
        return self.__floordiv__(other)

    def __rmod__(self, other):
        return self.__floordiv__(other)

    def __mul__(self, other):
        w = self.width * other
        h = self.height * other
        d = self.depth * other
        return Box3D(w, h, d)

    def __rmul__(self, other):
        return self.__mul__(other)

    def get_dim(self):
        return self.width, self.height, self.depth

class Line:
    def __init__(self, x1, y1, x2, y2):
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2

    def __len__(self):
        from math import sqrt, pow
        return sqrt(pow(self.x2 - self.x1, 2) + pow(self.y2 - self.y1, 2)) >= 1

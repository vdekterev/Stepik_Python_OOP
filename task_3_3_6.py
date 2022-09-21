from math import sqrt, pow


class Complex:
    def __init__(self, real, img):
        self.__real = self.__img = None
        if self.is_digit(real):
            self.__real = real
        if self.is_digit(img):
            self.__img = img

    @staticmethod
    def is_digit(value):
        if type(value) in (int, float):
            return value

    @property
    def real(self):
        return self.__real

    @real.setter
    def real(self, value):
        if not self.is_digit(value):
            raise ValueError("Неверный тип данных.")
        self.__real = value

    @property
    def img(self):
        return self.__img

    @img.setter
    def img(self, value):
        if not self.is_digit(value):
            raise ValueError("Неверный тип данных.")
        self.__img = value

    def __abs__(self):
        return abs(sqrt(pow(self.__real, 2) + pow(self.__img, 2)))


cmp = Complex(7, 8)
cmp.real = 3
cmp.img = 4
c_abs = abs(cmp)

from math import sqrt, pow


class RadiusVector:
    def __init__(self, coord, *coords):
        if all(map(lambda x: type(x) in (int, float), coords)):
            if len(coords) == 0:
                self.__coords = [0] * coord
            else:
                self.__coords = [coord] + list(coords)
        else:
            raise ValueError('coords must be integers')

    def get_coords(self):
        return self.__coords

    def set_coords(self, *coords):
        if all(map(lambda x: type(x) in (int, float), coords)):
            n = min(len(self.__coords), len(coords))
            self.__coords[:n] = coords[:n]
        else:
            raise ValueError('coords must be integers')

    def __len__(self):
        return len(self.__coords)

    def __abs__(self):
        return sqrt(sum([pow(coord, 2) for coord in self.__coords]))

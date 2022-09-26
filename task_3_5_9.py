class Body:
    def __init__(self, name, ro, volume):
        self.name = 'Имя отсутствует'
        self.ro = self.volume = 0
        if type(name) == str:
            self.name = name
        if type(ro) in (int, float):
            self.ro = ro
        if type(volume) in (int, float):
            self.volume = volume
        self.m = self.ro * self.volume

    def __eq__(self, other):
        other_m = other.m if type(other) == 'Body' else other
        return self.m == other_m

    def __lt__(self, other):
        other_m = other.m if type(other) == 'Body' else other
        return self.m < other_m

    def __le__(self, other):
        other_m = other.m if type(other) == 'Body' else other
        return self.m <= other_m

    def __gt__(self, other):
        other_m = other.m if type(other) == 'Body' else other
        return self.m > other_m

    def __ge__(self, other):
        other_m = other.m if type(other) == 'Body' else other
        return self.m >= other_m

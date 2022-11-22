class Thing:
    def __init__(self, name: str, weight: (int, float)):
        self.name = name if type(name) == str else None
        self.weight = weight if type(weight) in (int, float) else None


class Bag:
    def __init__(self, max_weight):
        self.max_weight = max_weight
        self.total_weight = max_weight
        self.things = []

    def add_thing(self, thing):
        if self.total_weight - thing.weight >= 0:
            self.things.append(thing)
            self.total_weight -= thing.weight
        else:
            raise ValueError('превышен суммарный вес предметов')

    def __getitem__(self, indx):
        try:
            return self.things[indx]
        except IndexError:
            raise IndexError('неверный индекс')

    def __setitem__(self, key, value):
        self.total_weight += self.things[key].weight
        if self.total_weight - value.weight >= 0:
            self.things[key] = value
            self.total_weight -= value.weight
        else:
            raise ValueError('превышен суммарный вес предметов')

    def __delitem__(self, key):
        try:
            self.total_weight += self.things[key].weight
            del self.things[key]
        except IndexError:
            raise IndexError('неверный индекс')

class Bag:
    def __init__(self, max_weight):
        self.max_weight = max_weight
        self.__things = []
        self.current_weight = 0

    @property
    def things(self):
        return self.__things

    def add_thing(self, thing):
        if self.max_weight > 0 and self.max_weight > thing.weight:
            self.__things.append(thing)
            self.max_weight -= thing.weight

    def remove_thing(self, indx):
        item = self.__things.pop(indx)
        self.max_weight += item.weight

    def get_total_weight(self):
        total_weight = 0
        for item in self.__things:
            total_weight += item.weight
        return total_weight


class Thing:
    def __init__(self, name, weight):
        self.name = name
        self.weight = weight

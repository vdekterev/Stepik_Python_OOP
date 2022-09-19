import time


class GeyserClassic:
    MAX_DATE_FILTER = 100
    slots = [None, None, None]

    def add_filter(self, slot_num, filter):
        types = {1: 'Mechanical', 2: 'Aragon', 3: 'Calcium'}
        if types[slot_num] == filter.type and self.slots[slot_num-1] is None:
            self.slots[slot_num-1] = filter

    def remove_filter(self, slot_num):
        self.slots[slot_num-1] = None

    def get_filters(self):
        return [s for s in self.slots if s is not None]

    def water_on(self):
        if None in self.slots:
            return False
        for filt in self.slots:
            if not 0 <= (time.time() - filt.date) <= self.MAX_DATE_FILTER:
                return False
        return True


class Mechanical:
    type = 'Mechanical'

    def __init__(self, date):
        self.date = date

    def __setattr__(self, key, value):
        if key == 'date' and key in self.__dict__:
            return
        object.__setattr__(self, key, value)


class Aragon:
    type = 'Aragon'

    def __init__(self, date):
        self.date = date

    def __setattr__(self, key, value):
        if key == 'date' and key in self.__dict__:
            return
        object.__setattr__(self, key, value)


class Calcium:
    type = 'Calcium'

    def __init__(self, date):
        self.date = date

    def __setattr__(self, key, value):
        if key == 'date' and key in self.__dict__:
            return
        object.__setattr__(self, key, value)

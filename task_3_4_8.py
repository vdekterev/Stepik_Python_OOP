class Item:
    def __init__(self, name: str, money: (int, float)):
        self.name = self.money = None
        if type(name) == str:
            self.name = name
        if type(money) in (int, float):
            self.money = money

    def __add__(self, other):
        return self.money + other.money

    def __iadd__(self, other):
        return self.__add__(other)

    def __radd__(self, other):
        return self.money + other


class Budget:
    def __init__(self):
        self.items = []

    def add_item(self, it):
        self.items.append(it)

    def remove_item(self, indx):
        self.items.pop(indx)

    def get_items(self):
        return self.items

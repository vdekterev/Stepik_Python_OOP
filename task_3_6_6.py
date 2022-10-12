import sys

class ShopItem:

    def __init__(self, name, weight, price):
        self.name = name
        self.weight = weight
        self.price = price

    def __hash__(self):
        return hash((self.name.lower(), self.weight, self.price))

    def __eq__(self, other):
        return hash(self) == hash(other)

# считывание списка из входного потока
lst_in = list(map(str.strip, sys.stdin.readlines()))  # список lst_in в программе не менять!


items = [ShopItem(l.split(':')[0], l.split(':')[1].split()[0], l.split(':')[1].split()[1])
         for l in lst_in]

shop_items = {item.name: [item, items.count(item)] for item in items}
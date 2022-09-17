class Shop:
    def __init__(self, shop_name):
        self.shop_name = shop_name
        self.goods = []

    def add_product(self, product):
        self.goods.append(product)

    def remove_product(self, product):
        self.goods.remove(product)


class Product:
    id = 0

    def __new__(cls, *args, **kwargs):
        cls.id += 1
        return super().__new__(cls)

    def __init__(self, name: str, weight: int, price: int):
        self.name = name
        self.weight = weight
        self.price = price
        self.id = self.id

    def __setattr__(self, key, value):
        if (key == 'name' and type(value) != str) or (key in ('weight', 'price') and type(value) != int)\
                    or (key in ('weight', 'price') and value < 0):
            raise TypeError("Неверный тип присваиваемых данных.")
        object.__setattr__(self, key, value)

    def __delattr__(self, item):
        if item == 'id':
            raise AttributeError('Атрибут id удалять запрещено.')
        object.__delattr__(self, item)


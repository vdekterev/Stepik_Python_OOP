class Box:
    def __init__(self):
        self.__objects = []

    def add_thing(self, obj):
        self.__objects.append(obj)

    def get_things(self):
        return self.__objects

    def __eq__(self, other):
        lst_self = [(obj.name, obj.mass) for obj in self.__objects]
        lst_other = [(obj.name, obj.mass) for obj in other.__objects]
        return sorted(lst_self) == sorted(lst_other)


class Thing:
    def __init__(self, name, mass):
        self.name = name if type(name) == str else 'missing name'
        self.mass = mass if type(mass) in (int, float) else 0

    def __eq__(self, other):
        return self.name.lower() == other.name.lower() and self.mass == other.mass

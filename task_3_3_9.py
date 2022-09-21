class Ingredient:
    def __init__(self, name: str, volume: int, measure: str):
        self.name = self.volume = self.measure = 'missing parameter'
        if type(name) == str:
            self.name = name
        if type(volume) == int:
            self.volume = volume
        if type(measure) == str:
            self.measure = measure

    def __str__(self):
        return f'{self.name}: {self.volume}, {self.measure}'


class Recipe:
    def __init__(self, *ings):
        self.__ings = list(ings)

    def add_ingredient(self, ing):
        if isinstance(ing, Ingredient):
            self.__ings.append(ing)

    def remove_ingredient(self, ing):
        self.__ings.remove(ing)

    def get_ingredients(self):
        return tuple(ing for ing in self.__ings)

    def __len__(self):
        return len(self.__ings)

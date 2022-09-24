class Book:
    def __init__(self, title: str, author: str, year: int):
        self.title = self.author = self.year = None
        if type(title) == str:
            self.title = title
        if type(author) == str:
            self.author = author
        if type(year) == int:
            self.year = year


class Lib:
    def __init__(self):
        self.book_list = []

    def __len__(self):
        return len(self.book_list)

    def __add__(self, other):
        self.book_list.append(other)
        return self

    def __iadd__(self, other):
        return self.__add__(other)

    def __sub__(self, other):
        if type(other) == Book:
            self.book_list.remove(other)
        elif type(other) == int:
            self.book_list.pop(other)
        return self

    def __isub__(self, other):
        return self.__sub__(other)

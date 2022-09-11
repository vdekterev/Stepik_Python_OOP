class Book:
    def __init__(self, author: str, title: str, price: str):
        self.__author = author
        self.__title = title
        self.__price = price

    def set_title(self, title: str):
        if type(title) == str:
            self.__title = title

    def set_author(self, author: str):
        if type(author) == str:
            self.__author = author

    def set_price(self, price: int):
        if type(price) == int:
            self.__price = price

    def get_title(self):
        return self.__title

    def get_author(self):
        return self.__author

    def get_price(self):
        return self.__price



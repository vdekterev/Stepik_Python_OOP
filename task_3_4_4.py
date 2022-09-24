class NewList:
    def __init__(self, lst=None):
        self.__list = lst[:] if lst and type(lst) == list else []

    def get_list(self):
        return self.__list

    def __sub__(self, other):
        if type(other) not in (list, NewList):
            raise ArithmeticError('type other not in (list, NewList)')
        sc = other if type(other) == list else other.get_list()
        return NewList(self.__substract(self.__list, sc))

    def __rsub__(self, other):
        if type(other) != list:
            raise ArithmeticError('incorrect operand (must be a list)')
        return NewList(self.__substract(other, self.__list))

    @staticmethod
    def __substract(lst_1, lst_2):
        if len(lst_2) == 0:
            return lst_1
        sub = lst_2[:]

        return [x for x in lst_1 if not NewList.__is_elem(x, sub)]

    @staticmethod
    def __is_elem(x, sub):
        res = any(map(lambda xx: type(x) == type(xx) and x == xx, sub))
        if res:
            sub.remove(x)
        return res

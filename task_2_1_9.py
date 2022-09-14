class LinkedList:
    def __init__(self):
        self.head = self.tail = None

    def add_obj(self, data):     # добавляет ОБЪЕКТ класса ObjList(data)
        if self.head is None:
            new_obj = ObjList(data)
            self.head = self.tail = new_obj
        n = self.tail
        while n.get_next() is not None:
            n = self.tail

    def remove_obj(self):
        self.tail = self.tail.__prev

    def get_data(self):
        return self.__data


class ObjList:

    def __init__(self, data):
        self.__next = None
        self.__prev = None
        self.__data = data

    def set_next(self, obj):
        self.__next = obj

    def set_prev(self, obj):
        self.__prev = obj

    def get_next(self):
        return self.__next

    def get_prev(self):
        return self.__prev

    def set_data(self, data):
        self.__data = data

    def get_data(self):
        return self.__data


lst = LinkedList()
lst.add_obj(ObjList('1'))
lst.add_obj(ObjList('2'))
lst.add_obj(ObjList('3'))

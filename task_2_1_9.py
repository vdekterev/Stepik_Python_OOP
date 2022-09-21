class LinkedList:
    """объявите класс LinkedList, который будет представлять связный список в целом
    и иметь набор следующих методов:
    И локальные публичные атрибуты:
    head - ссылка на первый объект связного списка (если список пустой, то head = None);
    tail - ссылка на последний объект связного списка (если список пустой, то tail = None).
    """

    def __init__(self):
        self.head = self.tail = None

    def add_obj(self, obj):
        """добавление нового объекта obj класса ObjList в конец связного списка;
        """
        if self.head is None:
            new_object = obj
            self.head = new_object
            self.tail = new_object
        else:
            n = self.head
            while n.get_next() is not None:
                n = n.get_next()
            new_object = obj
            self.tail = new_object
            n.set_next(new_object)
            new_object.set_prev(n)

    def remove_obj(self):
        """удаление последнего объекта из связного списка;
        """
        if self.head is None:
            return []
        elif self.head.get_next() is None:
            self.head = None
        else:
            n = self.head
            while n.get_next() is not None:
                n = n.get_next()
            n.get_prev().set_next(None)

    def get_data(self):
        """получение списка из строк локального свойства __data всех объектов связного списка.
        """
        if self.head is None:
            return []
        else:
            n = self.head
            res = []
            while n is not None:
                res.append(n.get_data())
                n = n.get_next()
            return res


class ObjList:
    """Объекты класса ObjList должны иметь следующий набор приватных локальных свойств:
    __next - ссылка на следующий объект связного списка (если следующего объекта нет, то __next = None);
    __prev - ссылка на предыдущий объект связного списка (если предыдущего объекта нет, то __prev = None);
    __data - строка с данными.
    Также в классе ObjList должны быть реализованы следующие сеттеры и геттеры:
    """

    def __init__(self, data):
        self.__next = self.__prev = None
        self.__data = data

    def set_next(self, obj):
        """изменение приватного свойства __next на значение obj;
        """
        self.__next = obj

    def set_prev(self, obj):
        """изменение приватного свойства __prev на значение obj;
        """
        self.__prev = obj

    def get_next(self):
        """получение значения приватного свойства __next;
        """
        return self.__next

    def get_prev(self):
        """получение значения приватного свойства __prev;
        """
        return self.__prev

    def set_data(self, data):
        """изменение приватного свойства __data на значение data;
        """
        self.__data = data

    def get_data(self):
        """получение значения приватного свойства __data.
        """
        return self.__data
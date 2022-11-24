class StackObj:
    def __init__(self, data):
        self.data = data
        self.__next = None

    @property
    def next(self):
        return self.__next

    @next.setter
    def next(self, obj):
        self.__next = obj


class Stack:
    def __init__(self):
        self.top = None
        self.counter = 0

    def push(self, obj):
        if self.top is None:
            self.top = obj
            self.counter += 1
        else:
            n = self.top
            while n.next is not None:
                n = n.next
            n.next = obj
            self.counter += 1

    def pop(self):
        if self.top is None:
            return
        elif self.top.next is None:
            r = self.top
            self.top = None
            self.counter -= 1
            return r
        else:
            n = self.top
            while n.next.next is not None:
                n = n.next
            pop = n.next
            n.next = None
            self.counter -= 1
            return pop

    def __len__(self):
        return self.counter - 1

    def __check_index(self, index):
        if type(index) != int or not 0 <= index <= self.__len__():
            raise IndexError('неверный индекс')

    def __getitem__(self, item):
        self.__check_index(item)
        if item == 0:
            return self.top
        n = self.top
        for _ in range(item):
            n = n.next
        return n

    def __setitem__(self, key, value):
        self.__check_index(key)
        if type(value) != StackObj:
            raise ValueError('Объект должен быть типа StackObj')
        if key == 0:
            self.top = value
            return
        n = self.top
        for _ in range(key-1):
            n = n.next
        obj = n.next.next
        n.next = value
        value.next = obj

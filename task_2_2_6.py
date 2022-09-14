class StackObj:
    def __init__(self, data):
        self.__data = data
        self.__next = None

    @property
    def next(self):
        return self.__next

    @next.setter
    def next(self, next):
        self.__next = next

    @property
    def data(self):
        return self.__data

    @data.setter
    def data(self, data):
        self.__data = data


class Stack:
    def __init__(self):
        self.top = None

    def push(self, obj):
        if self.top is None:
            self.top = obj
        else:
            new_object = StackObj(obj.data)
            n = self.top
            while n.next is not None:
                n = n.next
            n.next = new_object

    def get_data(self):
        if self.top is None:
            return []
        else:
            n = self.top
            res = []
            while n is not None:
                res.append(n.data)
                n = n.next
            return res

    def pop(self):
        if self.top is None:
            return []
        elif self.top.next is None:
            r = self.top
            self.top = None
            return r
        else:
            n = self.top
            while n.next.next is not None:
                n = n.next
            pop = n.next
            n.next = None
            return pop

class Stack:
    def __init__(self):
        self.top = None

    def push_back(self, obj):
        if self.top is None:
            self.top = obj
        else:
            n = self.top
            while n.next is not None:
                n = n.next
            n.next = obj

    def pop_back(self):
        if self.top is None:
            return []
        elif self.top.next is None:
            r = self.top
            self.top = None
            return self.top
        else:
            n = self.top
            while n.next.next is not None:
                n = n.next
            pop = n.next
            n.next = None
            return pop

    def __add__(self, other):
        self.push_back(other)
        return self

    def __iadd__(self, other):
        return self.__add__(other)

    def __mul__(self, other: list):
        for l in other:
            self.push_back(StackObj(l))
        return self

    def __imul__(self, other):
        return self.__mul__(other)


class StackObj:
    def __init__(self, data):
        self.__data = data
        self.__next = None

    @property
    def next(self):
        return self.__next

    @next.setter
    def next(self, obj):
        self.__next = obj

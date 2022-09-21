class Descriptor:
    def __set_name__(self, owner, name):
        self.name = f"_{owner.__name__}__{name}"

    def __set__(self, instance, value):
        instance.__dict__[self.name] = value

    def __get__(self, instance, owner):
        return instance.__dict__[self.name]


class ObjList:
    next = Descriptor()
    prev = Descriptor()
    data = Descriptor()

    def __init__(self, data):
        self.__data = data
        self.__next = self.__prev = None


class LinkedList:
    def __init__(self):
        self.head = self.tail = None

    def add_obj(self, obj):
        if self.head is None:
            new_object = obj
            self.head = self.tail = new_object
        else:
            n = self.head
            while n.next is not None:
                n = n.next
            new_object = obj
            self.tail = new_object
            n.next = new_object
            new_object.prev = n

    def remove_obj(self, indx):
        if self.__len__() == 1:
            self.head = self.tail = None
        if self.head is None:
            return
        if indx == 0:
            self.head = self.head.next
        elif indx + 1 == self.__len__():
            self.tail = self.tail.prev
        try:
            n = self.head
            finder = 0
            while finder != indx:
                n = n.next
                finder += 1
            n.prev.next = n.next
        except AttributeError:
            return 'remove_obj.error: No such index'

    def __len__(self):
        if self.head is None:
            return 0
        n = self.head
        counter = 1
        while n.next is not None:
            n = n.next
            counter += 1
        return counter

    def __call__(self, indx, *args, **kwargs):
        if self.head is None:
            return
        elif indx == 0:
            return self.head.data
        try:
            n = self.head
            finder = 0
            while finder != indx:
                n = n.next
                finder += 1
            return n.data
        except AttributeError:
            return 'linked_lst.error: No such index'

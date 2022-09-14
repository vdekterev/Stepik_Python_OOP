class TreeObj:
    def __init__(self, indx, value=None):
        self.indx = indx
        self.value = value
        self.__left = self.__right = None

    @property
    def left(self):
        return self.__left

    @left.setter
    def left(self, left):
        self.__left = left

    @property
    def right(self):
        return self.__right

    @right.setter
    def right(self, right):
        self.__right = right


class DecisionTree:
    root_object = None

    @classmethod
    def predict(cls, root, x):  # x = [1, 1, 0] or [0, 1, 1]
        root = cls.root_object
        if x[0] == 1:
            root = root.left
            root = root.left if x[1] == 1 else root.right
        elif x[0] == 0:
            root = root.right
            root = root.left if x[2] == 1 else root.right
        return root.value

    @classmethod
    def add_obj(cls, obj, node=None, left=True):
        if node is None:
            cls.root_object = obj
        new_object = obj
        if node is not None:
            if left:
                node.left = new_object
                return node.left
            else:
                node.right = new_object
                return node.right
        return new_object

class TriangleListIterator:
    def __init__(self, lst):
        self.lst = lst
        self.value = 0

    def __iter__(self):
        for i in range(len(self.lst)):
            for j in range(i+1):
                yield self.lst[i][j]

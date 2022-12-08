class IterColumn:
    def __init__(self, lst: list, column: int):
        self.lst = lst
        self.column = column

    def __iter__(self):
        for row in self.lst:
            yield row[self.column]

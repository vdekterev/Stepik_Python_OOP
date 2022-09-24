class MaxPooling:
    def __init__(self, step=(2, 2), size=(2, 2)):
        self.step = step
        self.size = size

    def __call__(self, matrix, *args, **kwargs):
        if not all(map(lambda x: len(x) == len(matrix) and all(map(lambda y: type(y) in (int, float), x)), matrix)):
            raise ValueError("Неверный формат для первого параметра matrix.")
        return self.validate_matrix(matrix)

    def validate_matrix(self, matrix):
        lst = []
        count = len(matrix) // self.step[0]
        stop = 0
        for i in range(0, len(matrix), self.step[0]):
            if count == stop:
                break
            for j in range(0, len(matrix[i]), self.step[0]):
                b = matrix[i][j:j+self.size[0]]
                if len(b) == self.size[0]:
                    lst.append(b)
                c = matrix[i+1][j:j+self.size[0]]
                if len(c) == self.size[0]:
                    lst[-1].extend(c)
            stop += 1
        res = list(map(lambda x: max(x), lst))
        return [res[i:i+self.step[0]] for i in range(0, len(lst), self.step[0])]

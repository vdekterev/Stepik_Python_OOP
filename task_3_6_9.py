s_inp = input()


class Dimensions:
    def __init__(self, a, b, c):
        try:
            self.a = self.number_validator(a) if self.number_validator(a) > 0 else None
            self.b = self.number_validator(b) if self.number_validator(b) > 0 else None
            self.c = self.number_validator(c) if self.number_validator(c) > 0 else None
        except ValueError:
            raise ValueError("габаритные размеры должны быть положительными числами")

    @staticmethod
    def number_validator(n):
        try:
            if int(n) > 0:
                return int(n)
            raise ValueError("габаритные размеры должны быть положительными числами")
        except ValueError:
            if float(n) > 0:
                return float(n)
            raise ValueError("габаритные размеры должны быть положительными числами")

    def __hash__(self):
        return hash((self.a, self.b, self.c))


lst_dims = []
for l in s_inp.split(';'):
    args = l.strip().split()
    lst_dims.append(Dimensions(*args))

lst_dims = sorted(lst_dims, key=hash)

class InputDigits:
    def __init__(self, func):
        self.__func = func

    def __call__(self, *args, **kwargs):
        return list(map(int, self.__func().split()))


input_dg = InputDigits(input)
res = input_dg()

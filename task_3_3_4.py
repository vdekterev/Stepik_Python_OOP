class WordString:
    def __init__(self, string=''):
        self.__string = string

    @property
    def string(self):
        return self.__string

    @string.setter
    def string(self, string):
        self.__string = string

    def __str__(self):
        return self.__string

    def words(self, indx):
        return self.string[indx]

    def __len__(self):
        return len(self.string.split())

    def __call__(self, a, *args, **kwargs):
        if len(self.string) == 0:
            return '0'
        return self.__string.split()[0]

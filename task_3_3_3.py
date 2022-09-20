class Model:
    def __init__(self, **kwargs):
        self.__model = kwargs

    def query(self, **kwargs):
        for k, v in kwargs.items():
            self.__model[k] = v
        return self.__model

    def __str__(self):
        if len(self.__model) == 0:
            return 'Model'
        return 'Model: ' + ", ".join([f'{key} = {value}' for key, value in self.__model.items()])

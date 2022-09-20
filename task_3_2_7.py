class HandlerGET:
    def __init__(self, func):
        self.__func = func

    def __call__(self, request, *args, **kwargs):
        return self.get(self.__func, request)

    def get(self, func, request, *args, **kwargs):
        if 'method' in request.keys() and request['method'] != 'GET':
            return
        return f'GET: {self.__func(request)}'


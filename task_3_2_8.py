class Handler:
    def __init__(self, methods=('GET',)):
        self.methods = methods

    def __call__(self, func):
        def wrapper(request, *args, **kwargs):
            if 'method' not in request.keys():
                request['method'] = self.methods[0]
            if request["method"] == 'GET' and 'GET' in self.methods:
                return self.get(func, request)
            elif request["method"] == 'POST':
                return self.post(func, request)
            else:
                return
        return wrapper

    def get(self, func, request, *args, **kwargs):
        return f'{request["method"]}: {func(request)}'

    def post(self, func, request, *args, **kwargs):
        return f'{request["method"]}: {func(request)}'

class ImageFileAcceptor:
    def __init__(self, extensions: tuple):
        self.extensions = extensions

    def __call__(self, filename, *args, **kwargs):
        if filename.split('.')[-1] in self.extensions:
            return filename

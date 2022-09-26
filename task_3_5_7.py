class FileAcceptor:
    def __init__(self, *extensions):
        self.extensions = [*extensions]

    def __call__(self, filename, *args, **kwargs):
        extension = filename.split('.')[1] if len(filename.split('.')) == 2 else filename.split('.')[-1]
        return extension in ' '.join(self.extensions)

    def __add__(self, other):
        self.extensions.extend([ex for ex in other.extensions if ex not in self.extensions])
        return FileAcceptor(*self.extensions)

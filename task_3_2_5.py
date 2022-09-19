class DigitRetrieve:
    def __call__(self, string, *args, **kwargs):
        try:
            return int(string)
        except:
            return

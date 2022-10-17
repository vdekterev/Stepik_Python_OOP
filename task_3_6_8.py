class BookStudy:
    def __init__(self, name: str, author: str, year: int):
        self.name = name if type(name) == str else 'NoName'
        self.author = author if type(author) == str else 'NoAuthor'
        self.year = year if type(year) == int else 'NoYear'

    def __hash__(self):
        return hash((self.name, self.author))


lst_in = [
    'Python; Балакирев С.М.; 2020',
    'Python ООП; Балакирев С.М.; 2021',
    'Python ООП; Балакирев С.М.; 2022',
    'Python; Балакирев С.М.; 2021',
]

lst_bs = []

for l in lst_in:
    args = list(map(str.strip, l.split(';')))
    args[-1] = int(args[-1])
    lst_bs.append(BookStudy(*args))

unique_books = len(set([hash(book) for book in lst_bs]))

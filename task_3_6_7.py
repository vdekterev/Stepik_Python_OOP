class DataBase:
    def __init__(self, path: str):
        self.path = path if type(path) == str else None
        self.dict_db = {}

    def write(self, record):
        self.dict_db.setdefault(record, [])
        self.dict_db[record].append(record)

    def read(self, pk):
        for rec in self.dict_db:
            if rec.pk == pk:
                return rec


class Record:
    pk = 0

    def __new__(cls, *args, **kwargs):
        cls.pk += 1
        return super().__new__(cls)

    def __init__(self, fio: str, descr: str, old: int):
        self.fio = fio if type(fio) == str else None
        self.descr = descr if type(descr) == str else None
        self.old = old if type(old) == int else None
        self.pk = Record.pk

    def __hash__(self):
        return hash((self.fio.lower(), self.old))

    def __eq__(self, other):
        return hash(self) == hash(other)


lst_in = ['Балакирев С.М.; программист; 33',
          'Кузнецов Н.И.; разведчик-нелегал; 35',
          'Суворов А.В.; полководец; 42',
          'Иванов И.И.; фигурант всех подобных списков; 26',
          'Балакирев С.М.; преподаватель; 33'
          ]


db = DataBase('mydb')
for l in lst_in:
    args = list(map(str.strip, l.split(';')))
    args[-1] = int(args[-1])
    db.write(Record(*args))

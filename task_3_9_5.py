class Person:
    indx = {0: 'fio', 1: 'job', 2: 'old', 3: 'salary', 4: 'year_job'}

    def __init__(self, fio, job, old, salary, year_job):
        self.fio = fio
        self.job = job
        self.old = old
        self.salary = salary
        self.year_job = year_job
        self.data = [self.fio, self.job, self.old, self.salary, self.year_job]
        self.value = 0

    def __getitem__(self, item):
        return self.data[item]

    def __setitem__(self, key, value):
        if type(key) != int or not 0 <= key <= 4:
            raise IndexError('неверный индекс')
        self.data[key] = value
        self.__setattr__(Person.indx[key], value)

    def __next__(self):
        if 0 <= self.value <= 4:
            val = self.data[self.value]
            self.value += 1
            return val
        else:
            raise StopIteration

    def __iter__(self):
        return self

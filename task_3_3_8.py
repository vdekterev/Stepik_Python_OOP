class Clock:
    def __init__(self, hrs, mins, sec):
        self.sec = self.hrs = self.mins = 0
        if self.time_validator(sec):
            self.sec = sec
        if self.time_validator(hrs):
            self.hrs = hrs
        if self.time_validator(mins):
            self.mins = mins

    @staticmethod
    def time_validator(value):
        if type(value) == int and value >= 0:
            return value

    def get_time(self):
        return self.sec + self.mins * 60 + self.hrs * 3600


class DeltaClock:
    def __init__(self, clock1, clock2):
        self.__clock1 = clock1
        self.__clock2 = clock2

    def __str__(self):
        if self.__clock1.get_time() <= self.__clock2.get_time():
            return '00: 00: 00'
        hrs = self.add_zero(str(self.__clock1.hrs - self.__clock2.hrs))
        mins = self.add_zero(str((self.__clock1.mins - self.__clock2.mins)\
            if self.__clock1.mins >= self.__clock2.mins else 60 - (self.__clock2.mins - self.__clock1.mins)))
        sec = self.add_zero(str((self.__clock1.sec - self.__clock2.sec)\
            if self.__clock1.sec >= self.__clock2.sec else 60 - (self.__clock2.sec - self.__clock1.sec)))
        return f'{hrs}: {mins}: {sec}'

    @staticmethod
    def add_zero(value):
        if int(value) < 10:
            return f'0{value}'
        return value

    def __len__(self):
        return self.__clock1.get_time() - self.__clock2.get_time()

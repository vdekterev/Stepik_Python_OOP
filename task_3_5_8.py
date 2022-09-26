class MoneyR:
    def __init__(self, volume=0.0):
        self.__cb = None
        self.__volume = volume

    @property
    def volume(self):
        return self.__volume

    @volume.setter
    def volume(self, volume):
        self.__volume = volume

    @property
    def cb(self):
        return self.__cb

    @cb.setter
    def cb(self, cb):
        self.__cb = cb

    def __lt__(self, other):
        if self.cb is not None and other.cb is not None:
            converted_money = other.volume * CentralBank.rates['rub']
            return self.volume < converted_money
        raise ValueError("Неизвестен курс валют.")

    def __le__(self, other):
        if self.cb is not None and other.cb is not None:
            converted_money = other.volume * CentralBank.rates['rub']
            return self.volume <= converted_money
        raise ValueError("Неизвестен курс валют.")

    def __eq__(self, other):
        if self.cb is not None and other.cb is not None:
            converted_money = other.volume * CentralBank.rates['rub']
            return bool(int(self.volume*CentralBank.rates['rub']*10 in range(int(converted_money * 10) - 1,
                                                                             int(converted_money * 10) + 1)))

        raise ValueError("Неизвестен курс валют.")


class MoneyD:
    def __init__(self, volume=0.0):
        self.__cb = None
        self.__volume = volume

    @property
    def volume(self):
        return self.__volume

    @volume.setter
    def volume(self, volume):
        self.__volume = volume

    @property
    def cb(self):
        return self.__cb

    @cb.setter
    def cb(self, cb):
        self.__cb = cb

    def __lt__(self, other):
        if self.cb is not None and other.cb is not None:
            converted_money = other.volume * CentralBank.rates['rub']
            return self.volume < converted_money
        raise ValueError("Неизвестен курс валют.")

    def __le__(self, other):
        if self.cb is not None and other.cb is not None:
            converted_money = other.volume * CentralBank.rates['rub']
            return self.volume <= converted_money
        raise ValueError("Неизвестен курс валют.")

    def __eq__(self, other):
        if self.cb is not None and other.cb is not None:
            converted_money = other.volume * CentralBank.rates['rub']
            return bool(int(self.volume * CentralBank.rates['rub'] * 10 in range(int(converted_money * 10) - 1,
                                                                                 int(converted_money * 10) + 1)))
        raise ValueError("Неизвестен курс валют.")


class MoneyE:
    def __init__(self, volume=0.0):
        self.__cb = None
        self.__volume = volume

    @property
    def volume(self):
        return self.__volume

    @volume.setter
    def volume(self, volume):
        self.__volume = volume

    @property
    def cb(self):
        return self.__cb

    @cb.setter
    def cb(self, cb):
        self.__cb = cb

    def __lt__(self, other):
        if self.cb is not None and other.cb is not None:
            converted_money = other.volume * CentralBank.rates['rub']
            return self.volume < converted_money
        raise ValueError("Неизвестен курс валют.")

    def __le__(self, other):
        if self.cb is not None and other.cb is not None:
            converted_money = other.volume * CentralBank.rates['rub']
            return self.volume <= converted_money
        raise ValueError("Неизвестен курс валют.")

    def __eq__(self, other):
        if self.cb is not None and other.cb is not None:
            converted_money = other.volume * CentralBank.rates['rub']
            return bool(int(self.volume * CentralBank.rates['rub'] * 10 in range(int(converted_money * 10) - 1,
                                                                                 int(converted_money * 10) + 1)))
        raise ValueError("Неизвестен курс валют.")


class CentralBank:
    __instance = None
    rates = {'rub': 72.5, 'dollar': 1.0, 'euro': 1.15}

    def __new__(cls, *args, **kwargs):
        return

    @classmethod
    def register(cls, money):
        money.cb = cls.rates

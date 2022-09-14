class PhoneBook:
    phones = []

    @classmethod
    def add_phone(cls, phone):
        cls.phones.append(phone)

    @classmethod
    def remove_phone(cls, indx):
        cls.phones.pop(indx)

    @classmethod
    def get_phone_list(cls):
        return cls.phones


class PhoneNumber:
    def __init__(self, number: int, fio: str):
        self.number = number
        self.fio = fio


p = PhoneBook()
p.add_phone(PhoneNumber(89635460925, 'Dekterev'))
print(p.get_phone_list())

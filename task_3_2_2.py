from random import randint, choice # функция для генерации целых случайных значений в диапазоне [a; b]


class RandomPassword:
    def __init__(self, psw_chars, min_length, max_length):
        self.psw_chars = psw_chars
        self.min_length = min_length
        self.max_length = max_length

    def __call__(self, *args, **kwargs):
        password = ''.join([choice(self.psw_chars) for _ in range(randint(self.min_length, self.max_length))])
        return password


rnd = RandomPassword("qwertyuiopasdfghjklzxcvbnm0123456789!@#$%&*", 5, 20)
psw = rnd()
lst_pass = [rnd() for _ in range(3)]

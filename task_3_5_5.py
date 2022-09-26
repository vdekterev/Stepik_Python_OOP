class StringText:
    def __init__(self, lst_words):
        self.lst_words = lst_words

    def __len__(self):
        return len(self.lst_words)

    def __eq__(self, other):
        return len(self) == len(other)

    def __lt__(self, other):
        return len(self) < len(other)

    def __le__(self, other):
        return len(self) <= len(other)


stich = ["Я к вам пишу – чего же боле?",
        "Что я могу еще сказать?",
        "Теперь, я знаю, в вашей воле",
        "Меня презреньем наказать.",
        "Но вы, к моей несчастной доле",
        "Хоть каплю жалости храня,",
        "Вы не оставите меня."]
poetry = [s.strip('–?!,.; ').split() for s in stich]

lst_text = [StringText(st) for st in poetry]
lst_text_sorted = [' '.join(x.lst_words) for x in sorted(lst_text, key=lambda x: len(x), reverse=True)]

class Morph:
    def __init__(self, *words):
        self.words = [*words]

    def add_word(self, word):
        if word not in self.words:
            self.words.append(word)

    def get_words(self):
        return tuple(self.words)

    def __eq__(self, other):
        if type(self) == Morph:
            return other.lower() in self.words
        return self.lower() in other.words

    def __ne__(self, other):
        return not self.__eq__(other)


dict_words = [Morph('связь', 'связи', 'связью', 'связи', 'связей', 'связям', 'связями', 'связях'),
                  Morph('формула', 'формулы', 'формуле', 'формулу', 'формулой', 'формул', 'формулам', 'формулами',
                        'формулах'),
                  Morph('вектор', 'вектора', 'вектору', 'вектором', 'векторе', 'векторы', 'векторов', 'векторам',
                        'векторами', 'векторах'
                        ),
                  Morph('эффект', 'эффекта', 'эффекту', 'эффектом', 'эффекте', 'эффекты', 'эффектов', 'эффектам',
                        'эффектами', 'эффектах'
                        ), Morph('день', 'дня', 'дню', 'днем', 'дне', 'дни', 'дням', 'днями', 'днях'
                                 )]


text = input()


words = map(lambda x: x.strip('?!:;.,').lower(), text.split())
print(sum(word == morph for word in words for morph in dict_words))

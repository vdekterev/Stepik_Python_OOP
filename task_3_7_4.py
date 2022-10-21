class Player:
    def __init__(self, name, old, score):
        self.name = name if type(name) == str else 'NoName'
        self.old = int(old)
        self.score = int(score)

    def __bool__(self):
        return bool(self.score)


players = [Player(*p.split(';')) for p in lst_in]
players_filtered = list(filter(bool, players))

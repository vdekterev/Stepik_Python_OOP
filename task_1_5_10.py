class Cell:
    def __init__(self, mine=False, around_mines=0):
        self.around_mines = around_mines
        self.mine = mine
        self.fl_open = True


class GamePole:
    def __init__(self, N: int, M: int):
        self._n = N
        self._m = M
        self.pole = [[Cell() for _ in range(self._n)] for _ in range(self._n)]
        self.init()

    def init(self):
        m = 0
        import random
        while m < self._m:
            i = random.randint(0, self._n - 1)
            j = random.randint(0, self._n - 1)
            if self.pole[i][j].mine:
                continue
            self.pole[i][j].mine = True
            m += 1

        indicies = (-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)
        for x in range(self._n):
            for y in range(self._n):
                if self.pole[x][y]:
                    mines_count = sum((self.pole[i+x][j+y].mine for i, j in indicies if 0 <= i+x < self._n and 0 <= y+j < self._n))
                    self.pole[x][y].around_mines = mines_count

    def show(self):
        for row in self.pole:
            print(*map(lambda x: '#' if not x.fl_open else x.around_mines if not x.mine else '*', row))


pole_game = GamePole(10, 12)
pole_game.init()
pole_game.show()

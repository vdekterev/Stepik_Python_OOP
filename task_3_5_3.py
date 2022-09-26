class Track:
    def __init__(self, start_x=0, start_y=0):
        if type(start_x) in (int, float):
            self.start_x = start_x
        if type(start_y) in (int, float):
            self.start_y = start_y
        self.tracks = []

    def add_track(self, tr):
        if type(tr) == TrackLine:
            self.tracks.append(tr)

    def get_tracks(self):
        return tuple(self.tracks)

    def __eq__(self, other):
        return len(self) == len(other)

    def __lt__(self, other):
        return len(self) < len(other)

    def __ne__(self, other):
        return len(self) != len(other)

    def __len__(self):
        x1, y1 = self.start_x, self.start_y
        distance = 0
        for el in self.tracks:
            x2, y2 = el.to_x, el.to_y
            distance += ((x1 - x2) ** 2 + (y1 - y2) ** 2) ** 0.5
            x1, y1 = x2, y2
        return int(distance)


class TrackLine:
    def __init__(self, to_x, to_y, max_speed):
        self.__to_x = self.__to_y = self.__max_speed = None
        if type(to_x) in (int, float):
            self.__to_x = to_x
        if type(to_x) in (int, float):
            self.__to_y = to_y
        if type(max_speed) == int:
            self.__max_speed = max_speed

    @property
    def to_x(self):
        return self.__to_x

    @to_x.setter
    def to_x(self, x):
        self.__to_x = x

    @property
    def to_y(self):
        return self.__to_y

    @to_y.setter
    def to_y(self, y):
        self.__to_y = y


track1, track2 = Track(), Track(0, 1)
track1.add_track(TrackLine(2, 4, 100))
track1.add_track(TrackLine(5, -4, 100))
track2.add_track(TrackLine(3, 2, 90))
track2.add_track(TrackLine(10, 8, 90))
res_eq = track1 == track2

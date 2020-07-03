class Road:
    def __init__(self, length, width):
        self._length = length
        self._width = width

    def mass(self):
        weigth_1sm = 25
        thikness = 5
        weight = self._length * self._width * (weigth_1sm / 1000) * thikness
        print(f'{self._length}м * {self._width}м * {weigth_1sm}кг * {thikness}см = {weight}т')


road_1 = Road(205, 6)
road_1.mass()
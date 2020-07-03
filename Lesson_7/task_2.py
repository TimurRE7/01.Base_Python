from abc import ABC, abstractmethod


class Dress(ABC):
    def __init__(self, param):
        self.param = param

    @abstractmethod
    def consumption(self):
        pass


class Coat(Dress):
    def consumption(self):
        result = (self.param / 6.5 + 0.5)
        return result

    @property
    def v(self):
        return self.consumption()


class Costume(Dress):
    def consumption(self):
        result = (2 * self.param + 0.3)
        return result

    @property
    def h(self):
        return self.consumption()


coat = Coat(5)
costume = Costume(20)
print(coat.v)
print(costume.h)

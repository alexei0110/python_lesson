from abc import ABC, abstractmethod


class Clothes(ABC):

    def __init__(self, param):
        self.param = param

    @property
    @abstractmethod
    def expense(self):
        pass

    def __add__(self, other):
        return self.expense + other.expense


class Coat(Clothes):

    @property
    def expense(self):
        return self.param / 6.5 + 0.5


class Suit(Clothes):

    @property
    def expense(self):
        return self.param * 2 + 0.3


a = Coat(52)
b = Suit(1.80)
print(a.expense)
print(b.expense)
print(a + b)

# Kalkulator objętości
# Stwórz - z wykorzystaniem klas i dziedziczenia - kalkulator objętości brył:
# sześcianu, prostopadłościanu, stożka i walca.

from math import pi


class Prostopadloscian:
    def __init__(self, a, b, c):
        self.c = c
        self.b = b
        self.a = a

    def objetosc(self):
        v = self.a * self.b * self.c
        return v


class Szescian(Prostopadloscian):
    def __init__(self, a):
        super(Szescian, self).__init__(a, a, a)


class Walec:
    def __init__(self, r, h):
        self.h = h
        self.r = r

    def objetosc(self):
        v = pi * self.r * self.r * self.h
        return v


class Stozek(Walec):
    def objetosc(self):
        return super().objetosc()*(1/3)


abc = Prostopadloscian(2, 3, 2)
print(abc.objetosc())

aaa = Szescian(3)
print(aaa.objetosc())

w = Walec(1, 1)
print(w.objetosc())

s = Stozek(1, 1)
print(s.objetosc())



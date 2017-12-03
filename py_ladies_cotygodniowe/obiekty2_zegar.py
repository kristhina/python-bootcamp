import builtins
from unittest import TestCase


class Czas:
    def __init__(self, godziny = 19, minuty = 17, sekundy = 30):
        self.g = godziny
        self.m = minuty
        self.s = sekundy

    def __str__(self):
        return("g = {}, m = {}, s = {}".format(self.g, self.m, self.s))

    def set_time(self, nowe_godziny = None, nowe_minuty= None, nowe_sekundy = None):
        if nowe_godziny:
            self.g = nowe_godziny
        if nowe_minuty:
            self.m = nowe_minuty
        if nowe_sekundy:
            self.s = nowe_sekundy
        # self.s = nowe_sekundy or self.s
        # to był trochę inny sposób

    def add_time(self, g = None, m = None, s = None):
        # zgodnie z poleceniem zakładam, że godziny można dodawać w nieskończoność
        if g:
            self.g += g
        if m:
            self.m += m
            if self.m >= 60:
                mtg = self.m // 60
                self.g += mtg
                self.m -= mtg*60
        if s:
            self.s += s
            if self.s >= 60:
                stm = self.s // 60
                self.m += stm
                self.s -= stm*60
                if self.m >= 60:
                    mtg = self.m // 60
                    self.g += mtg
                    self.m -= mtg*60


    def get_seconds(self):
        total_seconds = self.s + self.m*60 + self.g*3600
        return total_seconds

    def get_minutes(self):
        total_minutes = self.s/60 + self.m + self.g * 60
        return total_minutes

    def get_hours(self):
        total_hours = self.s/3600 + self.m/60 + self.g
        return total_hours


class Zegar(Czas):
    def __init__(self, format, **kwargs):
        super().__init__(**kwargs)
        self.format = format

    def __str__(self):
        return super().__str__() + " format = {}".format(self.format)

class DokladnyZegar(Zegar):
    def __init__(self, *args, milisekundy = 0, **kwargs):
        super().__init__(*args, **kwargs)
        self.ms = milisekundy
        # kolejność: argumenty pozycyjne potem *args, argumenty nazwane a potem **kwargs

    def __str__(self):
        return super().__str__() + " ms = {}".format(self.ms)

    def set_time(self, ms  = None, **kwargs):
        super().set_time(**kwargs)
        if ms:
            self.ms = ms

    def add_time(self, ms=None, **kwargs):
        super().add_time(**kwargs)
        if ms:
            self.ms += ms
            if self.ms >= 1000:
                msts = self.ms // 1000
                self.s += msts
                self.ms -= msts*1000
                if self.s >= 60:
                    stm = self.s // 60
                    self.m += stm
                    self.s -= stm * 60
                    if self.m >= 60:
                        mtg = self.m // 60
                        self.g += mtg
                        self.m -= mtg * 60


def mojprint(text, liczba_wydrukow, prefix, **kwargs):
    for i in range(liczba_wydrukow):
        print(prefix + text)


def mojprint2(*args, ile_razy, prefix=None, **kwargs):
    for i in range(ile_razy):
        nowe = (prefix,) + args if prefix is not None else args
        print(*nowe, **kwargs)


mojprint2("as", "be", ile_razy=3, prefix="P", end="22222\n")
mojprint2("prefix", ile_razy=3)

# n_czas = Czas(0, 2, 45)
# print(n_czas.g)
# print(n_czas.m)
# print(n_czas.s)
# n_czas.add_time(s = 20)
# print(n_czas)
#
# zegar = Zegar(format = '24H', godziny = 12, minuty=34, sekundy=3)
# print(zegar.g)
# zegar.set_time(nowe_godziny=13)
# print(zegar.g)
#
# dz = DokladnyZegar(format = '12H', godziny = 20)
# print(dz.g)
# print(dz.format)
# print(dz.ms)
#
# print(n_czas)
# print(zegar)
# print(dz)
#
# dz.add_time(ms = 2345, g=17, m=29, s = 78)
# print(dz)
# dz.set_time(ms = 0, nowe_sekundy = 0, nowe_minuty = 10, nowe_godziny=10)
# print(dz)
# print(dz.get_seconds())
# print(dz.get_minutes())
# print(dz.get_hours())
#
# # def __str__(self):
# #     temp = "{} ".format(self._get_name())
# #     for atr in vars(self)
# #         if not atr.startswith('_'):
# #         temp += "{}={} ".format(atr, getattr(self, atr))
# #     return temp
# #
# # @classmethod
# # def _get_name(cls):
# #     return cls.__name__
#

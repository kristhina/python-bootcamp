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
        self.s = nowe_sekundy or self.s
        # to był trochę inny sposób

    def add_time(self, g = None, m = None, s = None):

        # lepiej zacząć od sekund
        # if g:
        #     self.g += g
        # if m:
        #     self.m += m
        #     if self.m >= 60:
        #         mtg = self.m // 60
        #         self.g += mtg
        #         self.m -= mtg*60
        # if s:
        #     self.s += s
        #     if self.s >= 60:
        #         stm = self.s // 60
        #         self.m += stm
        #         self.s -= stm*60
        #         if self.m >= 60:
        #             mtg = self.m // 60
        #             self.g += mtg
        #             self.m -= mtg*60
        #

    def get_seconds(self):
        pass

    def get_minutes(self):
        pass

    def get_hours(self):
        pass


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

    def set_time(selfself, ms  = None, **kwargs):
        super().set_time(**kwargs)
        if ms:
            self.ms = ms

def mojprint():
    pass

n_czas = Czas(0, 2, 45)
print(n_czas.g)
print(n_czas.m)
print(n_czas.s)
n_czas.add_time(s = 20)
print(n_czas)


print('-----')

zegar = Zegar(format = '24H', godziny = 12, minuty=34, sekundy=3)
print(zegar.g)
zegar.set_time(nowe_godziny=13)
print(zegar.g)

print('-----')

dz = DokladnyZegar(format = '12H', godziny = 20)
print(dz.g)
print(dz.format)
print(dz.ms)

print(n_czas)
print(zegar)
print(dz)

# def __str__(self):
#     temp = "{} ".format(self._get_name())
#     for atr in vars(self)
#         if not atr.startswith('_'):
#         temp += "{}={} ".format(atr, getattr(self, atr))
#     return temp
#
# @classmethod
# def _get_name(cls):
#     return cls.__name__
# Wykorzystując kod przygotowany do tego zadania, zamień klasy na namedtuple.

# class Ojciec:
#     def __init__(self, imie, nazwisko, data_ur):
#         self.imie = imie
#         self.nazwisko = nazwisko
#         self.data_ur = data_ur

from collections import namedtuple

Ojciec = namedtuple('Ojciec', ['imie', 'nazwisko', 'data_ur'])
o = Ojciec(imie="Jacek", nazwisko='Kowalski', data_ur='2018-23-01')
print(o)
print(o.imie)
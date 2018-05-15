# Na rozszerz generator z zad 6. tak, żeby zwracał instancję klasy lub namedtuple zwierającą
# dowcip, id, czas stworzenia klasy, czas trwania zapytania.

from datetime import datetime

class Zart:
    def __init__(self, id, zart, czas_st, delta_t):
        self.id = id
        self.zart = zart
        self.czas_st = czas_st
        self.delta_t = delta_t


def generatorek()
    i = 1
    missed = 0
    while True:
        start = datetime.now()
        resp = request.get()
        end = datetime.now()
        delta = end - start
        if resp["type"] == "success":
            yield resp
            missed = 0
        else missed +=1
        if missed > 10:
            break
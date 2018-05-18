# Na rozszerz generator z zad 6. tak, żeby zwracał instancję klasy lub namedtuple zwierającą
# dowcip, id, czas stworzenia klasy, czas trwania zapytania.

import requests
import json
from datetime import datetime


class Joke:
    def __init__(self, id, joke, time, delta_t):
        self.id = id
        self.joke = joke
        self.time = time
        self.delta_t = delta_t

    def __repr__(self):
        return "Dowcip o numerze {} został wygenerowany {}. " \
               "Czas trwania zapytania wyniósł {}, a jego treść to: {}"\
            .format(self.id, self.time, self.delta_t, self.joke)


def chuck_norris():
    i = 1
    missed = 0
    while missed < 20:
        start = datetime.now()
        chn = requests.get("https://api.icndb.com/jokes/{}".format(str(i)))
        end = datetime.now()
        delta = end - start
        joke_content = json.loads(chn.content)
        try:
            chn_joke = joke_content['value']['joke']
            joke = Joke(i, chn_joke, start, delta)
            yield joke
            i += 1
            missed = 0
        except TypeError:
            i += 1
            missed += 1


for joke in chuck_norris():
    print(joke)

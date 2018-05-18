# Wykorzystując https://api.icndb.com/jokes/1 lub https://api.icndb.com/jokes/random
# (dokumentacja: http://www.icndb.com/api/) napisz generator,
# który będzie zwracał kolejne żarty o Chucku Norrisie w formie stringa, aż się nie wyczerpią.

import requests
import json


def chuck_norris():
    i = 1
    missed = 0
    while missed < 20:
        chn = requests.get("https://api.icndb.com/jokes/{}".format(str(i)))
        joke_content = json.loads(chn.content)
        try:
            joke = joke_content['value']['joke']
            yield joke
            i += 1
            missed = 0
        except TypeError:
            i += 1
            missed += 1


for joke in chuck_norris():
    print(joke)

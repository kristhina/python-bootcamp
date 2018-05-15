# Wykorzystując https://api.icndb.com/jokes/1 lub https://api.icndb.com/jokes/random
# (dokumentacja: http://www.icndb.com/api/) napisz generator,
# który będzie zwracał kolejne żarty o Chucku Norrisie w formie stringa, aż się nie wyczerpią.

import requests
import json
#
# chn = requests.get("https://api.icndb.com/jokes/1")
# jokes = json.loads(chn.content)
# print(jokes['value']['joke'])

def chuck_norris():
    i = 1
    while True:
        chn = requests.get("https://api.icndb.com/jokes/{}".format(str(i)))
        joke_content = json.loads(chn.content)
        joke = joke_content['value']['joke']
        print(joke)
        i += 1

print(chuck_norris())
#
# Pobierz losowe dane z https://pylove.org/exercise/1_19_2 i
# znajdź hasło, na które złoży się 6 najpopularniejszych
# liter w kolejności malejącej według wystąpień.

import requests
from collections import defaultdict

tekst = requests.get("https://pylove.org/exercise/1_19_2").text

d = defaultdict(int)
for k in tekst:
    d[k] += 1

word = ""
for _ in range(6):
    a_max = 0
    a_let = ''

    for k, v in d.items():
        if v > a_max:
            a_max = v
            a_let = k
    del d[a_let]
    word += a_let

print(word)


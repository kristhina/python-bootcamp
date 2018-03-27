#
# Pobierz losowe dane z https://pylove.org/exercise/1_19_2 i
# znajdź hasło, na które złoży się 6 najpopularniejszych
# liter w kolejności malejącej według wystąpień.

import requests
from collections import defaultdict


tekst = requests.get("https://pylove.org/exercise/1_19_2").text
# tekst = str(tekst_resp.content)
print(tekst)

d = defaultdict(int)
for k in tekst:
    d[k] += 1
print(d.items())

import requests
an_url = "https://pylove.org/exercise/1_19_2"
data = requests.get(an_url).text
zliczacz = defaultdict(int)
for let in data:
    zliczacz[let] += 1
print(zliczacz)
slowo = ""
for _ in range(6):
    a_max = 0
    a_let = ''

    for k, v in zliczacz.items():
        if v>a_max:
            a_max = v
            a_let = k
    del zliczacz[a_let]
    slowo+= a_let

print(slowo)


# Dodaj do zadań 1., 2. wyświetlanie czasu rozpoczęcia oraz zakończenia skryptu oraz czas jego wykonania.

from datetime import datetime
import requests
import json
from collections import defaultdict


t0 = datetime.now()
tekst_resp = requests.get("https://pylove.org/exercise/1_19_1")
tekst = json.loads(tekst_resp.content)
tekst_set = set(tekst)
for sth in tekst_set:
    if sth.isalpha():
        print(sth)
t1 = datetime.now()
roznica = t1-t0
print(t0)
print(t1)
print(roznica)

t2 = datetime.now()
an_url = "https://pylove.org/exercise/1_19_2"
data = requests.get(an_url).text
zliczacz = defaultdict(int)
for let in data:
    zliczacz[let] += 1
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

t3 = datetime.now()
roznica1 = t3-t2
print(t2)
print(t3)
print(roznica1)
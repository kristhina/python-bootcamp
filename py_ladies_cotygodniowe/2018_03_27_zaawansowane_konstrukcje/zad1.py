import requests
import json

tekst_resp = requests.get("https://pylove.org/exercise/1_19_1")
tekst = json.loads(tekst_resp.content)
tekst_set = set(tekst)
for sth in tekst_set:
    if sth.isalpha():
        print(sth)
# wynik = []
# print(' '.join(wynik))
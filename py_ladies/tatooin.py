#Korzystając z API https://swapi.co/api/. Pobierz dane wszystkich mieszkańców planety Tatooin

import requests

zad = requests.get("https://swapi.co/api")
print(zad.json())
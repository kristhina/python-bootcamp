#Korzystając z API https://swapi.co/api/. Pobierz dane wszystkich mieszkańców planety Tatooin

import requests
import json

tatooine = None
url = "https://swapi.co/api/planets/"
found = False
search_name = 'Tatooine'

def check_response_code(response):
    if response.status_code != 200:
        print("There is an error!")
        exit()


while not found:
    all_planets_resp = requests.get(url)
    check_response_code(all_planets_resp)
    all_planets = json.loads(all_planets_resp.content)
    for planet in all_planets["results"]:
        if planet['name'] == search_name:
            tatooine = planet
            found = True
            break
    if not found:
        if "next" in all_planets:
            url = all_planets["next"]
        else:
            print("Planet {0} not found".format(search_name))

planet_residents = []
for resident in tatooine["residents"]:
    resident_resp = requests.get(resident)
    check_response_code(resident_resp)
    resident_data = json.loads(resident_resp.content)
    resident_name = resident_data["name"]
    planet_residents.append(resident_name)

print(planet_residents)




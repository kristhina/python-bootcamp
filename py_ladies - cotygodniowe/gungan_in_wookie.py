import requests
import json


def check_response_code(response):
    if response.status_code != 200:
        print("There is an error!")
        exit()


def species_check(url, search_name):
    while True:
        species_resp = requests.get(url)
        check_response_code(species_resp)
        species = json.loads(species_resp.content)
        for sp in species["results"]:
            if sp["name"] == search_name:
                return sp
        if species["next"] is None:
            return {"error": "We cannot find {} in species".format(search_name)}
        url = species["next"]


gungan = species_check("https://swapi.co/api/species/", "Gungan")

for person in gungan["people"]:
    url = person + "?format=wookiee"
    person_resp = requests.get(url)
    check_response_code(person_resp)
    person_data = json.loads(person_resp.text)
    print(person_data['whrascwo'])





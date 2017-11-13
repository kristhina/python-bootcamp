import requests
import json


def check_response_code(response):
    if response.status_code != 200:
        print("There is an error!")
        exit()


movie_resp = requests.get("https://swapi.co/api/films/")
check_response_code(movie_resp)
movies = json.loads(movie_resp.content)
episode5 = None
for movie in movies["results"]:
    if movie["episode_id"] == 5:
        episode5 = movie

episode5_species = []
for species in episode5["species"]:
    species_resp = requests.get(species)
    check_response_code(species_resp)
    species_data = json.loads(species_resp.content)
    species_name = species_data["name"]
    episode5_species.append(species_name)

print(episode5_species)




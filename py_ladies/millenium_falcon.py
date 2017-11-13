import requests
import json

def check_response_code(response):
    if response.status_code != 200:
        print("There is an error!")
        exit()

def starship_check(url, search_name):
    starships_resp = requests.get(url)
    check_response_code(starships_resp)
    starships = json.loads(starships_resp.content)
    for starship in starships["results"]:
        if starship["name"] == search_name:
            return starship
    if starships["next"] != None:
        url = starships["next"]
        return starship_check(url, search_name)
    else:
        print("The starship {} is not found".format(search_name))


mf = starship_check("https://swapi.co/api/starships/", "Millennium Falcon")


def bmi_counter(height, mass):
    #function that counts BMI when it gets height in cm and mass in kg
    if type(height) != int or type(mass) != int:
        return "It is impossible to count BMI"
    return round(mass/(height*0.01)**2, 2)


for pilot in mf["pilots"]:
    pilot_resp = requests.get(pilot)
    check_response_code(pilot_resp)
    pilot_data = json.loads(pilot_resp.content)
    pilot_name = pilot_data["name"]
    pilot_height = int(pilot_data["height"])
    pilot_mass = int(pilot_data["mass"])
    pilot_bmi = bmi_counter(pilot_height, pilot_mass)
    print("BMI of {} is {}".format(pilot_name, pilot_bmi))


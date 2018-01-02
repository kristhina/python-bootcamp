# Napisz program, który po wejściu na adres /planet-details?planet=Tatooine
# odpowie jsonem zawierającym dane planety,
# o którą zapytał użytkownik (np. klimat, liczba mieszkańców).
# Dane planety program powinien pobierać ze Star Wars API,
# np.: https://swapi.co/api/planets/?search=Tatooine


from flask import Flask, request
import requests
import json

app = Flask(__name__)


@app.route("/planet-details", methods=["GET"])
def planet_details():
    planet_name = request.args.get("planet")
    planet_resp = requests.get("https://swapi.co/api/planets/?search=" + planet_name)
    if planet_resp.status_code != 200:
        return json.dumps({"response": "There is an error!"})
    planets = planet_resp.json()['results']
    if not planets:
        return json.dumps({"response": "planet {} doesn't exist".format(planet_name)})
    planet_data = planets[0]
    return json.dumps({"climate": planet_data['climate'], "population": planet_data['population']})


app.run(debug=True)


# Napisz program, który pod adresem /users/add
# będzie przyjmował zapytania POST z JSON-em o następującej strukturze:
# {"imie": "Grzegorz", "wiek": "26", "plec": "m"}
# W wyniku takiego zapytania dane osoby należy zapisać na serwerze.

# Po wejściu na adres: /users/stats zapytaniem GET program zwróci następującego JSON-a:
# {"ilosc_osob": X, "sredni_wiek": X,
# "najpopularniejsze_imie": X, "plec": {"k": X, "m": X}}
# (Rzecz jasna w miejscu X-ów powinny pojawić się dane
# oparte o dotychczas dodanych użytkowników.
# W kluczu ["plec"]["k"] powinna znaleźć się liczba zapisanych kobiet.)


from flask import Flask, request
import json

app = Flask(__name__)
users = []


@app.route("/users/add", methods=["POST"])
def new_user():
    data = request.get_json()
    users.append(data)
    return "Done"


@app.route("/users/stats", methods=["GET"])
def stats():

    users_count = len(users)

    total_age = 0
    for user in users:
        total_age += int(user['wiek'])
    if users_count == 0:
        age_average = 0
    else:
        age_average = total_age/users_count

    names = {}
    for user in users:
        name = user['imie']
        if name in names:
            names[name] += 1
        else:
            names[name] = 1
    most_popular_name = max(names, key=names.get)

    number_of_women = 0
    number_of_men = 0
    for user in users:
        if user['plec'] == 'k':
            number_of_women += 1
        elif user['plec'] == 'm':
            number_of_men += 1

    return json.dumps({"liczba osob": str(users_count), "sredni wiek": str(age_average),
                       "najpopularniejsze imie": most_popular_name,
                       "plec": {"k": number_of_women, "m": number_of_men}})


@app.route("/users", methods=["GET"])
def get_users():
    return json.dumps(users)

app.run(debug = True)
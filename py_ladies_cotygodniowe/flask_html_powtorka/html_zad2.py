# Napisz aplikację, która będzie wyświetlać dane pracowników pewnej firmy.
# Każdy pracownik będzie mieć identyfikator, imię, nazwisko, płacę,
# opis stanowiska (użyj klasy po stronie serwera).
# Utwórz stonę zawierającą tabelę pracowników (adres wymyśl samodzielnie).
# W każdym wierszu tabeli powinny znaleźć się imię, nazwisko pracownika
# i dodatkowa pusta komórka - uzupełnimy ją w następnym zadaniu.

from flask import Flask, render_template, request, redirect

app = Flask(__name__)


class Pracownik:
    def __init__(self, identyfikator, imie, nazwisko, placa, opis):
        self.id = identyfikator
        self.imie = imie
        self.nazwisko = nazwisko
        self.placa = placa
        self.opis = opis
        self.link = "/pracownik/" + str(self.id)
        self.text = "Więcej informacji o " + str(self.imie) + " " + str(self.nazwisko)


pracownik1 = Pracownik(1, "Tomasz", "Kowalski", 234, "sprząta tylko w poniedziałki")
pracownik2 = Pracownik(2, "Janusz", "Nowak", 23456, "szef wszystkich szefów")
pracownik3 = Pracownik(3, "Malwina", "Zapytka", 1500, "asystentka zawsze uśmiechnięta")
pracownik4 = Pracownik(4, "Remigiusz", "Wierciołek", 2310, "załatwi wszystko, co zechcesz")

pracownicy = [pracownik1, pracownik2, pracownik3, pracownik4]


@app.route('/pracownicy', methods=["GET", "POST"])
def dane_pracownikow():
    if request.method == "POST":
        identyfikator = request.form.get("identyfikator")
        imie = request.form.get("imie")
        nazwisko = request.form.get("nazwisko")
        placa = request.form.get("placa")
        opis = request.form.get("opis")
        pracownicy.append(Pracownik(identyfikator, imie, nazwisko, placa, opis))
        return redirect("/pracownicy")

    return render_template("pracownicy.html", pracownicy=pracownicy)


@app.route('/pracownik/<ident>', methods=['GET', 'POST'])
def dane_pracownika(ident):
    for pracownik in pracownicy:
        if int(pracownik.id) == int(ident):
            if request.method == "POST":
                pracownicy.remove(pracownik)
                return render_template("pracownicy.html", pracownicy=pracownicy)

            return render_template("pracownik.html", pracownik=pracownik, id=ident)


@app.route('/')
def przekierowanie():
    return redirect('/pracownicy')


app.run(debug=True)

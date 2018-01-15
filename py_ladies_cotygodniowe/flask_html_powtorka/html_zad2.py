# Napisz aplikację, która będzie wyświetlać dane pracowników pewnej firmy.
# Każdy pracownik będzie mieć identyfikator, imię, nazwisko, płacę,
# opis stanowiska (użyj klasy po stronie serwera).
# Utwórz stonę zawierającą tabelę pracowników (adres wymyśl samodzielnie).
# W każdym wierszu tabeli powinny znaleźć się imię, nazwisko pracownika
# i dodatkowa pusta komórka - uzupełnimy ją w następnym zadaniu.

from flask import Flask, render_template

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


@app.route('/pracownicy', methods=["GET"])
def dane_pracownikow():
    return render_template("pracownicy.html", pracownicy=pracownicy)


@app.route('/pracownik/<ident>', methods=['GET'])
def dane_pracownika(ident):
    for pracownik in pracownicy:
        if pracownik.id == int(ident):
            return render_template("pracownik.html", pracownik=pracownik)


app.run(debug=True)

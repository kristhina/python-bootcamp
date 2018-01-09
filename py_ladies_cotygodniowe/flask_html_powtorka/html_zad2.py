# Napisz aplikację, która będzie wyświetlać dane pracowników pewnej firmy.
# Każdy pracownik będzie mieć identyfikator, imię, nazwisko, płacę,
# opis stanowiska (użyj klasy po stronie serwera).
# Utwórz stonę zawierającą tabelę pracowników (adres wymyśl samodzielnie).
# W każdym wierszu tabeli powinny znaleźć się imię, nazwisko pracownika
# i dodatkowa pusta komórka - uzupełnimy ją w następnym zadaniu.

from flask import Flask

app = Flask(__name__)

class Pracownik():
    def __init__(self, id, imie, nazwisko, placa, opis):
        self.id = id
        self.imie = imie
        self.nazwisko = nazwisko
        self.placa = placa
        self.opis = opis

pracownik1 = Pracownik(1, "Tomasz", "Kowalski", 234, "lalala")
pracownik2 = Pracownik(2, "Janusz", "Nowak", 23456, "szef wszystkich szefów")

@app.route('/pracownicy', methods = ["GET"])

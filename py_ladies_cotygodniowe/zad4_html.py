# Utwórz klasę Osoba. Każda instancja tej klasy powinna posiadać trzy atrybuty – imię, nazwisko i wiek.
# Utwórz listę kilku dowolnych osób.
# Utwórz szablon HTML, który będzie renderował tabelę osób (imię, nazwisko i wiek powinny wyświetlać się w osobnych kolumnach).
# Napisz program, który po wejściu na adres /osoby renderuje ten szablon.
# Przetestuj program w przeglądar

from flask import Flask, render_template

class Osoba:
    def __init__(self, imie, nazwisko, wiek):
        self.wiek = wiek
        self.nazwisko = nazwisko
        self.imie = imie


Ania = Osoba("Anna", "Kowalska", 17)
Ola = Osoba("Aleksandra", "Nowak", 75)
Jan = Osoba("Jan", "Nowak", 67)

lista_osob = [Ania, Ola, Jan]


app = Flask(__name__)

@app.route("/osoby", methods = ["GET"])
def osoby():
    return render_template("osoby.html", osoby=lista_osob)

app.run(debug=True)


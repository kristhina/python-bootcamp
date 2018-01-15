# Napisz aplikację, która po wejściu na adres "/konto" wyświetli stan konta użytkownika
# i listę ostatnich przelewów.
# Początkowy stan konta ustaw np. na 1000 zł.
# Na stronie powinien znajdować się formularz, umożliwiający wykonanie przelewu -
# powinien zawierać dwa pola tekstowe:
# * nr konta docelowego,
# * kwotę przelewu.
# Po przesłaniu formularza kwota na koncie powinna zostać zmniejszona o podaną wartość,
# ponadto nowy przelew powinien pojawić się na liście ostatnich przelewów.
# Upewnij się, że odświeżenie strony po wykonaniu przelewu
# nie spowoduje wykonania tego przelewu jeszcze raz.

from flask import Flask, render_template, request, redirect

app = Flask(__name__)

stan_konta = 1000
lista_przelewow = []


@app.route("/konto", methods=["GET", "POST"])
def konto():
    if request.method == "POST":
        global stan_konta
        kwota = request.form.get("kwota")
        nr_konta = request.form.get("nr_konta")
        stan_konta -= int(kwota)
        lista_przelewow.append({"kwota": kwota, "numer_konta": nr_konta})
        return redirect("/konto")

    return render_template("konto.html", stan_konta=stan_konta, lista_przelewow=lista_przelewow)


@app.route("/")
def przekierowanie():
    return redirect("/konto")

app.run(debug=True)

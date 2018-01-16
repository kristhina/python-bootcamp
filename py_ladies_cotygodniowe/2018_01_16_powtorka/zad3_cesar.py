# Napisz aplikację - na podstawie podanego szablonu -
# która po podaniu tekstu i liczby zwróci tekst "przesunięty w prawo"
# (uwaga: ograniczamy się do małych liter alfabetu łacińskiego)
# o liczbę podaną przez użytkownika (np. abcd -> bcde, zdcb -> aedc)
# Przydatne funkcje: chr, ord
# Przydatny operator: % (modulo)
# Przydatna informacja: alfabet łaciński ma 26 liter

print(ord("a"))
print(ord("z"))
print(chr(97))
print(chr(122))

from flask import Flask, request, render_template, redirect

app = Flask(__name__)


def szyfrowanie(tekst, przesuniecie):
    nowe_litery = []
    for letter in tekst:
        o = ord(letter)
        new_o = o + int(przesuniecie)
        if new_o > 122:
            new_o -= 26
        nowe_litery.append(chr(new_o))
    zaszyfrowany_tekst = ''.join(nowe_litery)
    return zaszyfrowany_tekst


@app.route('/', methods=['GET', 'POST'])
def cezar_handler():
    encrypted_text = False
    if request.method == 'POST':
        tekst = request.form.get("text")
        przesuniecie = request.form.get("offset")
        encrypted_text = szyfrowanie(tekst, przesuniecie)

    return render_template('cezar.html', encrypted_text=encrypted_text)


app.run(debug=True)


def szyfrowanie(tekst, przesuniecie):
    nowe_litery = []
    for letter in tekst:
        o = ord(letter)
        new_o = o + przesuniecie
        if new_o > 122:
            new_o -= 26
        nowe_litery.append(new_o)
    zaszyfrowany_tekst = ''.join(nowe_litery)
    return zaszyfrowany_tekst

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

@app.route('/', methods=['GET', 'POST'])
def cezar_handler():
    if request.method == 'POST':
        pass # tu dodaj obsluge "szyfrowania"

    return render_template('cezar.html')

app.run(debug=True)
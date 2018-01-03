# Utwórz formularz zawierający dwa inputy o nazwach "liczba1" i "liczba2"
# oraz przycisk do wysłania formularza.
# Wysłanie formularza metodą GET powinno spowodować wyświetlenie strony
# zawierającej sumę liczb wprowadzonych przez użytkownika.

from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/add_form", methods = ["GET", "POST"])
def add():
    liczba1 = request.form.get('liczba1')
    liczba2 = request.form.get('liczba2')
    return render_template('add_form.html', liczba1=liczba1, liczba2=liczba2)

app.run(debug=True)
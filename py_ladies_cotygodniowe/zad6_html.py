# Utwórz formularz zawierający dwa inputy o nazwach "liczba1" i "liczba2"
# oraz przycisk do wysłania formularza.
# Wysłanie formularza metodą GET powinno spowodować wyświetlenie strony
# zawierającej sumę liczb wprowadzonych przez użytkownika.

from flask import Flask, render_template, request

app = Flask(__name__)


@app.route("/add_form", methods=["GET", "POST"])
def add():
    try:
        liczba1 = request.form.get('liczba1')
        liczba2 = request.form.get('liczba2')
        if liczba1 or liczba2 is not None:
            liczba1 = int(liczba1)
            liczba2 = int(liczba2)
            my_sum = liczba1 + liczba2
            return render_template('add_form.html', result=my_sum)
        else:
            return render_template("add_form.html")
    except ValueError:
        error = True
        return render_template("add_form.html", error=error)


app.run(debug=True)

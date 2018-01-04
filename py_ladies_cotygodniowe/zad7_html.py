# Napisz aplikację, która wyświetla stronę HTML zawierającą listę zespołów
# (zdefiniowaną w aplikacji) oraz formularz do wyszukiwania z jednym inputem.
# Przesłanie formularza powinno spowodować wyświetlenie tylko tych zespołów,
# które w nazwie zawierają ciąg znaków podany przez użytkownika.


from flask import Flask, render_template, request

zespoly = ["U2", "Coldplay", "The Kelly Family", "Pink Floyd", "Queen", "Led Zeppelin",
           "The Beatles", "Nirvana", "Aerosmith", "Piano Guys", "Eagles", "The Doors"]


app = Flask(__name__)


@app.route("/zespoly", methods=["GET", "POST"])
def zespoly_lista():
    fragment = request.form.get('fragment')
    return render_template("lista_zespolow.html", lista_zespolow=zespoly,
                           fragment=fragment)


app.run(debug=True)



from flask import Flask

app = Flask(__name__)


@app.route("/add/<int:liczba1>/<int:liczba2>")
def add(liczba1, liczba2):
    return str(liczba1 + liczba2)
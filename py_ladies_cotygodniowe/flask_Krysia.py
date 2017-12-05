from flask import Flask

app = Flask(__name__)

# @app.route("/")
# def hello():
#     return "Hello world!"
#
# app.run(debug = True)
#
# def welcome(name):
#     return "Welcome{}!".format(name)
#
# app.run(debug = True)
#
#
# from flask import Flask, requests
# app = Flask(__name__)
# saved = "Data"
#
# @app.route("/save", methods =["POST"])
# def save():
#     global saved
#     data = request.get_json()
#     saved = data["value"]
#     return "Saved {}".format(data["value"])
#
# @app.route("/read", methods = ["GET"])
# def read():
#     return saved

@app.route("/add/<liczba1>/<liczba2>")
def sum(liczba1, liczba2):
    return str(int(liczba1)+int(liczba2))

app.run(debug = True)


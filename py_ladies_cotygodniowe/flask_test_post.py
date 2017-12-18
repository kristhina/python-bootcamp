import flask
from flask import Flask, request

app = Flask(__name__)

saved = "Data"


@app.route("/name", methods=["PUT"])
def save():
    global saved
    data = request.get_json()
    saved = data["value"]
    json = "{{\"saved\": \"{}\"}}".format(saved)
    resp = flask.Response(json)
    resp.content_type = "application/json"
    return resp


@app.route("/name", methods=["GET"])
def read():
    return saved


app.run(debug=True)








import uuid

from flask import Flask, request, json

app = Flask(__name__)

users = {}

@app.route("/user/<username>/set-password", methods = ["POST"])
def set_password(username):
    # JSON format: ["password": '<tu_haslo>']
    data = request.get_json()
    new_password = data["password"]
    users[username] = new_password
    return "Set password of {} to '{}'".format(username, new_password)

@app.route("/user/<username>/login", methods = ["POST"])
def login(username):
    data = request.get_json()
    if username in users and users[username] == data["password"]:
        return str(uuid.uuid4())
    else:
        return "Wrong password"

@app.route("/users", methods = ["GET"])
def get_users():
    return json.dumps(list(users.keys()))

@app.route("/users/count", methods = ["GET"])
def get_number_of_users():
    return json.dumps({'count': len(users)})

app.run(debug = True)
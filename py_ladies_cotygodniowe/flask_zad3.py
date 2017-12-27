from flask import Flask, request

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
        return "Login successful"
    else:
        return "Wrong password"


app.run(debug = True)
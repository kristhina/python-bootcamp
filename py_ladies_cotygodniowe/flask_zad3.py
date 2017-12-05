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


app.run(debug = True)
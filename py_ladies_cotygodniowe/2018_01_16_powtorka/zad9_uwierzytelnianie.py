# Napisz aplikację, która będzie pozwalała założyć w niej konto posiadające login i hasło.
# Dane użytkowników trzymaj w słowniku. Pamiętaj żeby sprawdzić czy użytkownik
# o danym loginie już nie istnieje.
# Aplikacja też powinna pozwolić zalogować się wykorzystując login i hasło.

from flask import Flask, request, render_template, redirect


class User:
    def __init__(self, name, password):
        self.name = name
        self.password = password
        self.login = False


app = Flask(__name__)

users = {}

doubled = False
wrong = False


@app.route('/users', methods=["GET", "POST"])
def new_user():
    global doubled
    if request.method == "POST":
        user_name = request.form.get("name")
        user_password = request.form.get("password")
        if user_name not in users:
            users[user_name] = User(user_name, user_password)
            doubled = False
        else:
            doubled = True
        return redirect('/users')
    return render_template("users.html", dubbled=doubled)


@app.route('/users/login', methods=["GET", "POST"])
def login_user():
    global wrong

    if request.method == "POST":
        user_name = request.form.get("name")
        user_password = request.form.get("password")
        if user_name in users and users[user_name].password == user_password:
            users[user_name].login = True
            wrong = False
        else:
            wrong = True
        return redirect('/users/login')
    return render_template("users_login.html", wrong=wrong)


@app.route('/list_of_users', methods=["GET"])
def list_of_users():
    return render_template("users_list.html", users=users)


@app.route("/")
def redirect_to_users():
    return redirect("/users")


app.run(debug=True)

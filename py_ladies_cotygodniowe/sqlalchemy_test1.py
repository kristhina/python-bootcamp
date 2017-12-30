from json import JSONEncoder

from flask import Flask, request, make_response
from flask_sqlalchemy import SQLAlchemy
import json

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql+psycopg2://postgres:piontec1@127.0.0.1:5432/postgres'
db = SQLAlchemy(app)


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)

    def __repr__(self):
        return '<User %r>' % self.username


class UserEncoder(JSONEncoder):
    def default(self, user):
        included = {"username": user.username, "email": user.email}
        return included


@app.route("/users", methods=["GET"])
def get_users():
    users = User.query.all()
    return json.dumps(users, cls=UserEncoder), 200, \
           {'Content-Type': 'application/json; charset=utf-8'}


@app.route("/users", methods=["POST"])
def create_user():
    data = request.get_json()
    user = User(username=data["username"], email=data["email"])
    db.session.add(user)
    db.session.commit()
    response = make_response("/user/{}".format(user.username), 201)
    return response


@app.route("/users/<username>", methods=["GET"])
def get_user(username):
    user = User.query.filter_by(username=username).first()
    return json.dumps(user, cls=UserEncoder), 200, \
           {'Content-Type': 'application/json; charset=utf-8'}


app.run(debug=True)

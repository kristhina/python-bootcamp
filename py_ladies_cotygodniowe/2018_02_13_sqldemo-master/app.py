from flask import Flask

from models import db
from views import blog

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///sqldemo.db' #sqlite to nazwa samej bazy danych
# informacja, dokąd się sqlalchemy ma połączyć
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False # bez tej linijki działy się dziwne rzeczy
app.register_blueprint(blog)

db.init_app(app)


if __name__ == '__main__':
    app.run(debug=True)

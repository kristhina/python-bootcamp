from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy() # standardowa procedura związana z tą biblioteką


class BlogPost(db.Model): # reprezentuje model, który ma się pojawić w bazie danych
    id = db.Column(db.Integer, primary_key=True) #identyfikuje obiekt w bazie
    title = db.Column(db.String(80), nullable=False)
    content = db.Column(db.Text()) # w tekście nie trzeba podawać max długości;
    #  nie chcemy rezerwować określonej liczby znaków w tabeli (tak jest w przypadku stringa)
    author = db.Column(db.String(30), nullable=False)
    created = db.Column(db.DateTime(), nullable=False)

    def __repr__(self):
        return "BlogPost(id={}, title='{}', author='{}'".format(self.id, self.title, self.author)
    # magiczna metoda, która mówi, że jeżeli spróbujemy użyć printów, to python wyświetli
    # bardziej szczegółowe informacje na ten temat

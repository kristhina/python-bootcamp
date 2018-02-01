from sqlalchemy import create_engine

from main import db
import models


def db_start():
    create_engine('sqlite:///tmp/test.db', convert_unicode=True)
    db.create_all()
    db.session.commit()
    post_1 = models.BlogPosts()
    post_1.subject = "Pierwszy post"
    post_1.text = "Treść pierwszego postu na blogu"
    db.session.add(post_1)
    db.session.commit()


if __name__ == '__main__':
    db_start()
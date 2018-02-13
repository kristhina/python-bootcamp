from datetime import datetime

from app import app, db
from models import BlogPost

app.app_context().push() # kompletnie magiczna linijka od której wszystko zaczyna działać
# (GP nie wie, dlaczego, wygooglał to sobie)

db.create_all() # linijka, która tworzy bazę danych

post1 = BlogPost(
    title='Welcome to PyLove!',
    content="Let's learn how to write web apps ;)",
    author='Hiromi Uehara',
    created=datetime(2018, 2, 7)
)
post2 = BlogPost(
    title='Example post',
    content='Example post content',
    author='Aaron Parks',
    created=datetime(2018, 2, 10)
)
db.session.add(post1)
db.session.add(post2)
db.session.commit() # dopiero w tym momencie cokolwiek jest zapisywane w bazie danych

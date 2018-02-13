from datetime import datetime

from flask import render_template, redirect, Blueprint, request
from sqlalchemy import desc

from models import BlogPost, db

blog = Blueprint('blog', __name__) # korzystamy z tego tak, jakby to była nasza aplikacja


@blog.route('/', methods=['GET']) # po prostu przekierowanie na ścieżkę posts
def redirect_to_posts():
    return redirect('/posts')


@blog.route('/posts', methods=['GET']) # nazwa klasy + query + co chcemy wyciągnąć
# (all jeśli wszystko, co jest w bazie danych),
# tutaj order by, bo chcemy wszystko, ale uporządkowane
# potem kolumna, po której chcemy sortować
def posts():
    posts = BlogPost.query.order_by(desc(BlogPost.created))
    return render_template('posts.html', posts=posts)


@blog.route('/post/<int:id>', methods=['GET']) # tutaj mamy treść posta
def post(id):
    post = BlogPost.query.get(id) # operacja wyciągnięca rekordu o danych id
    return render_template('post.html', post=post)


@blog.route('/posts/create', methods=['POST'])
def create_post():
    new_post = BlogPost(
        title=request.form['title'],
        content=request.form['content'],
        author=request.form['author'],
        created=datetime.now(),
    )
    db.session.add(new_post)
    db.session.commit()
    return redirect('/posts')

@blog.route('/post/int:<id>/edit', methods=['PUT'])
def edit_post():


from main import app
from main import db

from flask import render_template, request, redirect
from models import BlogPosts
from sqlalchemy import desc


@app.route('/', methods=["GET", "POST"])
def info():
    blogposts = BlogPosts.query.all().order_by(desc(BlogPosts.id))
    return render_template('info.html', blogposts=blogposts)


@app.route('/new-post', methods=['POST'])
def new_post():
    content = request.form['content']
    subject = request.form['subject']
    post = BlogPosts(text=content, subject=subject)
    db.session.add(post)
    db.session.commit()
    return redirect('/')
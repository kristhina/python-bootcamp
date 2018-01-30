from main import app1

from flask import render_template, request



@app.route('/', methods = ["GET", "POST"])
def info():
    return render_template('info.html')
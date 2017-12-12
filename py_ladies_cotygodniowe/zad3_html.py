from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/hello")
def hello():
    name = request.args.get("name", "") # jeśli użytkownik nie poda, to będzie pusty ciąg znaków
    return render_template(
        'hello.html',
        naglowek=name,
    )

app.run(debug=True)



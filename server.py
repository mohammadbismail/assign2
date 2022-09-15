from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def hello_world():
    return render_template("index.html")


@app.route("/play")
def play():
    return render_template("index.html")


@app.route("/play/<x>")
def second(x):
    return render_template("second.html", num=int(x))


@app.route("/play/<x>/<color>")
def third(x, color):
    return render_template("third.html", num=int(x), box_color=color)


if __name__ == "__main__":
    app.run(debug=True)

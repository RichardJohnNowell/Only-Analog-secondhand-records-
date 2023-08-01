
import os
from flask import Flask, render_template


app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/listings")
def listings():
    return render_template("listings.html")


@app.route("/blog")
def blog():
    return render_template("blog.html")


@app.route("/opinions")
def opinions():
    return render_template("opinions.html")


@app.route("/contact")
def contact():
    return render_template("contact.html")


@app.route("/login")
def login():
    return render_template("login.html")


@app.route("/register")
def register():
    return render_template("register.html")


@app.route("/records")
def records():
    return render_template("records.html")


@app.route("/cassettes")
def cassettes():
    return render_template("cassettes.html")


if __name__ == "__main__":
    app.run(
        host=os.environ.get("IP", "0.0.0.0"),
        port=int(os.environ.get("PORT", "5000")),
        debug=True)
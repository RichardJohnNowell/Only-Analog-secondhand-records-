
import os
from flask import Flask, render_template


app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/listings")
def listings():
    return render_template("listings.html", page_title="Listings")


@app.route("/blog")
def blog():
    return render_template("blog.html", page_title="Blog")


@app.route("/opinions")
def opinions():
    return render_template("opinions.html", page_title="Opinions")


@app.route("/contact")
def contact():
    return render_template("contact.html", page_title="Contact")


if __name__ == "__main__":
    app.run(
        host=os.environ.get("IP", "0.0.0.0"),
        port=int(os.environ.get("PORT", "5000")),
        debug=True)
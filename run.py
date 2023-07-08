#python core file
import os
from flask import Flask, render_template


app = Flask(__name__)

#routing here

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
def tech():
    return render_template("opinions.html")


@app.route("/contact")
def contact():
    return render_template("contact.html")


if __name__ == "__main__":
    app.run(
        host=os.environ.get("IP", "0.0.0.0"),
        port=int(os.environ.get("PORT", "5000")),
        debug=True)
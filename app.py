#start
import os
from flask import Flask, request, session, redirect, url_for, render_template, flash

app = Flask(__name__)

"""
#postgresql database values
app.config["RENDER_HOST"] = os.environ.get("RENDER_HOST")
app.config["RENDER_NAME"] = os.environ.get("RENDER_NAME")
app.config["RENDER_PASSWORD"] = os.environ.get("RENDER_PASSWORD")
app.config["RENDER_PORT"] = os.environ.get("RENDER_PORT")
app.config["RENDER_URL"] = os.environ.get("RENDER_URL")
app.config["RENDER_USERNAME"] = os.environ.get("RENDER_USERNAME")
#secret key
app.secret_key = os.environ.get("SECRET_KEY")
#postgresql database connection using psycopg2
conn = psycopg2.connect("dbname=RENDER_NAME user=RENDER_USERNAME password=RENDER_PASSWORD host=RENDER_HOST port=RENDER_PORT url=RENDER_URL")
"""

@app.route("/")
def index():
    """
    routing for homepage
    """
    return render_template("index.html")


@app.route("/listings")
def listings():
    """
    routing for listings page
    """
    return render_template("listings.html")


@app.route("/records")
def records():
    """
    routing for records page
    """
    return render_template("records.html")


@app.route("/cassettes")
def cassettes():
    """
    routings for cassettes page
    """
    return render_template("cassettes.html")


@app.route("/blog")
def blog():
    """
    routing for blog page
    """
    return render_template("blog.html")


@app.route("/opinions")
def opinions():
    """
    routing for opinions page
    """
    return render_template("opinions.html")


@app.route("/contact")
def contact():
    """
    routing for contact page
    """
    return render_template("contact.html")


@app.route("/login")
def login():
    """
    routing for login page
    """
    return render_template("login.html")


@app.route("/register")
def register():
    """
    routing for register page
    """
    return render_template("register.html")


@app.route("/profile")
def profile():
    """
    routing for profile page
    """
    return render_template("profile.html")


if __name__ == "__main__":
    app.run(
        host=os.environ.get("IP", "0.0.0.0"),
        port=int(os.environ.get("PORT", "5000")),
        debug=True)

# app.py start
import os
from flask import (Flask, request, session, redirect, url_for,
                   render_template, flash)
import re
from werkzeug.security import generate_password_hash, check_password_hash
if os.path.exists("env.py"):
    import env


app = Flask(__name__)


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


"""
@app.route("/profile")
def profile():
    routing for profile page
    return render_template("profile.html")
"""


if __name__ == "__main__":
    app.run(
        host=os.environ.get("IP", "0.0.0.0"),
        port=int(os.environ.get("PORT", "5000")),
        debug=True)

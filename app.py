#start
import os
from flask import Flask, request, session, redirect, url_for, render_template, flash
import psycopg2-binary
import re
from werkzeug import generate_password_hash, check_password_hash


app = Flask(__name__)

"""
app.secret_key = "secret key"

#postgresql database
DB_HOST = "dpg-cj15uic07spjv9qfcr0g-a"
DB_NAME = "only_analog_records"
DB_PASS = "etc"
DB_PORT = "5432"
DB_USER = "only_analog_records_user"

#connection to sql
conn = psycopg2.connect(
    database="only_analog_records",
    host="dpg-cj15uic07spjv9qfcr0g-a",
    password="etc",
    port="5432",
    user="only_analog_records_user")
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

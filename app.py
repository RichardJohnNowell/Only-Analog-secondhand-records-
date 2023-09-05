"""start of only analog python file app.py"""


import os
import urllib.parse as up
import re
from flask import (Flask, request, session, redirect, url_for, render_template,
                   flash)
import psycopg2
import psycopg2.extras
from werkzeug.security import generate_password_hash, check_password_hash


# if the environment file is available, use that
if os.path.exists("env.py"):
    import env


# creating a Flask instance
app = Flask(__name__)


# key import
SECRET_KEY = os.environ.get("SECRET_KEY")


# key configuration
app.config["SECRET_KEY"] = SECRET_KEY


# elephant sql parse
up.uses_netloc.append("postgres")


# fetching database link from environment file
url = up.urlparse(os.environ["DATABASE_URL"])


# using psycopg2 to connect to the elephant sql database
conn = psycopg2.connect(
    database=url.path[1:],
    user=url.username,
    password=url.password,
    host=url.hostname,
    port=url.port,
)


# routes for different pages
@app.route("/")
def index():
    """
    routing for homepage with loggedin option
    """
    # check if user is logged in
    if "loggedin" in session:
        # if user logged in show them the homepage with name
        return render_template("index.html", username=session["username"])
        # if user is not logged in show them to the homepage
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


@app.route("/login", methods=["GET", "POST"])
def login():
    """
    routing for login page sorting
    """
    # postgres connection with cursor from extras dictionary
    cursor = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)
    # check if "username" and "password" POST requests exist
    if (
        request.method == "POST"
        and "username" in request.form
        and "password" in request.form
    ):
        username = request.form["username"]
        password = request.form["password"]
        print(password)
        # check if account exists using postgres query of oa_memb
        cursor.execute("SELECT * FROM oa_memb \
                       WHERE username = %s", (username,))
        # fetch one record and return the result
        account = cursor.fetchone()
        # check if entry is correct or incorrect
        if account:
            password_rs = account["password"]
            print(password_rs)
            if check_password_hash(password_rs, password):
                # create session data
                session["loggedin"] = True
                session["id"] = account["id"]
                session["username"] = account["username"]
                # go to profile page
                return redirect(url_for("profile"))
            else:
                # account does not exist or username/password incorrect
                flash("Incorrect username/password")
        else:
            # account does not exist or username/password incorrect
            flash("Incorrect username/password")
    return render_template("login.html")


@app.route("/logout")
def logout():
    """
    routing for logout page
    """
    # session ends
    session.pop("loggedin", None)
    session.pop("id", None)
    session.pop("username", None)
    # logout message
    flash('You have been logged out')
    # redirect to homepage
    return redirect(url_for("login"))


@app.route("/register", methods=["GET", "POST"])
def register():
    """
    routing for register page
    """
    # postgres connection with cursor from extras dictionary
    cursor = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)
    # check if "username", "password" and "email" POST requests exist
    if (
        request.method == "POST"
        and "username" in request.form
        and "password" in request.form
        and "email" in request.form
    ):
        # create variables for easy access
        fullname = request.form["fullname"]
        username = request.form["username"]
        password = request.form["password"]
        email = request.form["email"]
        # generate password security hash
        _hashed_password = generate_password_hash(password)
        # check if oa_memb account exists using postgres
        cursor.execute("SELECT * FROM oa_memb \
            WHERE username = %s", (username,))
        account = cursor.fetchone()
        print(account)
        # if account exists show error and validation checks
        if account:
            flash("Account already exists!")
        elif not re.match(r"[^@]+@[^@]+\.[^@]+", email):
            flash("Invalid email address!")
        elif not re.match(r"[A-Za-z0-9]+", username):
            flash("Username must contain only characters and numbers!")
        elif not username or not password or not email:
            flash("Please fill out the form!")
        else:
            # if account does not exist and the form data is valid then
            # insert a new account into the oa_memb membership
            cursor.execute(
                "INSERT INTO oa_memb (fullname, username, password, email) \
                    VALUES (%s,%s,%s,%s)",
                (fullname, username, _hashed_password, email),
            )
            conn.commit()
            # registration ok message
            flash("You have successfully registered!")
    elif request.method == "POST":
        # form is empty as no POST data
        flash("Please fill out the form!")
        # show registration form with message or not
    return render_template("register.html")


@app.route("/profile")
def profile():
    """
    routing for profile page
    """
    # postgres connection with cursor from extras dictionary
    cursor = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)
    # check if user is logged in
    if "loggedin" in session:
        # postgres query from oa_memb membership
        cursor.execute("SELECT * FROM oa_memb WHERE id = %s", [session["id"]])
        account = cursor.fetchone()
        # show the profile page with account info
        return render_template("profile.html", account=account)
        # user is not logged in so redirected to login page
    return redirect(url_for("login"))


@app.route("/delete_profile")
def delete_profile():
    """
    routing for deleting profile
    """
    # postgres connection with cursor from extras dictionary
    cursor = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)
    # delete member using sql
    cursor.execute("DELETE FROM oa_memb WHERE id = %s", [session["id"]])
    # delete message
    flash("Your Profile Has Been Deleted")
    # back to the homepage
    return render_template("index.html")


# debug is false
if __name__ == "__main__":
    app.run(
        host=os.environ.get("IP", "0.0.0.0"),
        port=int(os.environ.get("PORT", "5000")),
        debug=False)


# end of only analog python file app.py

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


if __name__ == "__main__":
    app.run(
        host=os.environ.get("IP", "0.0.0.0"),
        port=int(os.environ.get("PORT", "5000")),
        debug=True)
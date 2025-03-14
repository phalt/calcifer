import os

from flask import Flask, render_template

from calciferpi.settings import settings

# Determine the directory where the current script is located.
BASE_DIR = os.path.abspath(os.path.dirname(__file__))
STATIC_DIR = os.path.join(BASE_DIR, "static/")
TEMPLATE_DIR = os.path.join(BASE_DIR, "templates/")

app = Flask(__name__, static_folder=STATIC_DIR, template_folder=TEMPLATE_DIR)


@app.route("/")
def index():
    return render_template("index.html")


def run():
    app.run(debug=settings.SERVER_DEBUG, port=settings.SERVER_PORT)

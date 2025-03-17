import os

from flask import Flask, render_template

from calciferpi import readings
from calciferpi.settings import settings

# Determine the directory where the current script is located.
BASE_DIR = os.path.abspath(os.path.dirname(__file__))
STATIC_DIR = os.path.join(BASE_DIR, "static/")
TEMPLATE_DIR = os.path.join(BASE_DIR, "templates/")

app = Flask(__name__, static_folder=STATIC_DIR, template_folder=TEMPLATE_DIR)


@app.route("/readings/local")
def get_local_reading():
    """
    Return the current temperature and humidity reading from the DHT22 sensor
    located on the same Raspberry Pi as the server.
    """
    reading = readings.get_readings()
    return render_template("reading.html", reading=reading.model_dump())


@app.route("/")
def index():
    reading = readings.get_readings()
    return render_template("index.html", context={"readings": [reading.model_dump()]})


def run():
    app.run(host=settings.SERVER_HOST, debug=settings.SERVER_DEBUG, port=settings.SERVER_PORT)

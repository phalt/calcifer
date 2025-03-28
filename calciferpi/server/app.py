import os

from flask import Flask, render_template

from calciferpi import readings
from calciferpi.server import nodes
from calciferpi.settings import settings

# Determine the directory where the current script is located.
BASE_DIR = os.path.abspath(os.path.dirname(__file__))
STATIC_DIR = os.path.join(BASE_DIR, "static/")
TEMPLATE_DIR = os.path.join(BASE_DIR, "templates/")

app = Flask(__name__, static_folder=STATIC_DIR, template_folder=TEMPLATE_DIR)


@app.route("/api/reading")
def get_api_reading():
    """
    Returns a JSON response for the local devices' readings.
    This is the "node" endpoint used by other CalciferPi hosts
    """
    reading = readings.get_readings()
    return reading.model_dump_json()


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
    local_reading = readings.get_readings()
    all_readings = [local_reading] + nodes.get_node_readings()
    return render_template("index.html", context={"readings": [r.model_dump() for r in all_readings]})


def run():
    app.run(host=settings.SERVER_HOST, debug=settings.SERVER_DEBUG, port=settings.SERVER_PORT)

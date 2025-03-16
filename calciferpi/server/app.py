import os

from flask import Flask, render_template
from pydantic import BaseModel

from calciferpi.readings import get_humidity, get_temperature
from calciferpi.settings import settings

# Determine the directory where the current script is located.
BASE_DIR = os.path.abspath(os.path.dirname(__file__))
STATIC_DIR = os.path.join(BASE_DIR, "static/")
TEMPLATE_DIR = os.path.join(BASE_DIR, "templates/")

app = Flask(__name__, static_folder=STATIC_DIR, template_folder=TEMPLATE_DIR)


class Reading(BaseModel):
    name: str
    temperature: float
    humidity: float


@app.route("/")
def index():
    readings = Reading(name="Paul's room", temperature=get_temperature(), humidity=get_humidity())
    return render_template("index.html", context={"readings": [readings.model_dump()]})


def run():
    app.run(debug=settings.SERVER_DEBUG, port=settings.SERVER_PORT)

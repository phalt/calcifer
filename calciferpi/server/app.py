import os

from flask import Flask, render_template
from pydantic import BaseModel

from calciferpi import readings
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
    temp, hum = readings.get_readings()
    reading = Reading(name="Paul's room", temperature=temp, humidity=hum)
    return render_template("index.html", context={"readings": [reading.model_dump()]})


def run():
    app.run(debug=settings.SERVER_DEBUG, port=settings.SERVER_PORT)

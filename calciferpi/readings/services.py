# TODO: Gracefully handle importing this on non-Raspberry Pi devices
import datetime

import adafruit_dht
from pydantic import BaseModel

from calciferpi import dht
from calciferpi.settings import settings as calcifer_settings


class Reading(BaseModel):
    device_name: str
    temperature: float
    humidity: float
    time: datetime.datetime


def get_readings() -> Reading:
    """
    Returns temperature, humidity
    """
    device = dht.get_dht22_device()
    readings = Reading(
        device_name=calcifer_settings.DEVICE_NAME,
        temperature=_get_temperature(device=device),
        humidity=_get_humidity(device=device),
        time=datetime.datetime.now(),
    )
    device.exit()
    return readings


def _get_temperature(device: adafruit_dht.DHT22 | None) -> float:
    if device is None:
        return -20.0
    return device.temperature


def _get_humidity(device: adafruit_dht.DHT22 | None) -> float:
    if device is None:
        return -50.0
    return device.humidity

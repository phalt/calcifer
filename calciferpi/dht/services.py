import adafruit_dht
import board as raspberry_pi_gpio
from adafruit_blinka.microcontroller.generic_micropython import Pin

from calciferpi.settings import settings as calcifer_settings


def _determine_pin_from_int(pin: int) -> Pin:
    # TODO: support all the correct GPIO pins
    return {
        4: raspberry_pi_gpio.D4,
        17: raspberry_pi_gpio.D17,
    }


def get_dht22_device() -> adafruit_dht.DHT22:
    data_out_pin = _determine_pin_from_int(calcifer_settings.DATA_PIN)
    return adafruit_dht.DHT22(pin=data_out_pin)

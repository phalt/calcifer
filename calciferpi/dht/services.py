import adafruit_dht
from pydantic import BaseModel

from calciferpi.settings import settings as calcifer_settings


class DebugDHT22(BaseModel):
    """
    A debug class to simulate the DHT22 sensor.
    Used when settings.DEBUG is True.
    """

    temperature: float = -20.0
    humidity: float = -50.0

    def exit(self):
        pass


def get_dht22_device() -> adafruit_dht.DHT22 | DebugDHT22:
    if calcifer_settings.DEBUG:
        return DebugDHT22()
    else:
        # Imported here to prevent explosions in non-Raspberry Pi environments
        import board as raspberry_pi_gpio
        from adafruit_blinka.microcontroller.generic_micropython import Pin

        def _determine_pin_from_int(pin: int) -> Pin:
            # TODO: support all the correct GPIO pins
            return {
                4: raspberry_pi_gpio.D4,
                17: raspberry_pi_gpio.D17,
            }[pin]

        data_out_pin = _determine_pin_from_int(calcifer_settings.DATA_PIN)
        return adafruit_dht.DHT22(pin=data_out_pin)

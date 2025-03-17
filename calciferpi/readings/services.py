# TODO: Gracefully handle importing this on non-Raspberry Pi devices
import adafruit_dht

from calciferpi import dht


def get_readings() -> [float, float]:
    """
    Returns temperature, humidity
    """
    device = dht.get_dht22_device()
    return [_get_temperature(device=device), _get_humidity(device=device)]


def _get_temperature(device: adafruit_dht.DHT22 | None) -> float:
    if device is None:
        return -20.0
    return device.temperature


def _get_humidity(device: adafruit_dht.DHT22 | None) -> float:
    if device is None:
        return -50.0
    return device.humidity

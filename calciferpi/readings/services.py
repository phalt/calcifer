def _get_device():
    # TODO: Gracefully handle importing this on non-Raspberry Pi devices
    from calciferpi.dht import get_dht22_device

    return get_dht22_device()


def get_temperature() -> float:
    device = _get_device()
    if device is None:
        return -20.0
    return device.temperature


def get_humidity() -> float:
    device = _get_device()
    if device is None:
        return -50.0
    return device.humidity

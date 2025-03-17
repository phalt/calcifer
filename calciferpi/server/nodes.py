# Handles querying other nodes for their readings
import datetime
import httpx

from calciferpi import readings
from calciferpi.settings import settings as calcifer_settings


def _get_node_reading(node_address: str) -> dict:
    return httpx.get(f"{node_address}/api/reading").json()


def get_node_readings() -> list[readings.Reading]:
    if not calcifer_settings.NODES:
        return []

    node_readings: list[readings.Reading] = []

    for node_address in calcifer_settings.NODES:
        raw_reading = _get_node_reading(node_address=node_address)
        node_readings.append(
            readings.Reading(
                temperature=raw_reading["temperature"],
                humidity=raw_reading["humidity"],
                device_name=raw_reading["device_name"],
                time=raw_reading["time"],
            )
        )
    return node_readings

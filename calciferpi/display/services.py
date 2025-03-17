from datetime import datetime

from rich.columns import Columns
from rich.panel import Panel


def generate_standard_layout(temp: float, hum: float) -> Columns:
    temp_panel = Panel(
        f"{temp}°C",
        title="🌡️",
    )
    hum_panel = Panel(
        f"{hum}%",
        title="💦",
    )
    now = datetime.now()
    time_panel = Panel(f"{datetime.strftime(now, '%H:%M:%S %d-%m-%Y')}", title="🕒")
    return Columns([temp_panel, hum_panel, time_panel])

from datetime import datetime

from rich.columns import Columns
from rich.panel import Panel


def generate_standard_cli_layout(temp: float, hum: float, time: datetime) -> Columns:
    temp_panel = Panel(
        f"{temp}°C",
        title="🌡️",
    )
    hum_panel = Panel(
        f"{hum}%",
        title="💦",
    )
    time_panel = Panel(f"{datetime.strftime(time, '%H:%M:%S %d-%m-%Y')}", title="🕒")
    return Columns([temp_panel, hum_panel, time_panel])

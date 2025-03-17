import click


@click.group()
def cli_group():
    """
    CalciferPi 🔥🍓:  The simplest Raspberry Pi temperature sensor

    https://github.com/phalt/calcifer
    """


@click.command()
def version():
    """
    Print the current version of calficerpi
    """
    from calciferpi.settings import (
        VERSION,
    )

    print(f"calciferpi {VERSION}")


@click.command()
def read():
    """
    Read the temperature and humidity from the DHT22 sensor
    """
    from datetime import datetime

    from rich.columns import Columns
    from rich.console import (
        Console,
    )
    from rich.panel import Panel

    from calciferpi import readings

    console = Console()
    temp, hum = readings.get_readings()
    temp_panel = Panel(
        f"{temp}°C",
        title="🌡️",
    )
    hum_panel = Panel(
        f"{hum}%",
        title="💦",
    )
    console.print(Columns([temp_panel, hum_panel]))
    now = datetime.now()
    console.print(Columns([Panel(f"{datetime.strftime(now, '%H:%M:%S %d-%m-%Y')}", title="🕒")]))


@click.command()
def host():
    """
    Run the micro web server in host mode
    """
    from calciferpi.server.app import app

    app.run()


cli_group.add_command(version)
cli_group.add_command(read)
cli_group.add_command(host)

if __name__ == "__main__":
    cli_group()

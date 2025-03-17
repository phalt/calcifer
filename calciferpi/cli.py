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
    Runs once and then exits
    """
    from rich.console import (
        Console,
    )

    from calciferpi import displays, readings

    console = Console()
    temp, hum = readings.get_readings()
    layout = displays.generate_standard_cli_layout(temp=temp, hum=hum)
    console.print(layout)


@click.command()
def live():
    """
    Display a live updating display of the temperature and humidity and refreshes every 60 seconds
    """
    import time

    from rich.console import (
        Console,
    )
    from rich.live import Live

    from calciferpi import displays, readings

    def _live_reading():
        temp, hum = readings.get_readings()
        return displays.generate_standard_cli_layout(temp=temp, hum=hum)

    console = Console()

    with Live(_live_reading(), refresh_per_second=1, console=console, screen=True) as live:
        while True:
            time.sleep(60)
            live.update(_live_reading(), refresh=True)


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
cli_group.add_command(live)

if __name__ == "__main__":
    cli_group()

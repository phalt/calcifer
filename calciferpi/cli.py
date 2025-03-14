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
    from rich.console import (
        Console,
    )

    from calciferpi import readings

    console = Console()
    temp = readings.get_temperature()
    console.print(f"🌡️ Temperature: {temp}°C")
    hum = readings.get_humidity()
    console.print(f"💦 Humidity: {hum}%")


@click.command()
def serve():
    """
    Run the micro web server
    """
    from calciferpi.server.app import app

    app.run()


cli_group.add_command(version)
cli_group.add_command(read)
cli_group.add_command(serve)

if __name__ == "__main__":
    cli_group()

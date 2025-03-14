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
@click.option(
    "-i",
    "--input",
    help="Example input command",
    required=True,
)
def example(
    input,
):
    """
    Generate a "basic" file structure, no code.
    """
    from rich.console import (
        Console,
    )

    console = Console()
    console.log(f"{input}")


cli_group.add_command(version)
cli_group.add_command(example)

if __name__ == "__main__":
    cli_group()

"""Console script for viana_ff."""
import viana_ff

import typer
from rich.console import Console

app = typer.Typer()
console = Console()


@app.command()
def main():
    """Console script for viana_ff."""
    console.print("Replace this message by putting your code into "
                  "viana_ff.cli.main")
    console.print("See Typer documentation at https://typer.tiangolo.com/")


if __name__ == "__main__":
    app()

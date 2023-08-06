from pathlib import Path
from typing import Optional, Any

import click
import typer

from . import __version__
from .chord import Chord, Chords

app = typer.Typer()


@app.command()
def print_version(ctx: click.Context, value: bool) -> Any:
    """
    show uke version.
    """
    if not value or ctx.resilient_parsing:
        return
    typer.echo(f"uke version: {__version__} :capricorn:")
    raise typer.Exit()


if __name__ == "__main__":
    typer.run(print_version())

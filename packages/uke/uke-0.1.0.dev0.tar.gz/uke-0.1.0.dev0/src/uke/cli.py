from pathlib import Path
from typing import Optional
import sys

import click
import typer

from . import __version__, Chord, Chords

app = typer.Typer()


@app.command()
def print_version(ctx: click.Context, value: bool) -> None:
    if not value or ctx.resilient_parsing:
        return
    typer.echo(f"uchord2 version: {__version__}")
    raise typer.Exit()


if __name__ == "__main__":
    typer.run(print_version())
    sys.exit(app())

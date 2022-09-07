#!/usr/bin/python
import typer
import rich
from utilities.formatter.number import print_number

import typer

app = typer.Typer()


@app.command()
def hello(number: int):
    if number < 0:
        rich.print(
            "[bold red]Error: Comat currently doesn't support negative numbers[/bold red]"
        )
    else:
        print_number(number)


if __name__ == "__main__":
    app()

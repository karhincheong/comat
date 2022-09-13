#!/usr/bin/python
import typer
import rich
from algorithms.statistics import mean_from_array
from utilities.formatter.number import print_number
from typing import List

app = typer.Typer()


@app.command()
def number(number: int):
    if number < 0:
        rich.print(
            "[bold red]Error: Comat currently doesn't support negative numbers[/bold red]"
        )
    else:
        print_number(number)


@app.command()
def stats(arr: List[int], method: str):
    if method == "mean":
        print(mean_from_array(arr))


if __name__ == "__main__":
    app()

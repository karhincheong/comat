#!/usr/bin/python
from rich.console import Console
import sys

sys.path.append("../../algorithms")
from algorithms.factors import *

console = Console()


def print_num(number):
    console.print(f"[u][bold blue]{number}[/bold blue][/u]")


def print_factorization(number):
    factorization = prime_factorization(number)
    console.print(f"[b]Prime factorization[/b]: [u blue]{factorization}[/u blue]")


def print_factors(number):
    factor_ls = factor_list(number)
    console.print(
        f"[b]Factors[/b]: [u blue]{','.join(str(factor) for factor in factor_ls) }[/u blue]"
    )

#!/usr/bin/python
from rich.console import Console
from algorithms.factors import *

console = Console()


def print_num(number):
    console.print(f"[u][bold blue]{number}[/bold blue][/u]")


def print_factorization(number):
    factorization = prime_factorization(number)
    console.print(f"[b]Prime factorization[/b]: [u blue]{factorization}[/u blue]")


def print_factors(number):
    global factor_ls
    factor_ls = factor_list(number)
    console.print(
        f"[b]Factors[/b]: [u blue]{','.join(str(factor) for factor in factor_ls) }[/u blue]"
    )

def print_parity(number):
    if 2 in factor_ls:
        console.print(f"[b]Odd/Even[/b]: [blue u]Even[blue u]")
    else:
        console.print(f"[b]Odd/Even[/b]: [blue u]Odd[blue u]")

def print_number(number):
    print_num(number)
    print_factorization(number)
    print_factors(number)
    print_parity(number)
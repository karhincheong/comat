#!/usr/bin/python
from rich.console import Console
from algorithms.factors import *
from algorithms.bases import *
console = Console()


def print_num(number):
    console.print(f"[b]Number[/b]: [u][bold blue]{number}[/bold blue][/u]")


def print_factorization(number):
    factorization = prime_factorization(number)
    console.print(f"[b]Prime factorization[/b]: [blue]{factorization}[blue]")


def print_factors(number):
    global factor_ls
    factor_ls = factor_list(number)
    console.print(
        f"[b]Factors[/b]: [blue]{', '.join(str(factor) for factor in factor_ls)}[/blue]"
    )


def print_parity(number):
    parity = "Even" if number % 2 == 0 else "Odd"
    console.print(f"[b]Parity[/b]: [blue]{parity}[/blue]")

def print_bases(number):
    console.print(f"[b]Hexadecimal[/b]: [blue]{get_hex(number)}[blue]")
    console.print(f"[b]Binary[/b]: [blue]{get_bin(number)}[blue]")

def print_number(number):
    print_num(number)
    print_factorization(number)
    print_factors(number)
    print_parity(number)
    print_bases(number)

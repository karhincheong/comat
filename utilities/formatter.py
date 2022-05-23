#!/usr/bin/python
from rich.console import Console
import sys
sys.path.append('../factors')
from factors.factors import prime_factorization
console = Console()


def print_num(number):
    console.print(f"[u][bold blue]{number}[/bold blue][/u]")


def print_factorization(number):
    factorization = prime_factorization(number)
    console.print(f"Prime factorization: {factorization}")

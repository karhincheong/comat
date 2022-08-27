#!/usr/bin/python
import argparse
from utilities.formatter.number import *
from rich import print

parser = argparse.ArgumentParser()

# Number argument
parser.add_argument("-n", "--number", type=int, help="Enter a non-negative integer and it will tell you its properties", required=True)

args = parser.parse_args()
#print_number(args.number)
if args.number < 0:
    print("[bold magenta]Mat doesn't support negative integers[/bold magenta]")
else:
    print_number(args.number)

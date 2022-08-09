#!/usr/bin/python
import argparse
from utilities.formatter.number import *

parser = argparse.ArgumentParser()

# Number argument
parser.add_argument("-n", "--number", type=int, help="Enter a number and it will tell you its properties", required=True)

args = parser.parse_args()
print_number(args.number)

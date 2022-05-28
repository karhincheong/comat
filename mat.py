#!/usr/bin/python
import argparse
from utilities.formatter import *

parser = argparse.ArgumentParser()

# Number argument
parser.add_argument("-n", "--number", type=int, help="Enter a number", required=True)

args = parser.parse_args()
print_num(args.number)
print_factorization(args.number)
print_factors(args.number)

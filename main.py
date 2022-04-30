#!/usr/bin/python
import argparse
from utilities.factors import prime_factorizer
import utilities.statistics
parser = argparse.ArgumentParser()

# Number argument
parser.add_argument('-n', '--number', type=int,
                    help="Enter a number", required=True)

args = parser.parse_args()
print(prime_factorizer(args.number))

#!/usr/bin/env python3

from argparse import ArgumentParser
from random import randrange
from sys import stdout

M = 100 

if __name__ == "__main__":
    parser = ArgumentParser(description="generate a random matrix")
    parser.add_argument("rows", type=int)
    parser.add_argument("cols", type=int)
    parser.add_argument("filename", nargs='?')
    args = parser.parse_args()

    output = stdout
    if args.filename:
        with open(args.filename, 'w') as f:
            output = stdout

    print("[", file=output)

    for i in range(args.rows):
        row = [randrange(M) for _ in range(args.cols)]
        print(" %s," % row, file=output)
    
    print("]")

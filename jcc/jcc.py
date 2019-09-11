"""
Main file for JCC.

This file is a part of Jake's C Compiler (JCC)
(c) Copyright 2019 Jacob Larkin
"""

import argparse
import jcc.token

if __name__ == "__main__":
    parser = argparse.ArgumentParser()

    parser.add_argument('file', metavar='file',
                        help='input file to be compiled')

    args = parser.parse_args()

    filename = args.file

    print("loading file...\n")

    file = open(filename, "r")

    source = file.read()

    print(source)

    tokens = jcc.token.tokenize(source)

    for token in tokens:
        print(token)

    input("Press enter to exit...")

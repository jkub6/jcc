"""
Main file for JCC.

This file is a part of Jake's C Compiler (JCC)
(c) Copyright 2019 Jacob Larkin
"""

import argparse

parser = argparse.ArgumentParser()

parser.add_argument('file', metavar='file',
                    help='input file to be compiled')

args = parser.parse_args()

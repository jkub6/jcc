"""
Main file for JCC.

This file is a part of Jake's C Compiler (JCC)
(c) Copyright 2019 Jacob Larkin
"""

import sys
import argparse

import jcc.parser
import jcc.generator
import jcc.assembler


def run():
    """Run JCC compiler."""
    # configure argparse
    argparser = argparse.ArgumentParser()
    argparser.add_argument("file", metavar="input_file",
                           help="input file location")
    argparser.add_argument("-o", "--output_file", metavar="output_file",
                           dest="output_file_name", default="a.out",
                           help="output file location", )
    argparser.add_argument("-v", "--verbose", action="store_true",
                           help="enables verbose output")
    args = argparser.parse_args()

    # read input file
    if args.verbose:
        print("[reading input file]")
    try:
        input_file_name = args.file
        input_file = open(input_file_name)
        input_data = input_file.read()
        input_file.close()
    except Exception as e:
        print(str(e))
        sys.exit(e.errno)

    # parse input_data
    if args.verbose:
        print("[parsing input data]")
    ast = jcc.parser.parse(input_data, input_file_name)

    # show recieved output
    if args.verbose:
        print("[c -> ast -> c code begin]")
        print(jcc.parser.ast_to_c(ast))
        print("[c -> ast -> c code end]")

    # generate assembly code
    if args.verbose:
        print("[generating assembly code]")
    assembly_data = jcc.generator.generate(ast)

    # generate binary code
    if args.verbose:
        print("[generating binary code]")
    binary_data = jcc.assembler.assemble(assembly_data)

    # write to output file
    if args.verbose:
        print("[writing to output file]")
    try:
        output_file_name = args.output_file_name
        output_file = open(output_file_name, "w")
        output_file.write(binary_data)
    except Exception as e:
        print(str(e))
        sys.exit(e.errno)

    if args.verbose:
        print("[JCC finished]")

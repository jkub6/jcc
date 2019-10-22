"""
File describing program flow for JCC.

This file is a part of Jake's C Compiler (JCC)
(c) Copyright 2019 Jacob Larkin
"""

import os
import sys
import argparse
from io import StringIO

import jcc.parser
import jcc.generator
import jcc.cleaner
import jcc.assembler


VERBOSE = False


def vprint(*argv):
    """Print only when verbose mode is on."""
    global VERBOSE
    if VERBOSE:
        print(*argv)


def parse_args(run_with_args=None):
    """Parse arguments given to JCC."""
    argparser = argparse.ArgumentParser()
    argparser.add_argument("file", metavar="input_file",
                           help="input file location")

    argparser.add_argument("-c", "--compile", action="store_true",
                           help="compile C file to assembly")
    argparser.add_argument("-a", "--assemble", action="store_true",
                           help="assemble input file to binary")
    argparser.add_argument("-l", "--output_cleaned", action="store_true",
                           help="output a file with the cleaned assembly")

    argparser.add_argument("-A", "--assemby_output",
                           metavar="assembly_output_file",
                           dest="assemby_output_filename", default="./out.s",
                           help="assembly output file location")
    argparser.add_argument("-L", "--cleaned_output",
                           metavar="cleaned_output_file",
                           dest="cleaned_output_filename", default="./out.scl",
                           help="cleaned assembly output file location")
    argparser.add_argument("-B", "--binary_output",
                           metavar="binary_output_file",
                           dest="binary_output_filename", default="./out.dat",
                           help="binary output file location")

#   argparser.add_argument("-r", "--readability", action="store_true",
#                          help="level (0-3) of assembly code readability" +
#                               "comments, spacing, etc...")
    argparser.add_argument('-r', '--readability', required=False, type=int,
                           choices=range(0, 4), metavar="[0-3]",
                           help="level (0-3) of assembly code readability \
                                comments, spacing, etc...", default=0)

    argparser.add_argument("-v", "--verbose", action="store_true",
                           help="enable verbose output")

    if run_with_args is not None:
        args = argparser.parse_args(run_with_args)
    else:
        args = argparser.parse_args()

    global VERBOSE
    VERBOSE = args.verbose

    return args


def read_file(filename):
    """Read data from file."""
    vprint("[reading input file \"{0}\"]".format(filename))
    try:
        file = open(filename, "r")
        data = file.read()
        file.close()
        return data
    except Exception as e:
        print(str(e))
        sys.exit(e.errno)


def write_file(filename, data):
    """Write data to file."""
    vprint("[writing output file \"{0}\"]".format(filename))
    try:
        os.makedirs(os.path.dirname(filename), exist_ok=True)
        file = open(filename, "w")
        file.write(data)
    except Exception as e:
        print(str(e))
        sys.exit(e.errno)


def parse_c_code(c_data, filename):
    """Parse C file and return an abstract syntax tree."""
    vprint("[parsing C code]")
    try:
        ast = jcc.parser.parse(c_data, filename)

        vprint("[interpreted C code begin]\n")
        vprint(jcc.parser.ast_to_c(ast))
        vprint("[interpreted C code end]")

        str_buf = StringIO()
        ast.show(buf=str_buf)

        vprint("[abstract syntax tree begin]\n")
        vprint(str_buf.getvalue())
        vprint("[abstract syntax tree end]")

        return ast
    except jcc.parser.ParseError as e:
        print("Parse Error: " + str(e))
        sys.exit(e.errno)


def generate_assembly_code(ast, readability):
    """Generate assembly code from C code."""
    vprint("[generating assembly code]")
    assembly_data = jcc.generator.generate(ast, readability)
    vprint("[generated assembly code begin]\n")
    vprint(assembly_data)
    vprint("[generated assembly code end]")
    return assembly_data


def clean_assembly(assembly_data):
    """Generate binary code from assembly code."""
    vprint("[cleaning assembly]")
    clean_data = jcc.cleaner.clean(assembly_data)
    vprint("[cleaned assembly begin]\n")
    vprint(clean_data)
    vprint("[cleaned assembly end]")
    return clean_data


def generate_binary_code(clean_data):
    """Generate binary code from assembly code."""
    vprint("[assembling to binary file]")
    binary_data = jcc.assembler.assemble(clean_data)
    short_data = binary_data.strip("00\n")
    vprint("[generated binary data begin]\n")
    diff = len(binary_data) - len(short_data)
    diff = int(diff/3)
    vprint(short_data + "\n(" + str(diff) + " blank lines truncated)...")
    vprint("[generated binary data end]")
    return binary_data


def finish():
    """End JCC execution."""
    vprint("[JCC finished]")


def run(run_with_args=None):
    """Run JCC compiler."""
    args = parse_args(run_with_args)

    if args.compile:
        c_data = read_file(args.file)
        ast = parse_c_code(c_data, args.file)
        assembly_data = generate_assembly_code(ast, args.readability)
        write_file(args.assemby_output_filename, assembly_data)
    else:
        assembly_data = read_file(args.file)

    if args.assemble:
        clean_data = clean_assembly(assembly_data)
        if args.output_cleaned:
            write_file(args.cleaned_output_filename, clean_data)
        binary_data = generate_binary_code(clean_data)
        write_file(args.binary_output_filename, binary_data)

    finish()

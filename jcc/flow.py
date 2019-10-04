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

VERBOSE = False


def vprint(*argv):
    """Print only when verbose mode is on."""
    global VERBOSE
    if VERBOSE:
        print(*argv)


def parse_args():
    """Parse arguments given to JCC."""
    argparser = argparse.ArgumentParser()
    argparser.add_argument("file", metavar="input_file",
                           help="input file location")
    argparser.add_argument("-a", "--assemby_output",
                           metavar="assembly_output_file",
                           dest="assemby_output_filename", default="out.s",
                           help="assembly output file location")
    argparser.add_argument("-b", "--binary_output",
                           metavar="binary_output_file",
                           dest="binary_output_filename", default="out.dat",
                           help="binary output file location")
    argparser.add_argument("-A", "--assemble_only", action="store_true",
                           help="assemble input file to binary (no C files)")
    argparser.add_argument("-C", "--compile_only", action="store_true",
                           help="compile C file to assembly (no binary)")
    argparser.add_argument("-v", "--verbose", action="store_true",
                           help="enable verbose output")
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
        return ast
    except jcc.parser.ParseError as e:
        print("Parse Error: " + str(e))
        sys.exit(e.errno)


def generate_assembly_code(ast):
    """Generate assembly code from C code."""
    vprint("[generating assembly code]")
    assembly_data = jcc.generator.generate(ast)
    return assembly_data


def generate_binary_code(assembly_data):
    """Generate binary code from assembly code."""
    vprint("[assembling to binary file]")
    binary_data = jcc.assembler.assemble(assembly_data)
    return binary_data


def finish():
    """End JCC execution."""
    vprint("[JCC finished]")
    sys.exit(0)


def run():
    """Run JCC compiler."""
    args = parse_args()

    if args.compile_only:
        c_data = read_file(args.file)
        ast = parse_c_code(c_data, args.file)
        assembly_data = generate_assembly_code(ast)
        write_file(args.assemby_output_filename, assembly_data)

    elif args.assemble_only:
        assembly_data = read_file(args.file)
        binary_data = generate_binary_code(assembly_data)
        write_file(args.binary_output_filename, binary_data)

    else:
        c_data = read_file(args.file)
        ast = parse_c_code(c_data, args.file)
        assembly_data = generate_assembly_code(ast)
        write_file(args.assemby_output_filename, assembly_data)
        binary_data = generate_binary_code(assembly_data)
        write_file(args.binary_output_filename, binary_data)

    finish()

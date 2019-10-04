"""
Parse C code into an abstract syntax tree for JCC.

This file is a part of Jake's C Compiler (JCC)
(c) Copyright 2019 Jacob Larkin
"""

import pycparser


class ParseError(Exception):
    """Raised when there is an error parsing the C code."""

    errno = 3


def parse(input_data, input_file_name, use_cpp=False):
    """Parse input source code and return as an abstract syntax tree."""
    if use_cpp:
        print("C preprocessing not implemented, ignoring...")

    parser = pycparser.CParser()

    try:
        ast = parser.parse(input_data, input_file_name)
    except pycparser.plyparser.ParseError as e:
        raise ParseError(str(e))

    return ast


def ast_to_c(ast):
    """Translate an abstract syntax tree to C code."""
    generator = pycparser.c_generator.CGenerator()
    return generator.visit(ast)

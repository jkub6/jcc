"""
Parse C code into an abstract syntax tree for JCC.

This file is a part of Jake's C Compiler (JCC)
(c) Copyright 2019 Jacob Larkin
"""

from pycparser import CParser, c_generator


def parse(input_data, input_file_name, use_cpp=False):
    """Parse input source code and return as an abstract syntax tree."""
    if use_cpp:
        print("C preprocessing not implemented, ignoring...")

    parser = CParser()
    return parser.parse(input_data, input_file_name)


def ast_to_c(ast):
    """Translate an abstract syntax tree to C code."""
    generator = c_generator.CGenerator()
    return generator.visit(ast)

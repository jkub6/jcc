"""
Testing file for JCC.

This file is a part of Jake's C Compiler (JCC)
(c) Copyright 2019 Jacob Larkin
"""

import jcc
from pycparser import c_ast


if __name__ == "__main__":
    jcc.flow.VERBOSE = True
    c_data = jcc.flow.read_file("tests/premade/stage_5/valid/exp_return_val.c")

    ast = jcc.flow.parse_c_code(c_data,
                                "tests/premade/stage_5/valid/exp_return.c")
    assembly_data = jcc.flow.generate_assembly_code(ast, 3)
    clean_data = jcc.flow.clean_assembly(assembly_data)
    binary_data = jcc.flow.generate_binary_code(clean_data)

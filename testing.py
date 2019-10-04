"""
Testing file for JCC.

This file is a part of Jake's C Compiler (JCC)
(c) Copyright 2019 Jacob Larkin
"""

import jcc

if __name__ == "__main__":
    c_data = jcc.flow.read_file("examples/pycparser/c_files/simple.c")
    ast = jcc.flow.parse_c_code(c_data, "examples/pycparser/c_files/simple.c")
    print(ast)
    # assembly_data = jcc.jcc.generate_assembly_code(ast)
    # jcc.binary_data = jcc.jcc.generate_binary_code(assembly_data)

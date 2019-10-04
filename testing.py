"""
Testing file for JCC.

This file is a part of Jake's C Compiler (JCC)
(c) Copyright 2019 Jacob Larkin
"""

import jcc
from pycparser import c_ast


if __name__ == "__main__":
    jcc.flow.VERBOSE = True
    c_data = jcc.flow.read_file("examples/pycparser/c_files/simple.c")
    c_data = """
int main(){int a = 1; return 0;}
int second(int v){return 1;}
int a(){return 2;}
    """
    ast = jcc.flow.parse_c_code(c_data, "examples/pycparser/c_files/simple.c")
    assembly_data = jcc.flow.generate_assembly_code(ast)
    clean_data = jcc.flow.clean_assembly(assembly_data)
    binary_data = jcc.flow.generate_binary_code(clean_data)

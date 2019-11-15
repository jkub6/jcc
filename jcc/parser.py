"""
Parse C code into an abstract syntax tree for JCC.

This file is a part of Jake's C Compiler (JCC)
(c) Copyright 2019 Jacob Larkin
"""

import re
import pycparser
from pycparser import c_generator


class ParseError(Exception):
    """Raised when there is an error parsing the C code."""

    errno = 3


def remove_comments(text):
    """Remove comments from c text while keeping line numbers."""
    done = ""
    for line in text.split("\n"):
        i = line.find("//")
        if i >= 0:
            done += line[:i] + "\n"
        else:
            done += line + "\n"
    return done
    #def replacer(match):
    #    s = match.group(0)
    #    lines = s.count("\n")
    #    out = "\n"*lines
    #    return out
    #pattern = re.compile(
    #    r'//.*?$|/\*.*?\*/|\'(?:\\.|[^\\\'])*\'|"(?:\\.|[^\\"])*"',
    #    re.DOTALL | re.MULTILINE
    #)
    #return re.sub(pattern, replacer, text)


def parse(input_data, input_file_name, use_cpp=False):
    """Parse input source code and return as an abstract syntax tree."""
    if use_cpp:
        print("C preprocessing not fully implemented, ignoring...")

    parser = pycparser.CParser()

    input_data = remove_comments(input_data)

    try:
        ast = parser.parse(input_data, input_file_name)
    except pycparser.plyparser.ParseError as e:
        raise ParseError(str(e))

    return ast


def ast_to_c(ast):
    """Translate an abstract syntax tree to C code."""
    generator = pycparser.c_generator.CGenerator()
    return generator.visit(ast)

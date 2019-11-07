"""
Preprocess C code.

This file is a part of Jake's C Compiler (JCC)
(c) Copyright 2019 Jacob Larkin
"""

import os
import re


def preprocess(c_data, filepath=None):
    """Preprocess C code."""
    cwd = os.getcwd()

    preprocessed_data = ""
    for line in c_data.split("\n"):
        line = line.strip()
        if line.startswith('#include "'):
            if filepath is not None:
                os.chdir(os.path.dirname(filepath))
            filepath = line.split('"')[1]
            file_data = open(filepath, "r")
            line = preprocess(file_data.read())
        elif line.startswith("#include <"):
            filepath = line.split('<')[1]
            filepath = os.path.join("./jstdlib/", filepath[:-1])
            file_data = open(filepath, "r")
            line = preprocess(file_data.read())

        preprocessed_data += line+"\n"

    os.chdir(cwd)
    return preprocessed_data

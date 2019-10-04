"""
Contains utility function for loading premade test files.

This file is a part of Jake's C Compiler (JCC)
(c) Copyright 2019 Jacob Larkin
"""

import os


def load_files(stage_num, valid):
    """Load all files for a given stage number."""
    c_assembly_pairs = []
    if valid:
        path = "./tests/premade/stage_{0}/valid".format(stage_num)
    else:
        path = "./tests/premade/stage_{0}/invalid".format(stage_num)
    filenames = os.listdir(path)
    for filename in filenames:
        if os.path.isfile(os.path.join(path, filename)):
            if filename.endswith(".c"):
                c_filepath = os.path.join(path, filename)
                assembly_filepath = os.path.join(path, filename[:-2]+".s")
                binary_filepath = os.path.join(path, filename[:-2]+".dat")
                c_data = open(c_filepath, "r").read()
                assembly_data = "None"
                binary_data = "None"
                # assembly_data = open(assembly_filepath, "r").read()
                # binary_data = open(binary_filepath, "r").read()
                c_assembly_pairs.append((c_data, assembly_data, binary_data))
    return c_assembly_pairs

"""
Contains tests for the assembler.

This file is a part of Jake's C Compiler (JCC)
(c) Copyright 2019 Jacob Larkin
"""

import pytest

import os


def load_stage_files(stage_num, valid):
    """Load all files for a given stage number."""
    c_assembly_pairs = []
    if valid:
        path = "./tests/premade_c_to_assembly/"\
               "stage_{0}/valid".format(stage_num)
    else:
        path = "./tests/premade_c_to_assembly/"\
               "stage_{0}/invalid".format(stage_num)
    filenames = os.listdir(path)
    for filename in filenames:
        if os.path.isfile(os.path.join(path, filename)):
            if filename.endswith(".c"):
                c_filepath = os.path.join(path, filename)
                assembly_filepath = os.path.join(path, filename[:-2]+".s")
                c_data = open(c_filepath, "r").read()
                assembly_data = "None"
                # assembly_data = open(assembly_filepath, "r").read()
                # c_assembly_pairs.append((c_data, assembly_data))
    return c_assembly_pairs


def test_premade_c_to_assembly_stage_1_valid():
    """Test a whole bunch of premade C/assembly file pairs."""
    for pair in load_stage_files(1, True):
        print(pair[0])

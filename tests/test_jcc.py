"""
Contains tests for jcc.

This file is a part of Jake's C Compiler (JCC)
(c) Copyright 2019 Jacob Larkin
"""

import pytest

import shutil

import jcc
import tests.premade


tmp_args = ["file", "-cla", "-A", "tests/tmp/tmp.s",
            "-L", "tests/tmp/tmp.scl", "-B", "tests/tmp/tmp.dat"]


def test_premade_stage_1_valid():
    """Test parsing a whole bunch of premade file groups."""
    for file_group in tests.premade.load_files(1, True):
        tmp_args[0] = file_group.c_filepath

        jcc.run(tmp_args)

        with open(tmp_args[3], "r") as assembly_file:
            assert assembly_file.read() == file_group.assembly_data
        with open(tmp_args[5], "r") as cleaned_file:
            assert cleaned_file.read() == file_group.clean_data
        # with open(tmp_args[7], "r") as binary_file:
        #     assert binary_file.read() == file_group.binary_data

        shutil.rmtree("tests/tmp")

        


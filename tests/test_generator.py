"""
Contains tests for the generator.

This file is a part of Jake's C Compiler (JCC)
(c) Copyright 2019 Jacob Larkin
"""

import pytest

import jcc
import tests.premade


def test_premade_stage_1_valid():
    """Test parsing a whole bunch of premade C files."""
    for file_group in tests.premade.load_files(1, True):
        ast = jcc.parser.parse(file_group.c_data, file_group.c_filepath)
        assembly_data = jcc.generator.generate(ast)
        assert file_group.assembly_data == assembly_data
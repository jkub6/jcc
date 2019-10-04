"""
Contains tests for the assembler.

This file is a part of Jake's C Compiler (JCC)
(c) Copyright 2019 Jacob Larkin
"""

import pytest

import jcc
import tests.premade


def test_import():
    """Test import."""
    import jcc.cleaner


def test_premade_stage_1_valid():
    """Test parsing a whole bunch of premade C files."""
    for file_group in tests.premade.load_files(1, True):
        ast = jcc.parser.parse(file_group.c_data, file_group.c_filepath)
        assembly_data = jcc.generator.generate(ast)
        clean_data = jcc.cleaner.clean(assembly_data)
        assert file_group.clean_data == clean_data

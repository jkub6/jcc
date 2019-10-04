"""
Contains tests for the parser.

This file is a part of Jake's C Compiler (JCC)
(c) Copyright 2019 Jacob Larkin
"""

import pytest

import jcc
import tests.premade


def test_import():
    """Test import."""
    import jcc.parser


def test_premade_stage_1_valid():
    """Test parsing a whole bunch of premade C files."""
    for file_group in tests.premade.load_files(1, True):
        jcc.parser.parse(file_group.c_data, file_group.c_filepath)


def test_premade_stage_2_valid():
    """Test parsing a whole bunch of premade C files."""
    for file_group in tests.premade.load_files(1, True):
        jcc.parser.parse(file_group.c_data, file_group.c_filepath)


def test_premade_stage_3_valid():
    """Test parsing a whole bunch of premade C files."""
    for file_group in tests.premade.load_files(1, True):
        jcc.parser.parse(file_group.c_data, file_group.c_filepath)


def test_premade_stage_4_valid():
    """Test parsing a whole bunch of premade C files."""
    for file_group in tests.premade.load_files(1, True):
        jcc.parser.parse(file_group.c_data, file_group.c_filepath)


def test_premade_stage_5_valid():
    """Test parsing a whole bunch of premade C files."""
    for file_group in tests.premade.load_files(1, True):
        jcc.parser.parse(file_group.c_data, file_group.c_filepath)


def test_premade_stage_6_valid():
    """Test parsing a whole bunch of premade C files."""
    for file_group in tests.premade.load_files(1, True):
        jcc.parser.parse(file_group.c_data, file_group.c_filepath)


def test_premade_stage_7_valid():
    """Test parsing a whole bunch of premade C files."""
    for file_group in tests.premade.load_files(1, True):
        jcc.parser.parse(file_group.c_data, file_group.c_filepath)


def test_premade_stage_8_valid():
    """Test parsing a whole bunch of premade C files."""
    for file_group in tests.premade.load_files(1, True):
        jcc.parser.parse(file_group.c_data, file_group.c_filepath)


def test_premade_stage_9_valid():
    """Test parsing a whole bunch of premade C files."""
    for file_group in tests.premade.load_files(1, True):
        jcc.parser.parse(file_group.c_data, file_group.c_filepath)


def test_premade_stage_10_valid():
    """Test parsing a whole bunch of premade C files."""
    for file_group in tests.premade.load_files(1, True):
        jcc.parser.parse(file_group.c_data, file_group.c_filepath)


# def test_premade_stage_1_invalid():
#     """Test parsing a whole bunch of premade C files."""
#     for file_group in tests.premade.load_files(1, False):
#         print(file_group.c_filepath)
#         with pytest.raises(jcc.parser.ParseError):
#             jcc.parser.parse(file_group.c_data, file_group.c_filepath)

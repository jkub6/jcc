"""
Contains tests for the generator.

This file is a part of Jake's C Compiler (JCC)
(c) Copyright 2019 Jacob Larkin
"""

import pytest

import tests.premade


def test_premade_stage_1_valid():
    """Test a whole bunch of premade C/assembly file pairs."""
    for pair in tests.premade.load_files(1, True):
        print(pair[0])

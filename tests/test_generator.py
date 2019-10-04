"""
Contains tests for the generator.

This file is a part of Jake's C Compiler (JCC)
(c) Copyright 2019 Jacob Larkin
"""

import pytest


@pytest.mark.order1
def test_import():
    """Test import."""
    import jcc.generator

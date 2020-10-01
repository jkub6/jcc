"""
Contains tests to see if dff is working properly.

This file is a part of Jake's C Compiler (JCC)
(c) Copyright 2019 Jacob Larkin
"""

import pytest
from cocotb_test.run import run
import os


def test_dff():
    """Test running verilog testbench."""
    run(
        verilog_sources=["./tests/dff/verilog/dff.v"],
        toplevel="dff_test",
        module="dff_cocotb",
        sim_build="./tests/dff/verilog/sim_build"
    )

"""
Contains tests to see if pytest is working properly.

This file is a part of Jake's C Compiler (JCC)
(c) Copyright 2019 Jacob Larkin
"""

import pytest
from cocotb_test.run import run


@pytest.mark.skip("Don't have Verilog Processor code yet")
def test_dff():  # test
    """Test running verilog testbench."""
    run(
        verilog_sources=["verilog/dff.v"],  # sources
        toplevel="dff_test",             # top level HDL
        module="dff_cocotb",
        sim_build="tests/verilog/sim_build"
    )

"""
Contains tests to see if the processor is working correctly.

This file is a part of Jake's C Compiler (JCC)
(c) Copyright 2019 Jacob Larkin
"""

import pytest
from cocotb_test.run import run
import os

def setup_module(module):
    """ setup any state specific to the execution of the given module."""

def test_processor():
    """Test running verilog testbench."""
    run(
        verilog_sources=["./tests/processor/verilog/alu.v",
                         "./tests/processor/verilog/bitgen.v"
                         "./tests/processor/verilog/btn_debounce.v",
                         "./tests/processor/verilog/controller.v"
                         "./tests/processor/verilog/dataPath.v",
                         "./tests/processor/verilog/exmem.v"
                         "./tests/processor/verilog/glyphs.v",
                         "./tests/processor/verilog/instructionRegister.v"
                         "./tests/processor/verilog/LSFR.v",
                         "./tests/processor/verilog/mux2.v",
                         "./tests/processor/verilog/mux4.v",
                         "./tests/processor/verilog/programcounter.v"
                         "./tests/processor/verilog/regfile.v",
                         "./tests/processor/verilog/register.v",
                         "./tests/processor/verilog/shifter.v",
                         "./tests/processor/verilog/signExtend.v",
                         "./tests/processor/verilog/statemachine.v",
                         "./tests/processor/verilog/switch_tester.v",
                         "./tests/processor/verilog/top.v",
                         "./tests/processor/verilog/vga_control.v",
                         "./tests/processor/verilog/vga.v"],
        toplevel="top",
        module="tests.processor.processor_cocotb",
        sim_build="./tests/processor/verilog/sim_build"
    )

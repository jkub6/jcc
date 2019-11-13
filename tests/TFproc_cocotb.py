"""
Cocotb testbench for TFproc.

This file is a part of Jake's C Compiler (JCC)
(c) Copyright 2019 Jacob Larkin
"""

import os
import random
import logging
import shutil


import cocotb
from cocotb.clock import Clock
from cocotb.decorators import coroutine
from cocotb.triggers import Timer, RisingEdge, ReadOnly, Edge
from cocotb.monitors import Monitor
from cocotb.drivers import BitDriver
from cocotb.binary import BinaryValue
from cocotb.regression import TestFactory
from cocotb.scoreboard import Scoreboard
from cocotb.result import TestFailure, TestSuccess

import jcc

logging.getLogger('cocotb').setLevel(logging.ERROR)
logging.basicConfig(level=logging.DEBUG)


@cocotb.coroutine
def clock_gen(signal):
    """Generate the clock signal."""
    while True:
        signal <= 0
        yield Timer(20000)  # ps
        signal <= 1
        yield Timer(20000)  # ps


@cocotb.coroutine
def run_file(dut, filepath):
    """Load and run Dat file in processor."""
    cocotb.fork(clock_gen(dut.clk))
    clkedge = RisingEdge(dut.clk)

    dut.reset <= 1
    dut.loadedAdr <= 0

    yield clkedge

    file = open(filepath, "r")
    data = file.read().strip()
    file.close()

    # print(data)

    for i, line in enumerate(data.split("\n")):
        dut.reset <= 0
        vec = BinaryValue()
        vec.integer = int(line, 16)
        dut.memory.ram[i].setimmediatevalue(vec)
        if line == "0000":
            break

    cycles = 0
    last_pc = 0
    pcs_in_row = 0
    while pcs_in_row < 10 and (cycles < 5000):
        yield clkedge

        pc = dut.proc.dp.progcount.count.value.integer
        if last_pc == pc:
            pcs_in_row += 1
        else:
            pcs_in_row = 0
            last_pc = pc
            # print("RA", dut.proc.dp.regFile.RAM[0])
            # print("T0", dut.proc.dp.regFile.RAM[1])
            # print("T1", dut.proc.dp.regFile.RAM[2])
            # print("SP", dut.proc.dp.regFile.RAM[15])
            # print("BP", dut.proc.dp.regFile.RAM[14])
            # print("RAM <e000>", dut.memory.ram[57344])
            # print("RAM <dfff>", dut.memory.ram[57343])
            # print("RAM <dffe>", dut.memory.ram[57342])
            # print("RAM <dffd>", dut.memory.ram[57341])
            # print("RAM <deec>", dut.memory.ram[57340])
            # print("---> pc", pc, ":", data.split("\n")[pc])

        cycles += 1
    # print("prog over ----------")

    cycles -= 10  # remove cycles from in loop

    return dut.proc.dp.regFile.RAM[0].value.integer


@cocotb.coroutine
def run_test(dut):
    """Configure testbench and run a test."""
    log = logging.getLogger('run_test')
    with open("../../temp_files.txt") as f:
        data = f.read()
    files = data.strip().split("\n")

    rets = []

    for i, filepath in enumerate(files):
        try:
            log.debug("Simulation: {}/{}".format(i, len(files)))
            tmp_args = ["../../"+filepath, "-cla", "-A", "./tmp/tmp.s",
                        "-L", "./tmp/tmp.scl", "-B", "./tmp/tmp.dat"]
            jcc.run(tmp_args)
            ret = yield run_file(dut, "./tmp/tmp.dat")
            rets.append(str(ret))
        except:
            rets.append("FAIL")

    with open("../../temp_results.txt", "w") as f:
        for ret in rets:
            f.write(ret + "\n")

    shutil.rmtree("tmp")


factory = TestFactory(run_test)
factory.generate_tests()

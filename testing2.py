"""
Contains tests to see if TFproc is working properly.

This file is a part of Jake's C Compiler (JCC)
(c) Copyright 2019 Jacob Larkin
"""

import os
import shutil
import subprocess

from cocotb_test.run import run

import jcc


def load_filepaths(stage_num, valid):
    """Load all filepaths for a given stage number."""
    filepaths = []
    if valid:
        path = "premade/stage_{0}/valid".format(stage_num)
    else:
        path = "premade/stage_{0}/invalid".format(stage_num)
    filenames = os.listdir("tests/"+path)
    for filename in filenames:
        if os.path.isfile(os.path.join("tests/"+path, filename)):
            if filename.endswith(".c"):
                filepath = os.path.join(path, filename)
                filepaths.append(filepath)
    return filepaths


stages = [i+2 for i in range(1)]
parameters = []
files = []
ids = []
i = 0
for stage in stages:
    print("sf")
    for filepath in load_filepaths(stage, True):
        parameters.append((stage, i, filepath))
        files.append(filepath)
        ids.append(str(stage) + ":" + filepath[:-2])
        i += 1

verilog_results = []
print(parameters)


def setup_module(module):
    """Run all programs and save output to global var."""
    global verilog_results

    with open("./tests/temp_files.txt", "w") as f:
        for filepath in files:
            f.write(filepath + "\n")

    run(
        verilog_sources=["TFproc/alu.v", "TFproc/controller.v",
                         "TFproc/datapath.v", "TFproc/memTest.v",
                         "TFproc/ProcConnect.v", "TFproc/Processor.v",
                         "TFproc/regfile.v"],
        toplevel="ProcConnect",
        module="TFproc_cocotb",
        sim_build="tests/TFproc/sim_build"
    )
    print("ran")

    with open("./tests/temp_results.txt") as f:
        results = f.read()

    for line in results.strip().split("\n"):
        verilog_results.append(line)


def gcc_and_run(filepath):
    """Compile, run and get output of .c file."""
    gccOut = subprocess.Popen(["gcc", "-o", "./tmp/tmp", filepath],
                              stdout=subprocess.PIPE,
                              stderr=subprocess.STDOUT)
    gccStdout, gccStderr = gccOut.communicate()
    print(gccStdout)
    print(gccStderr)

    progOut = subprocess.Popen("./tmp/tmp",
                               stdout=subprocess.PIPE,
                               stderr=subprocess.STDOUT)
    progStdout, progStderr = progOut.communicate()
    print(progStdout)
    print(progStderr)

    return progOut.returncode


def test_file():
    """Configure testbench and run a test."""
    global verilog_results
    result = int(verilog_results[num]) % 255

    os.mkdir("tmp")

    answer = gcc_and_run("tests/"+filepath)

    shutil.rmtree("tmp")

    assert answer == result

test_file()

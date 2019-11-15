"""
Contains tests to see if TFproc is working properly.

This file is a part of Jake's C Compiler (JCC)
(c) Copyright 2019 Jacob Larkin
"""

import os
import ntpath
import shutil
import subprocess

import pytest
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


skips = ["3div", "3mod", "3associativity_2"]
skips += ["4skip_on_failure_short_circuit_or",
          "4skip_on_failure_short_circuit_and",
          "4skip_on_failure_multi_short_circuit"]
skips += ["8break", "8continue_empty_post", "8continue", "8do_while",
          "8for_nested_scope",
          "8for_variable_shadow", "8nested_break"]
skips += ["8nested_while", "8continue_in_while"]
skips += ["1bin_num", "1hex_num"]

skips += ["9fun_in_expr", "9hello_world", "9later_decl",
          "9rename_function_param", "9mutual_recursion"]
skips += ["10forward_declaration",
          "10global_not_initialized"]
skips += ["11both", "11dereference", "11basic_array"]
skips += ["11write_mem", "11address"]
# stages = [i+6 for i in range(1)]
stages = [i+13 for i in range(1)]
parameters = []
files = []
ids = []
i = 0
for stage in stages:
    for filepath in load_filepaths(stage, True):
        filename = ntpath.basename(filepath)
        if str(stage)+filename[:-2] in skips:
            continue
        parameters.append((stage, i, filepath))
        files.append(filepath)
        ids.append(str(stage) + ":" + filename[:-2])
        i += 1
# files = ["premade/stage_3/valid/sub.c"]
# parameters = [(3, 0, "premade/stage_3/valid/sub.c")]
# ids = ["yee"]
verilog_results = []
print(parameters)


def setup_module(module):
    """Run all programs and save output to global var."""
    global verilog_results

    try:
        os.mkdir("tmp")
    except FileExistsError:
        pass

    with open("./tests/temp_files.txt", "w") as f:
        for filepath in files:
            f.write(filepath + "\n")

    run(
        verilog_sources=["TFproc/alu.v", "TFproc/controller.v",
                         "TFproc/datapath.v", "TFproc/procMem.v",
                         "TFproc/ProcConnect.v", "TFproc/Processor.v",
                         "TFproc/regfile.v"],
        toplevel="ProcConnect",
        module="TFproc_cocotb",
        sim_build="tests/TFproc/sim_build"
    )
    os.remove("./tests/temp_files.txt")

    with open("./tests/temp_results.txt") as f:
        results = f.read()
    os.remove("./tests/temp_results.txt")

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


@pytest.mark.parametrize("stage, num, filepath", parameters, ids=ids)
def test_files(stage, num, filepath):
    """Configure testbench and run a test."""
    global verilog_results
    result = int(verilog_results[num]) % 256
    try:
        answer = gcc_and_run("tests/"+filepath)
    except:
        print("Error compiling file")
        raise Exception("Error compiling file")

    assert answer == result


def teardown_module(module):
    """Tear down the test module."""
    shutil.rmtree("tmp")
